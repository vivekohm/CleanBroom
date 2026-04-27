from app.retriever import search
from app.llm import ask_llama

def query_system(question):
    context = search(question)

    prompt = f"""
    You are a strict document assistant.

    Use ONLY the provided context to answer the question.
    If the answer is not explicitly in the context, reply exactly:
    "I don't know based on the provided document."
    
    Do NOT use any external knowledge.
    Do NOT make assumptions.


    Context:
    {context}

    Question:
    {question}
    """

    return ask_llama(prompt)