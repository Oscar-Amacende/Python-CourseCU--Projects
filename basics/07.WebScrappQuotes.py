# pip install scrapy --break-system-packages. --break-system-packages.
# este codigo no devuelve por si solo se imprime con scrapy runspider scrapper1.py
import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/tag/humor',]
    def parse(self,response):
        for quote in response.css('div.quote'):
            yield {'quote': quote.css('span.text::text').get()}
