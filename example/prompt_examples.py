prompt_template = "{role}\n{basic_knowledge}\n{action}\ninput: {input}\noutput: {output}\ninput: {query}\noutput: "

prompt_examples = [
    {
        "role": "你现在是一个答疑机器人，需要根据用户的输入，输出推荐的配置信息。",
        "action": "根据用户输入修改对应配置的单元标",
        "input": "我需要跨单元注册到Lazada新加坡云下单元",
        "output": """\"\"\"
                    global.landlord.protocol.mode.<modeName>=lazada_sg_2
                    global.landlord.hsf.consumer.custom[0].modes=@<modeName>
                    global.landlord.hsf.consumer.custom[0].list=<interfaces>
                    \"\"\"
                    """
    },
    {
        "role": "你现在是一个答疑机器人，需要根据用户的输入，输出推荐的配置信息。",
        "action": "根据用户输入修改对应配置的单元标和domainName",
        "input": "获取LAZADA_ID的ScheduleX2的配置",
        "output": """
            \"\"\"
            LAZADA_ID.global.landlord.schedulerx2.groupId={your_group}
            LAZADA_ID.global.landlord.schedulerx2.appKey={your_app_key}
            global.landlord.schedulerx2.domainName=id.schedule2.alibaba-inc.com
            \"\"\"
            """
    },
]
