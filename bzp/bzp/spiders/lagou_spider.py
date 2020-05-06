import scrapy
from scrapy import Request
from bs4 import BeautifulSoup
from bzp.items import lagouItem
class DmozSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = [      
        "https://www.lagou.com/beijing-zhaopin/Java/?labelWords=label"       
    ]

    def start_requests(self):
        # headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
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
        for url in self.start_urls:
            yield Request(url, headers=headers)

    def parse(self, response):
        # job_list = response.css('div.job-list>ul>li')
        # response.encoding = 'UTF-8'
        soup = BeautifulSoup(response.body, 'html.parser')          
        job_list = soup.find_all("li", class_="con_list_item default_list") 
        #job_list = response.xpath("//li[@class='con_list_item default_list']").extract()             
        for job in job_list:
            #职位
            postionName = str(job.find("h3").get_text())
            #发布者
            interviewer = str(job.find("span",class_="money").get_text())
            print('_______',postionName)
            torrent = lagouItem()            
            torrent['positionName'] = postionName
            torrent['interviewer'] = interviewer
            # print(sites)
            # torrent['name'] = response.xpath("//div[@class='name']/h1/text()").extract()
            # torrent['salary'] = response.xpath("//div[@class='name']/span[@class='salary']/text()").extract()        
            yield torrent