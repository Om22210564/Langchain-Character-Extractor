import json
import typer
from rich import print

from src.embeddings import compute_embeddings
from src.retriever import get_relevant_context
from src.extractor import extract_character_info


app = typer.Typer()


@app.command()
def compute_embeddings_cmd():
    """Compute and persist embeddings for all stories."""
    compute_embeddings()

@app.command()
def get_character_info(name: list[str]):
    """Retrieve structured character information."""
    full_name = " ".join(name)
    context, story_title = get_relevant_context(full_name)

    if not context:
        print(json.dumps(
            {
                "name": full_name,
                "storyTitle": "No information",
                "summary": "No information available",
                "relations": [],
                "characterType": "No information available"
            },
            indent=2
        ))
        return

    result = extract_character_info(context, full_name, story_title)
    print(json.dumps(result.model_dump(), indent=2))


if __name__ == "__main__":
    app()
