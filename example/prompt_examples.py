prompt_examples = [
    {
        "role": "你现在是一个答疑机器人，需要根据用户的输入，输出推荐的配置信息。",
        "input": "我需要跨单元注册到lazada云下",
        "output": """
                    global.landlord.protocol.mode.<modeName>=lazada_sg
                    global.landlord.hsf.consumer.custom[0].modes=@<modeName>
                    global.landlord.hsf.consumer.custom[0].list=<interfaces>
                    """
    }
]
