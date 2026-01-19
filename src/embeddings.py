import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_core.documents import Document



load_dotenv()


DATASET_PATH = Path("Dataset/langchain-assignment-dataset/stories")
VECTORSTORE_PATH = "vectorstore"

def load_vectorstore():
    embeddings = MistralAIEmbeddings(
        model="mistral-embed",
        api_key=os.getenv("MISTRAL_API_KEY"),
    )
    return Chroma(
        persist_directory=VECTORSTORE_PATH,
        embedding_function=embeddings,
    )

def compute_embeddings():
    if not DATASET_PATH.exists():
        raise RuntimeError(
            "Dataset not found. Please place story files inside Dataset/stories/"
        )

    embeddings = MistralAIEmbeddings(
        model="mistral-embed",
        api_key=os.getenv("MISTRAL_API_KEY"),
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
    )

    documents = []

    for file in DATASET_PATH.glob("*.txt"):
        text = file.read_text(encoding="utf-8")
        
        # Grab first line as story title
        first_line = text.strip().split("\n")[0]  # First line of txt file
        story_title = first_line if first_line else file.stem

        chunks = splitter.split_text(text)
        for chunk in chunks:
            documents.append(
                Document(
                    page_content=chunk,
                    metadata={"story_title": story_title},
                )
            )


    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=VECTORSTORE_PATH,
    )

    vectorstore.persist()
    print(f"Stored {len(documents)} chunks in vector database.")
