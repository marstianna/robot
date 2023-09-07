prompt_examples = [
    {
        "role": "你现在是一个答疑机器人，需要根据用户的输入，输出推荐的配置信息。",
        "input": "我需要跨单元注册到lazada云下",
        "output": """
                    global.landlord.protocol.mode.<modeName>=lazada_sg
                    global.landlord.hsf.consumer.custom[0].modes=@<modeName>
                    global.landlord.hsf.consumer.custom[0].list=<interfaces>
                    """
    },
    {
        "role": "你现在是一个答疑机器人，需要根据用户的输入，输出推荐的配置信息。",
        "input": "我当前应用部署lazada在rg_sg机房，我需要跨单元注册到lazada老机房",
        "output": """
                    global.landlord.hsf.consumer.custom[0].modes=SOURCE_RAW
                    global.landlord.hsf.consumer.custom[0].list={interfaces}
                    """
    },
    {
        "role": "你现在是一个答疑机器人，需要根据用户的输入，输出推荐的配置信息。",
        "input": "获取LAZADA_ID的ScheduleX2的配置",
        "output": """
                    LAZADA_ID.global.landlord.schedulerx2.groupId={your_group}
                    LAZADA_ID.global.landlord.schedulerx2.appKey={your_app_key}
                    global.landlord.schedulerx2.domainName=schedulerx-lazada-sg-landlord.alibaba-inc.com
                    """
    },
    {
        "role": "你现在是一个答疑机器人，需要根据用户的输入，输出推荐的配置信息。",
        "input": "接入多租户框架之后，启动时报tddl的datetime错误。",
        "output": """
                    解决方案为在satellite.properties添加
                    global.landlord.mybatis.type.enabled=false
                    """
    }
]
