import json
from scrapy.crawler import CrawlerProcess
from spiders.data import DataSpider

from db_settings.models import Tag, Author, Quote
from db_settings.connect import connect

def feed_db():
    with open('result.json', 'r') as f:
        data = json.load(f)
        for el in data:
            authot_to_db = Author(name=el.get('author')[0]).save()
            tags_to_db = Tag(tag=el.get('tag')).save()
            quote_to_db = Quote(quote=el.get('quote'), tags=tags_to_db, author=authot_to_db).save()

def make_json_file():

    authors = []
    quotes = []
    with open('result.json', 'r') as f:
        data = json.load(f)
    for el in data:
        authors.append(el.get('author'))
        quotes.append(el.get('quote'))

    with open('authors.json', 'w') as file:
        json.dump(authors, file)
    with open('quotes.json', 'w') as file:
        json.dump(quotes, file)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(DataSpider)
    process.start()
    make_json_file()
    feed_db()