from api import data_cleaning_api
from database.text_splitter.ali_text_splitter import AliTextSplitter


async def test_split() -> list[str]:
    text = """【发布回滚】无责任发布回滚申诉
一、背景
“发布回滚率”指标对琅琊榜（研发效能指数和技术风险分）影响较大，原则上发布回滚归属的应用负责人和责任团队应该关心所有发布回滚的情况，有责任尽可能避免线上回滚，所有的问题尽可能在灰度甚至更早的阶段发现。但是由于部分特殊原因（比如特殊封网影响、基础设施瘫痪等），经过和指标Owner阿贵讨论，业务团队可对回滚的原因申请“无责任回滚”，由业务域对应的SRE团队的TL审核，以减少异常场景对团队结果评估的影响。
此外，技术风险小组会季度整体审计一次，避免错误申报的情况。
申诉范围限于以下情况：
无责任应急回滚：非本应用代码或本应用依赖的二方包、三方包或者中间件问题，如为其它应用发布后问题引发的本应用回滚；
同一系统多部署单元：对于多部署单元的回滚，可以支持合并为一次回滚；（若1个application、1个代码仓的x个应用，在1个发布单中发布产生回滚，则只记录1次回滚，另外x-1次记录为无责任回滚，不会影响团队的应用发布回滚率评价。此项规则从2020年4月1日后生效。）
二、申诉流程
Step1：填写发布回滚无责任申请表。
发布ID
应用名称
申请人
SRE TL
无责任原因
花名+工号
花名+工号
xxxxx
Step2：在产品用户通道提交（链接）
样例：https://aone.alipay.com/issue/23929293?spm=a2o8d.corp_prod_issue_list.0.0.3f8c658f49Km9x&stat=1.5.0&toPage=1&versionId=1792916
image.png
主要是3个关键信息填对。
指派给“薛丁文(錵鈥)”
Step3：联系SRE TL在下面评论“评审OK”
Step4：产品会自动在x个工作日处理，处理后变化如下
1、回滚数量不变，但是在点击明细中会增加字段标记”无责任回滚“。
2、”发布回滚率“指标计算时不会计算“”无责任发布回滚“。"""

    splitter = AliTextSplitter()
    return splitter.split_text(text)
