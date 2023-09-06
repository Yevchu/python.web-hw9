import scrapy


class DataSpider(scrapy.Spider):
    name = "data"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "result.json"}


    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            yield {
                "tag": quote.xpath("div[@class='tags']/a/text()").extract(),
                "author": quote.xpath("span/small/text()").extract(),
                "quote": quote.xpath("span[@class='text']/text()").get()
            }
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)