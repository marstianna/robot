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

async def test_examples():
    input = "请从下文中提取对应的功能介绍和对应的实例代码：\n{0}"

    replace = """一、代码改造
        无必须性的代码改造，多租户会修改spring注入的hsf bean的类。
        不过，为了优化，建议对以下类做替换：
        
        HSFSpringConsumerBean -- 替换类 --> SatelliteHSFSpringConsumerBean
        HSFApiConsumerBean -- 替换类 --> SatelliteHSFApiConsumerBean
        
        HSFSpringProviderBean -- 替换类 --> SatelliteHSFSpringProviderBean
        HSFApiProviderBean -- 替换类 --> SatelliteHSFApiProviderBean
        
        ServiceFactory -- 替换类 --> SatelliteServiceFactory
        
        *** 服务模式说明 ***
        支持通过配置，为hsf增加一些扩展功能
        详见文档：https://yuque.antfin-inc.com/satellite/sa/mp6wof
        
        二、特性说明（非改造项）：hsf本地调用被多租户代理
        在java启动时，增加的配置：-Dhsf.client.localcall=true，会失效，hsf的本地调用将由多租户提供。
        在启动过程中，会有日志提示：
        [Satellite HSF] Reset hsf.client.localcall: false -> true! You can modify it in satelllite.properties!
        
        配置方式，在resources目录下，新增配置文件satellite.properties
        # hsf配置开关配置, 默认为true
        hsf.client.localcall=true
        
        # 2.0.7-SNAPSHOT版本，支持服务级别的配置
        # 服务级别的配置, 走本地调用的hsf接口列表，逗号分隔，需要带版本号
        hsf.client.localcall.uniqueNames=com.alibaba.global.TestLocalFacade:1.0.0
        
        # 服务级别的配置, 不走本地调用的hsf接口，逗号分隔，需要带版本号
        hsf.client.remotecall.uniqueNames=com.alibaba.global.TestRemoteFacade:1.0.0
        
        satellite.properties对应的远程diamond为
        dataId：应用名:satellite.properties
        groupId：DEFAULT
        
    
    """

    print(llm_utils.call(prompt=input.format(replace), top_k=2))
    # return examples


async def add_examples():
    print("add_examples")
    return
