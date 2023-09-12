from database import vector_store_utils
from knowledge_base import basic_knowledge
from llm import llm_utils

def search_kb(query: str,top_k: int,score_threshold: float,refactor: bool = False):
    docs = vector_store_utils.search_in_vector_store(query=query,
                                                      knowledge_base_name=basic_knowledge.basic_knowledge_name,
                                                      top_k=top_k, score_threshold=score_threshold)
    print(docs)
    if refactor:
        context = "\n".join([doc.page_content for doc in docs])
        context = "针对以下语句，把每一行作为单独语句，然后根据语意将文字内容进行重排序，并润色，但是不能修改其原有内容，也不能新加内容：\n" + context
        print(llm_utils.call(context))

    return docs


def add_kb(input: str):
    basic_knowledge.basic_knowledge.append(input)
