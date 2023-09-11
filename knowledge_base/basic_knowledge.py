basic_knowledge_name = "multi_tenant_basic_knowledge"

basic_knowledge = [
    "LAZADA主要运营的国家为东南亚6个国家，分别为：新加坡,马来西亚,越南,菲律宾,泰国,印度尼西亚",
    "新加坡的国家代号为SG，线上环境部署在新加坡云上机房和新加坡云下机房",
    "马来西亚的国家代号为MY，线上环境部署在新加坡云上机房和新加坡云下机房",
    "越南的国家代号为VN，线上环境部署在新加坡云上机房和新加坡云下机房",
    "菲律宾的国家代号为PH，线上环境部署在新加坡云上机房和新加坡云下机房",
    "泰国的国家代号为TH，线上环境部署在新加坡云上机房和新加坡云下机房",
    "印度尼西亚的国家代号为ID，简称为印尼，线上环境部署在印尼云上机房和印尼云下机房",
    "新加坡的租户标为LAZADA_SG",
    "马来西亚的租户标为LAZADA_MY",
    "越南的租户标为LAZADA_VN",
    "菲律宾的租户标为LAZADA_PH",
    "泰国的租户标为LAZADA_TH",
    "印尼的租户标为LAZADA_ID",
    "LAZADA新加坡云上机房的代号为os30",
    "LAZADA新加坡云上机房的单元标为rg_sg",
    "LAZADA新加坡云下机房的代号为sg52",
    "LAZADA新加坡云下机房的单元标为lazada_sg_2",
    "LAZADA印尼云上机房的代号为id137",
    "LAZADA印尼云上机房的单元标为rg_id",
    "LAZADA印尼云下机房的代号为id35",
    "LAZADA印尼云下机房的单元标为lazada_id",
    "多租户针对TDDL做了改造，如果您的应用使用了数据库datetime字段类型，那么在您的应用中请添加global.landlord.mybatis.type.enabled=false",
    "ScheduleX2的国际化新加坡机房的domainName为sg.schedule2.alibaba-inc.com",
    "ScheduleX2的印尼机房的domainName为id.schedule2.alibaba-inc.com",
    "本地的satellite.properties对应的diamond配置项为：\ndataId:{应用名}:satellite.properties\ngroupId:DEFAULT",
    "程序运行期间，可以通过com.alibaba.global.landlord.LandlordContext获取到对应的租户上下文信息。",
    "LandlordContext.getCurrentTenantId()可以获取当前租户ID",
    "LandlordContext.getCurrentSiteId()可以获取当前站点ID",
    "LandlordContext.getCurrentOeId()可以获取当前运营实体ID",
    "程序运行期间，可以通过com.alibaba.global.g11n.G11nContext获取到对应的国际化相关信息。",
    "G11nContext.getCurrentRegion()可以获取到当前区域",
    "G11nContext.getCurrentRegion()可以获取到当前国家",
    "G11nContext.getCurrentLocale()可以获取到对应国家的Locale实例",
    "G11nContext.getCurrentCurrencyCode()可以获取到当前国家的货币类型",
    "G11nContext.getCurrentCurrencyCode()可以获取到当前国家的币种",
    "可以通过枚举类com.alibaba.global.landlord.model.ProtocolMode指定对应的通信协议模式，实现通信协议的增强（不侵入业务代码），达到接口按租户裂变，hsf跨单注册，hsf跨单元调用，metaq跨单元消费，metaq跨单元投递等能力。",
    "ProtocolMode.RAW表示原始模式，当模式设置没有配置时，自动生效的默认值",
    "ProtocolMode.MULTI表示当前HSF接口按照租户裂变版本号",
    "ProtocolMode.MULTI表示当前METAQ按照租户裂变对应的topic和cid",
    "ProtocolMode.SOURCE_RAW表示跨单元调用老单元的HSF服务，或者跨单元消费老单元的METAQ消息",
    "ProtocolMode.TARGET_RAW表示从老单元调用目标单元的HSF接口，订阅目标单元的METAQ消息，或者将METAQ消息投递到目标单元",
    "ProtocolMode.WRAPPER_RAW表示在本单元注册一个版本号为1.0.0_GL的HSF服务",
    "ProtocolMode.WRAPPER_SOURCE_RAW表示将HSF服务注册到老单元，并在版本号后面追加_GL"
]