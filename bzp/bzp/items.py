import scrapy

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    jobdes = scrapy.Field()
    salary = scrapy.Field()
    pass


    
#招聘信息item
class BosszhipinItem(scrapy.Item):
    Job = scrapy.Field()
    Salary = scrapy.Field()
    Company = scrapy.Field()
    City = scrapy.Field()
    Experience = scrapy.Field()
    Education = scrapy.Field()
    CompanySize = scrapy.Field()
    Financing = scrapy.Field()
    Industry = scrapy.Field()
    KeyWord = scrapy.Field()
    ContactPerson = scrapy.Field()
    Duties = scrapy.Field()
    Img = scrapy.Field()
    PubTime = scrapy.Field()
    Md5 = scrapy.Field()

    pass   


class lagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 职位id
    pid = scrapy.Field()
    # 职业名称
    positionName = scrapy.Field()
    # 求职发布者
    interviewer = scrapy.Field()
    # 工作年限
    workYear = scrapy.Field()
    # 工资
    salary = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 文凭要求
    education = scrapy.Field()
    # 公司名称
    companyShortName = scrapy.Field()
    # 工作领域
    industryField = scrapy.Field()
    # 上市情况
    financeStage = scrapy.Field()
    # 公司规模
    companySize = scrapy.Field()
    # 发布时间
    time = scrapy.Field()
    # 更新时间
    updated_at = scrapy.Field()
    # 职位详情
    detail = scrapy.Field()
    # 工作地点
    location = scrapy.Field()

    pass   