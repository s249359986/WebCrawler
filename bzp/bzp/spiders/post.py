import scrapy
from scrapy import Request
from bzp.items import BosszhipinItem
class DmozSpider(scrapy.Spider):
    name = "post"
    allowed_domains = ["zhipin.com"]
    start_urls = [
        "https://www.zhipin.com/job_detail/?query=&city=101010100&industry=&position=100123"        
    ]

    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield Request(url, headers=headers)

    def parse(self, response):
        torrent = BosszhipinItem()
        torrent['url'] = response.url
        torrent['title'] = response.xpath("//div[@id='wrap']").extract()        
        return torrent