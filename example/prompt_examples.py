prompt_examples = [
    {
        "role": "你现在是一个答疑机器人，需要根据用户的输入，输出推荐的配置信息。",
        "input": "我需要跨单元注册到lazada云下",
        "output": """\"\"\"
                    global.landlord.protocol.mode.<modeName>=lazada_sg
                    global.landlord.hsf.consumer.custom[0].modes=@<modeName>
                    global.landlord.hsf.consumer.custom[0].list=<interfaces>
                    \"\"\"
                    """
    },
    {
        "role": "你现在是一个答疑机器人，需要根据用户的输入，输出推荐的配置信息。",
        "input": "获取LAZADA_ID的ScheduleX2的配置",
        "output": """
            \"\"\"
            LAZADA_ID.global.landlord.schedulerx2.groupId={your_group}
            LAZADA_ID.global.landlord.schedulerx2.appKey={your_app_key}
            global.landlord.schedulerx2.domainName=schedulerx-lazada-sg-landlord.alibaba-inc.com
            \"\"\"
            """
    },
]
