from langchain import PromptTemplate

from example import example_service
from llm import llm_utils


async def reload_examples():
    print("reload_examples")
    return


async def list_examples():
    print("list_examples")
    return


async def delete_example():
    print("delete_example")
    return


async def query_examples(query: str):
    examples = example_service.search_examples(query)
    for example in examples:
        template = PromptTemplate(input_variables=["role", "basic_knowledge", "input", "output", "query"],
                                  template="{role}\n{basic_knowledge}\ninput: {input}\noutput: "
                                           "{output}\ninput: {query}\noutput: ").partial(
            **example)
        print("template info :"+template.format(query=query))
        call = llm_utils.call(prompt=template.format(query=query), top_k=2)
        print(call)


async def add_examples():
    print("add_examples")
    return
