import scrapy


class ShoeScraperSpider(scrapy.Spider):
    name = "shoe_scraper"
    allowed_domains = ["flipkart.com"]
    start_urls = ["https://www.flipkart.com/mens-footwear/sports-shoes/running-shoes~type/pr?sid=osp%2Ccil%2C1cu&otracker=nmenu_sub_Men_0_Running+Shoes&page=1"]

    for url in urls:
      yield scrapy.Request(url = url, callback = self.parse, headers = self.headers)

def parse(self, response):
    self.no_of_pages -= 1

    def parse(self, response):
        pass
