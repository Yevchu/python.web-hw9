import json
from scrapy.crawler import CrawlerProcess
from spiders.data import DataSpider

from db_settings.models import Tag, Author, Quote
from db_settings.connect import connect

authors_list = []
quotes_list = []
tags_list = []

def parse_res():
    with open('result.json', 'r') as f:
        data = json.load(f)
        for el in data:
            authors_list.append(el.get('author')[0])
            quotes_list.append(el.get('quote'))
            tags_list.append(el.get('tag'))

def make_json_file(author, quote):
    with open('authors.json', 'w') as file:
        json.dump(author, file)
    with open('quotes.json', 'w') as file:
        json.dump(quote, file)

def feed_db():

    for author in authors_list:
        authot_to_db = Author(name=author).save()

    for tags in tags_list:
        tags_to_db = Tag(tag=tags).save()

    for quote in quotes_list:
        quote_to_db = Quote(quote=quote).save()


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(DataSpider)
    process.start()
    parse_res()
    make_json_file(authors_list, quotes_list)
    feed_db()