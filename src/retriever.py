import os
from dotenv import load_dotenv
from src.embeddings import load_vectorstore


load_dotenv()

VECTORSTORE_PATH = "vectorstore"

def get_relevant_context(query: str, k: int = 5, min_score: float = 0.2):
    vectorstore = load_vectorstore()
    docs_with_scores = vectorstore.similarity_search_with_score(query, k=k)
    
    filtered_docs = [doc for doc, score in docs_with_scores if score >= min_score]
    if not filtered_docs and docs_with_scores:
        filtered_docs = [docs_with_scores[0][0]]
    if not filtered_docs:
        return "", None

    context = "\n".join(doc.page_content for doc in filtered_docs)

    # Prevent hallucination: only return context if character exists
    if query.lower() not in context.lower():
        return "", None

    story_title = filtered_docs[0].metadata.get("story_title", "Unknown")
    return context, story_title
