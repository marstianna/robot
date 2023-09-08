from langchain import PromptTemplate, LLMChain

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
    print("input string : " + query)
    context,examples = example_service.search_examples(query)
    if examples is None:
        return

    for example in examples:
        template = PromptTemplate(input_variables=["role", "basic_knowledge", "input", "output", "query","action"],
                                  template="{role}\n{basic_knowledge}\n{action}\ninput: {input}\noutput: "
                                           "{output}\ninput: {query}\noutput: ").partial(
            **example)

        print("template info :" + template.format(query=query))
        call = llm_utils.call(prompt=template.format(query=query), top_k=2)
        print(call)

    # return examples


async def add_examples():
    print("add_examples")
    return
