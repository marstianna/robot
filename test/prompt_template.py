from langchain import PromptTemplate

import example.prompt_examples
import knowledge_base.basic_knowledge


def test_example():
    example_ = example.prompt_examples.prompt_examples[0]
    knowledge_ = knowledge_base.basic_knowledge.basic_knowledge[0]
    example_.update({"basic_knowledge":knowledge_})
    template = PromptTemplate(input_variables=["role","basic_knowledge","input" ,"output","query"],
                              template="role: {role}\nbasic_knowledge: {basic_knowledge}\ninput: {input}\noutput: {output}\ninput: {query}\noutput: ").partial(**example_)

    print(template.format(query="我需要跨单元注册到lazada云上"))

if __name__ == "__main__":
    test_example()
