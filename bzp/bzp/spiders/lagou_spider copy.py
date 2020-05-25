import scrapy
import time
from scrapy import Request
from bs4 import BeautifulSoup
from bzp.items import lagouItem
class DmozSpider(scrapy.Spider):
    name = "lagou11"
    allowed_domains = ["lagou.com"]
    page_num = 1
    # 岗位类别
    gwType = "前端开发"
    cityType = "北京"
    cityTypePinYin = "beijing"
    next_url_pre = "https://www.lagou.com/"+cityTypePinYin+"-zhaopin/"+gwType+"/"
    next_url_end = "/?filterOption=3&sid=40c0ba4953bb4fd28a006b0b7bfe3066"
    start_urls = [ 
         "https://www.lagou.com/"+cityTypePinYin+"-zhaopin/"+gwType+"/1/?filterOption=3&sid=40c0ba4953bb4fd28a006b0b7bfe3066"
        #  "https://www.lagou.com/beijing-zhaopin/Java/?labelWords=label"       
    ]
    headers = {
        'x-devtools-emulate-network-conditions-client-id': "5f2fc4da-c727-43c0-aad4-37fce8e3ff39",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'dnt': "1",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
        'cookie': "__c=1501326829; lastCity=101020100; __g=-; __l=r=https%3A%2F%2Fwww.google.com.hk%2F&l=%2F; __a=38940428.1501326829..1501326829.20.1.20.20; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1501326839; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1502948718; __c=1501326829; lastCity=101020100; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1501326839; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1502954829; __l=r=https%3A%2F%2Fwww.google.com.hk%2F&l=%2F; __a=38940428.1501326829..1501326829.21.1.21.21",
        'cache-control': "no-cache",
        'postman-token': "76554687-c4df-0c17-7cc0-5bf3845c9831"
    }

    def start_requests(self):
        # headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
      
        for url in self.start_urls:
            yield Request(url, headers = self.headers)

    def parse(self, response):
        # job_list = response.css('div.job-list>ul>li')
        # response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.body, 'html.parser')          
        job_list = soup.find_all("li", class_="con_list_item default_list")                  
        page_list = soup.find("div", class_="pager_container").find_all("a", class_="page_no")                          
        page_counts = page_list[len(page_list)-2].get_text()
        print("page_num-----------------",page_counts)
        print("page_list-----------------",len(page_list))
        for job in job_list:
            #职位
            postionName = str(job.find("h3").get_text())
            #发布者
            #interviewer = str(job.find("div",class_="company_name").find("a").get_text())
            #工作年限
            workYear = str(job.find("div",class_="li_b_l").get_text())
            #工资
            salary = str(job.find("span",class_="money").get_text())
            #文凭
            education = str(job.find("div",class_="li_b_l").get_text())
            #公司
            companyShortName = str(job.find("div",class_="company_name").find("a").get_text())
            #公司规模公司领域  industry
            industryField = str(job.find("div",class_="industry").get_text())
                        
            print('_______',postionName)
            torrent = lagouItem()            
            torrent['positionName'] = postionName            
            torrent['workYear'] = workYear
            torrent['salary'] = salary
            torrent['education'] = education
            torrent['companyShortName'] = companyShortName
            torrent['industryField'] = industryField
            torrent['city'] = self.cityType           
                                                   
            yield torrent

        if self.page_num > int(page_counts):
            self.crawler.engine.close_spider(self, 'done!' % response.body)
        # 翻页
        self.page_num += 1
        time.sleep(2)
        yield self.next_request(self.page_num)
    def next_request(self, pageNum):
        tempUrl = self.next_url_pre+str(pageNum)+self.next_url_end
        print('next_request------',tempUrl)
        return scrapy.http.Request(tempUrl,headers=self.headers,callback=self.parse,dont_filter = True)