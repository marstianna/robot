from typing import List

from fastapi import Body, Request
from langchain import PromptTemplate, LLMChain
from starlette.responses import StreamingResponse

import config
from example import example_service

from llm import llm_utils


async def chat(query: str = Body(..., description="用户输入", examples=["你好"]),
               knowledge_base_name: str = Body(..., description="知识库名称", examples=["samples"]),
               top_k: int = Body(config.VECTOR_SEARCH_TOP_K, description="匹配向量数"),
               request: Request = None, ):
    context, examples = example_service.search_examples(query)
    if examples is None:
        return context

    async def chat_iterator(query: str,
                            examples: List[dict],
                            top_k: int):
        for example in examples:
            template = PromptTemplate(input_variables=["role", "basic_knowledge", "input", "output", "query"],
                                      template="{role}\n{basic_knowledge}\n{action}\ninput: {input}\noutput: "
                                               "{output}\ninput: {query}\noutput: ").partial(
                **example)

            print("template info :" + template.format(query=query))
            call = llm_utils.call(prompt=template.format(query=query), top_k=2)
            print(call)
            yield call

    return StreamingResponse(chat_iterator(query, examples, top_k),
                             media_type="text/event-stream")
