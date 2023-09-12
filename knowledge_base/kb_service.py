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
        context = "将以下知识库内容:\n"+context+"\n根据语意进行，重新组织语言，使其容易阅读和理解，但是不能修改其原有内容，也不能新加内容。"
        print(llm_utils.call(context))

    return docs


def add_kb(input: str):
    basic_knowledge.basic_knowledge.append(input)
