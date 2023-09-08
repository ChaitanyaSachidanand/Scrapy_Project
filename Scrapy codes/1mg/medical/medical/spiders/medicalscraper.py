import scrapy


class MedicalscraperSpider(scrapy.Spider):
    name = "medical"
    allowed_domains = ["www.1mg.com"]
    start_urls = ["https://www.1mg.com/drugs-all-medicines"]

    def parse(self, response):
        
        pass
