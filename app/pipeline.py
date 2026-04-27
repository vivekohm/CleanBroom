from app.retriever import search
from app.llm import ask_llama

def query_system(question):
    context = search(question)

    prompt = f"""
    You are a helpful assistant.
    Answer ONLY from the context below.

    Context:
    {context}

    Question:
    {question}
    """

    return ask_llama(prompt)