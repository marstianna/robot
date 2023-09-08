import sys
import os

from llm import llm_utils

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import argparse
import uvicorn
from starlette.responses import RedirectResponse
from example.example_api import add_examples, delete_example, query_examples, list_examples, reload_examples
from chat.chat_api import chat
import config
from fastapi import FastAPI
from database import vector_store_utils
from knowledge_base import basic_knowledge
from langchain.schema import Document


async def document():
    return RedirectResponse(url="/docs")


def create_app():
    app = FastAPI(
        title="Global Robot Server",
        version=config.VERSION
    )
    # MakeFastAPIOffline(app)
    # Add CORS middleware to allow all origins
    # 在config.py中设置OPEN_DOMAIN=True，允许跨域
    # set OPEN_DOMAIN=True in config.py to allow cross-domain
    # if OPEN_CROSS_DOMAIN:
    # app.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=["*"],
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )

    # app.get("/",
    #         response_model=BaseResponse,
    #         summary="swagger 文档")(document)

    # Tag: ExampleManager
    app.get("/examples/reload",
            tags=["ExampleManager"],
            summary="重载examples")(reload_examples)
    app.get("/examples/query",
            tags=["ExampleManager"],
            summary="查询examples")(query_examples)
    app.get("/examples/add",
            tags=["ExampleManager"],
            summary="添加example")(add_examples)
    app.get("/examples/list",
            tags=["ExampleManager"],
            summary="获取所有examples")(list_examples)
    app.get("/examples/delete",
            tags=["ExampleManager"],
            summary="删除examples")(delete_example)
    app.get("/chat",
            tags=["Chat"],
            summary="对话")(chat)

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
    llm_utils.get_llm()
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
