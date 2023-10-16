# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:04:34 2023

@author: msis
"""
import scrapy

from ..items import InternalsItem

class internal(scrapy.Spider):
    name='internals'
    # start_urls=[]
    # for i in range(1,10):
       # start_urls.append("https://www.flipkart.com/mens-footwear/sports-shoes/running-shoes~type/pr?sid=osp%2Ccil%2C1cu&otracker=nmenu_sub_Men_0_Running+Shoes&page="+str(i))
    start_urls = ['https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_b12dce52-ef92-4d1d-8df1-e73cec5a368c_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y',]
    
    def parse(self,response):
        
        #items = InternalsItem()
        # shoes_link = response.xpath("//div[@class='_1AtVbE col-12-12']/div[@class='_13oc-S']/div/div[@class='_1UoZlX']/a[@class='_31qSD5']").xpath("@href").getall()

        title = response.css('.IRpwTa::text').extract()
        yield{"title":title}
        """price = response.css('div._30jeq3::text').extract()
        size = response.css('div._376u-U::text').extract()
        company = response.css('div._2WkVRV::text').extract()
        
        items['title'] = title
        # items['deliviry_status'] = deliviry_status
        
        yield items"""
                
    


