from example import example_service


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
    examples = example_service.search_examples("测试数据")
    print(examples)
    return


async def add_examples():
    print("add_examples")
    return
