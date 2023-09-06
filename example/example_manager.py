from langchain import FAISS, FewShotPromptTemplate, PromptTemplate, LLMChain
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain.chat_models import ChatOpenAI
from transformers.pipelines import task


from langchain.prompts.example_selector import SemanticSimilarityExampleSelector

import config
from example import prompt_examples
from fastapi import Body
from knowledge_base import basic_knowledge
from embedding import embedding_utils
import json

from database import vector_store_utils

embeddings = embedding_utils.embeddings

example_selector = SemanticSimilarityExampleSelector.from_examples(prompt_examples.prompt_examples, embeddings, FAISS, k=config.VECTOR_SEARCH_TOP_K)

def search_examples(query: str = Body(..., description="用户输入", examples=["你好"])):
    #首先从基础知识库里面检索对应的基础只是
    docs = vector_store_utils.search_in_vector_store(query=query, knowledge_base_name=basic_knowledge.basic_knowledge_name, top_k=1)

    #由于我设置的top_k=1,所以这里最多只有一个元素
    doc = docs[0]


    #获取到根据输入匹配到的对应的examples
    examples = [example_.update({"basic_knowledge":doc.page_content}) for example_ in example_selector.select_examples({"input": query})]

    return examples

    # for selected_example in selected_examples:
    #     template = PromptTemplate.from_template(template="role: {role}\nused basic knowledge: {basic_knowledge}\nQuestion: {"
    #                                           "input}\nAnswer :{output}",
    #                                  partial_variables=selected_example,
    #                                  suffix="Question: {input}"
    #                                  )
    #     template.partial(basic_knowledge="doc.page_content")
    #
    #     template.format()
    #
    #     chain = LLMChain(prompt=template, llm=model)
    #
    #     answer = ""
    #     async for token in callback.aiter():
    #         answer += token
    #     yield json.dumps({"answer": answer},
    #                      ensure_ascii=False)




