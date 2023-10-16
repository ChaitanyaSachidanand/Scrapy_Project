import scrapy
from ..items import FlipkartShoeItem

class ShoeScrapeSpider(scrapy.Spider):
    name = "shoe_scrape"
    # no_of_pages = 4
  
    allowed_domains = ["flipkart.com"]
    start_urls = ["https://www.flipkart.com/aadi-mesh-lightweight-comfort-summer-trendy-walking-outdoor-daily-use-running-shoes-men/p/itm5fd3ef71721ed?pid=SHOFZDBPKJVXB6BQ&marketplace=FLIPKART"]

    # def start_requests(self):
    #     urls = [
    #     "https://www.flipkart.com/mens-footwear/sports-shoes/running-shoes~type/pr?sid=osp%2Ccil%2C1cu&otracker=nmenu_sub_Men_0_Running+Shoes&page=1"
    #     ]

        # for url in urls:
        #     yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
    #     self.no_of_pages -= 1
    # # self.page_no += 1

    #     shoes = response.xpath("//div[@class='_1AtVbE col-12-12']/div[@class='_13oc-S']/div/div[@class='_1UoZlX']/a[@class='_31qSD5']").xpath("@href").getall()

    #     for shoes in shoes:
    #         shoesUrl = response.urljoin(shoes)
    #         yield scrapy.Request(url = shoesUrl, callback = self.parse_shoes)
    
    #     if(self.no_of_pages > 0):
    #         next_page_all_href = response.xpath("//div[@class='_2MImiq']/nav[@class='yFHi8N']/a[@class='_1LKTO3']").xpath("@href").getall()
    #         next_page_href = next_page_all_href[len(next_page_all_href) - 1]
    #         next_page_url = response.urljoin(next_page_href)
    #         yield scrapy.Request(url = next_page_url, callback = self.parse)

# def parse_shoes(self, response):
        shoesUrl = response.request.url
        shoesName = response.xpath("//span[@class='B_NuCI']//text()").get()
        
        shoesPrice = response.xpath("//div[@class='_30jeq3 _16Jk6d']//text()").get()
        shoesRating = response.xpath("//div[@class='_3LWZlK _3uSWvT']//text()").getall()
        
        # shoesRating = response.xpath("//div[@class='col-12-12 _11EBw0']/div[@class='_1i0wk8']//text()").get()
        
        # shoesImageUrl = response.xpath("//div[@class='_3BTv9X _3iN4zu']/img/@src").get()
        
        # yield FlipkartShoeItem("url" = shoesUrl,"name" = shoesName, "price" = shoesPrice, "rating" = shoesRating)
        yield {"shoesUrl":shoesUrl,
        "shoesName":shoesName,
        "shoesPrice":shoesPrice ,
        "shoesRating":shoesRating}