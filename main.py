import sys
import os

from llm import llm_utils

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import argparse
import uvicorn
from starlette.responses import RedirectResponse
from example.example_api import add_examples, delete_example, query_examples, list_examples, reload_examples,test_examples
from knowledge_base.kb_service import search_kb,add_kb
from api.chat_api import chat
import config
from fastapi import FastAPI
from database import vector_store_utils
from knowledge_base import basic_knowledge
from langchain.schema import Document
from api.data_cleaning_api import damo_text_split
from api.generate_prompt_api import generate_similar_fine_tuning_prompt,generate_similar_basic_knowledge,generate_similar_basic_knowledge2,generate_similar_basic_knowledge3
from api.health_check import health_check
from api.test_api import test_split

async def document():
    return RedirectResponse(url="/docs")


def create_app():
    app = FastAPI(
        title="Global Robot Server",
        version=config.VERSION
    )

    app.get("/examples/reload",
            tags=["ExampleManager"],
            summary="重载examples")(reload_examples)
    app.get("/examples/query",
            tags=["ExampleManager"],
            summary="查询examples")(query_examples)
    app.get("/examples/test",
            tags=["ExampleManager"],
            summary="测试examples")(test_examples)
    app.get("/examples/add",
            tags=["ExampleManager"],
            summary="添加example")(add_examples)
    app.get("/examples/list",
            tags=["ExampleManager"],
            summary="获取所有examples")(list_examples)
    app.get("/examples/delete",
            tags=["ExampleManager"],
            summary="删除examples")(delete_example)
    app.get("/kb/search",
            tags=["KB"],
            summary="查询KB")(search_kb)
    app.get("/kb/add_kb",
            tags=["KB"],
            summary="添加KB")(add_kb)
    app.get("/chat",
            tags=["Chat"],
            summary="对话")(chat)
    app.get("/status.taobao",
            tags=["healthCheck1"],
            summary="健康检查")(health_check)
    app.get("/checkpreload.htm",
            tags=["healthCheck2"],
            summary="健康检查")(health_check)
    app.get("/",
            tags=["healthCheck3"],
            summary="健康检查")(health_check)
    app.get("/data_cleaning/damo_split",
            tags=["only_Chat"],
            summary="达摩院模型拆分")(damo_text_split)
    app.get("/generate_prompt/basic_knowledge",
            tags=["generate_basic_knowledge"],
            summary="自动生成知识库")(generate_similar_basic_knowledge)
    app.get("/generate_prompt/basic_knowledge2",
            tags=["generate_basic_knowledge"],
            summary="自动生成知识库")(generate_similar_basic_knowledge2)
    app.get("/generate_prompt/basic_knowledge3",
            tags=["generate_basic_knowledge"],
            summary="自动生成知识库")(generate_similar_basic_knowledge3)
    app.get("/generate_prompt/fine_tuning_prompt",
            tags=["generate_fine_tuning_prompt"],
            summary="自动微调语料")(generate_similar_fine_tuning_prompt)
    app.get("/test/test_split",
            tags=["test1"],
            summary="测试")(test_split)
    return app


app = create_app()


def run_api(host, port, **kwargs):
    if kwargs.get("ssl_keyfile") and kwargs.get("ssl_certfile"):
        uvicorn.run(app,
                    host=host,
                    port=port,
                    ssl_keyfile=kwargs.get("ssl_keyfile"),
                    ssl_certfile=kwargs.get("ssl_certfile"),
                    )
    else:
        uvicorn.run(app, host=host, port=port)


def init():
    os.environ.update({"TRANSFORMERS_OFFLINE":"1"})
    llm_utils.start_llm()
    vector_store_utils.init_vector_store(knowledge_base_name=basic_knowledge.basic_knowledge_name,
                                         docs=[Document(page_content=text, metadata={}) for text in
                                               basic_knowledge.basic_knowledge])


if __name__ == "__main__":
    init()
    parser = argparse.ArgumentParser(prog='langchain-ChatGLM',
                                     description='About langchain-ChatGLM, local knowledge based ChatGLM with langchain'
                                                 ' ｜ 基于本地知识库的 ChatGLM 问答')
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=7861)
    parser.add_argument("--ssl_keyfile", type=str)
    parser.add_argument("--ssl_certfile", type=str)
    # 初始化消息
    args = parser.parse_args()
    args_dict = vars(args)
    run_api(host=args.host,
            port=args.port,
            ssl_keyfile=args.ssl_keyfile,
            ssl_certfile=args.ssl_certfile,
            )
