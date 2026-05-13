from app.retrieval import retrieve_knowledge


def answer_worker(question: str):

    knowledge = retrieve_knowledge(question)

    if not knowledge:
        return "No verified operational knowledge found."

    return "\n".join(knowledge)

# from app.retrieval import retrieve_knowledge


# def answer_worker(question: str):

#     knowledge = retrieve_knowledge(question)

#     if not knowledge:
#         return "No verified operational knowledge found."

#     return "\n".join(knowledge)

# from app.retrieval import retrieve_knowledge
# from langchain_ollama import ChatOllama


# llm = ChatOllama(
#     model="tinyllama"
# )


# def answer_worker(question: str):

#     knowledge = retrieve_knowledge(question)

#     context = "\n".join(knowledge)

#     prompt = f"""
# You are a factory co-worker AI.

# Use ONLY verified operational knowledge.

# Knowledge:
# {context}

# Question:
# {question}
# """

#     response = llm.invoke(prompt)

#     return response.content

# from app.retrieval import retrieve_knowledge
# from langchain_ollama import ChatOllama


# llm = ChatOllama(
#     model="tinyllama"
# )


# def answer_worker(question: str):

#     knowledge = retrieve_knowledge(question)

#     context = "\n".join(knowledge)

#     prompt = f"""
# Factory operational knowledge:

# {context}

# Worker question:
# {question}

# Answer the worker question using the operational knowledge above.
# Be short and direct.
# """

#     response = llm.invoke(prompt)

#     return response.content

