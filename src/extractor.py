
from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate


from src.schemas import CharacterInfo



def extract_character_info(context: str, character_name: str, story_title: str) -> CharacterInfo:
    parser = PydanticOutputParser(pydantic_object=CharacterInfo)

    prompt = PromptTemplate(
        template="""

You are extracting factual information about a character from a story.
Use ONLY the provided context. 
If the character is not mentioned, return an error or 'No information available'.

Character name: {character_name}
Story title: {story_title}
Context:
{context}
Character roles are limited to one of the following:
- Protagonist
- Villain
- Side character
If unsure about the role due to lack of context, default to "Side character".

{format_instructions}
""",
        input_variables=["context", "character_name", "story_title"],
        partial_variables={
            "format_instructions": parser.get_format_instructions()
        },
    )

    llm = ChatMistralAI(
        model="mistral-large-latest",
        temperature=0,
    )

    chain = prompt | llm | parser

    return chain.invoke(
        {
            "context": context,
            "character_name": character_name,
            "story_title": story_title
        }
    )
