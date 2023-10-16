# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class InternalsPipeline:
    
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect('exam.db')
        self.curr = self.conn.cursor()
        
    def create_table(self):
        self.curr.execute('''DROP TABLE IF EXISTS desktops_tb''')
        self.curr.execute('''create table desktops_tb(
            title text)''')
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    
    def store_db(self,item):
        self.curr.execute(''' insert into desktops_tb values(?)''',
                          (
                              item['title']
                            #   item['deliviry_status'][0]
                            ))
        self.conn.commit()