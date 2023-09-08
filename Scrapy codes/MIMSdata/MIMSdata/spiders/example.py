import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class MySpider(scrapy.Spider):
    name = 'MIMSdata'
    start_urls = ['https://www.mims.com/account/login?']  # URL of the login page

    def parse(self, response):
        return FormRequest.from_response(
            response,
            formdata={
                'Input.Email': 'chaithanyasachidanand@gmail.com',
                'Input.Password': 'Q1234567890p',
            },
            callback=self.after_login
        )

    def after_login(self, response):
        # Check if login was successful
        if 'Welcome' in response.text:
            self.logger.info('Login successful')
            # Now, you can navigate to the pages you want to scrape
            yield scrapy.Request(url='https://www.mims.com/india/drug/', callback=self.parse_data)
        else:
            self.logger.error('Login failed')

    def parse_data(self, response):
        # Parse the data from the page as needed
        # Example: Extract data from a table
        data = response.css('table tr td::text').getall()
        yield {
            'data': data
        }
