import scrapy


class BookdataSpider(scrapy.Spider):
    name = "bookData"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):

        booktittles = response.css("h3 > a::attr(title)").getall()
        for tittle in booktittles:
            print()
            print()
            print()
            print('tittle',tittle)
            print()
            print()
            print()

            yield{
                'tittle':tittle
            }
            
