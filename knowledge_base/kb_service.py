from database import vector_store_utils
from knowledge_base import basic_knowledge
from llm import llm_utils

def search_kb(query: str,top_k: int,score_threshold: float,refactor: bool = False):
    docs = vector_store_utils.search_in_vector_store(query=query,
                                                      knowledge_base_name=basic_knowledge.basic_knowledge_name,
                                                      top_k=top_k, score_threshold=score_threshold)
    print(docs)
    if refactor:
        context = "。".join([doc.page_content for doc in docs])
        print(llm_utils.call(context))

    return docs


def add_kb(input: str):
    basic_knowledge.basic_knowledge.append(input)
