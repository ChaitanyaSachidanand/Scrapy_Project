import scrapy


class QuotsScraperSpider(scrapy.Spider):
    name = "quots_scraper"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        pass
