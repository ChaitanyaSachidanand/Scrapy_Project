import scrapy

from ..items import ScrapyInternalItem


class InternalsSpider(scrapy.Spider):
    name='scrapy_internal'
    # start_urls=[]
    # for i in range(1,10):
       # start_urls.append("https://www.flipkart.com/mens-footwear/sports-shoes/running-shoes~type/pr?sid=osp%2Ccil%2C1cu&otracker=nmenu_sub_Men_0_Running+Shoes&page="+str(i))
    start_urls = ['https://www.flipkart.com/q/shoes']
    
    def parse(self,response):
        
        #items = InternalsItem()
        # shoes_link = response.xpath("//div[@class='_1AtVbE col-12-12']/div[@class='_13oc-S']/div/div[@class='_1UoZlX']/a[@class='_31qSD5']").xpath("@href").getall()

        title = response.css('._2WkVRV::text').extract()
        yield{"title":title}
        """price = response.css('div._30jeq3::text').extract()
        size = response.css('div._376u-U::text').extract()
        company = response.css('div._2WkVRV::text').extract()
        
        items['title'] = title
        # items['deliviry_status'] = deliviry_status
        
        yield items"""
                