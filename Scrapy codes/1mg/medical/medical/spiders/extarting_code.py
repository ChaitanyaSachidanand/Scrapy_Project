# import scrapy


# class AuthorSpider(scrapy.Spider):
#     name = "medical"

#     start_urls = ["https://www.1mg.com/drugs/avastin-100mg-injection-135666"]

#     def parse(self, response):
#         author_page_links = response.css(".author + a")
#         yield from response.follow_all(author_page_links, self.parse_author)

#         pagination_links = response.css("li.next a")
#         yield from response.follow_all(pagination_links, self.parse)

#     def parse_author(self, response):
#         def extract_with_css(query):
#             return response.css(query).get(default="").strip()

#         yield {
#             "name": response.xpath("//*[@id="drug_header"]/div/div/div[2]/div/div[1]/h1/text()").get(),
#             "birthdate": extract_with_css(".author-born-date::text"),
#             "bio": extract_with_css(".author-description::text"),
#         }