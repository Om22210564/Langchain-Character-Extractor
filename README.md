## LangChain Character Extractor

This project extracts structured information about characters from stories using LangChain, Mistral AI embeddings, and a local Chroma vector database.

### Features

Compute embeddings for story text and store them locally.

Search for a character and retrieve structured details in JSON format:

Name

Story title

Summary

Relations

Character role (Protagonist, Villain, Side character)

Handles edge cases when the character is not found.

### Dataset

The dataset contains multiple story files (.txt), one per story.

The first line of each file is used as the story title.

Example structure:
Dataset/
└── langchain-assignment-dataset/
    └── stories/
        ├── a-mother.txt
        ├── sorrow.txt
        ├── the-lantern-keepers.txt
        ├── the-poor-relations-story.txt
        └── the-schoolmistress.txt
"The dataset is referenced as a submodule. It should be cloned separately or downloaded as instructed."

### Setup

Create a virtual environment:

python -m venv myenv
source myenv/Scripts/activate      # Windows
# or
source myenv/bin/activate          # macOS/Linux


Install dependencies:

pip install -r requirements.txt


Add your Mistral API key in .env:

MISTRAL_API_KEY=<your_api_key_here>

Setup

Create a virtual environment:

python -m venv myenv
source myenv/Scripts/activate      # Windows
# or
source myenv/bin/activate          # macOS/Linux


Install dependencies:

pip install -r requirements.txt


Add your Mistral API key in .env:

MISTRAL_API_KEY=<your_api_key_here>

Notes

vectorstore/ is automatically created when embeddings are computed. It is not included in the repo.

Character roles are limited to Protagonist, Villain, Side character.

Ensure the dataset folder exists as shown above before running the commands.

### Folder Structure
langchain-character-extractor/
├── Dataset/                     # Story files (submodule or downloaded)
├── vectorstore/                 # Persisted embeddings (created after compute)
├── src/
│   ├── cli.py                   # CLI commands
│   ├── embeddings.py            # Embedding computation
│   ├── retriever.py             # Vector search logic
│   ├── extractor.py             # Character info extraction
│   └── schemas.py               # Pydantic schemas
├── requirements.txt
├── .gitignore
├── .env
└── myenv
