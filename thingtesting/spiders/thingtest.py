import scrapy


class ThingTest(scrapy.Spider):
    name = "thingtest"
    start_urls = [
        "https://thingtesting.com/?o=a-z",
    ]

    def parse(self, response):
        product_names = response.css("h2.sc-1i7hkfu-1")
        descr = response.css("p.sc-1i7hkfu-0")
        index = 0
        for product in product_names:
            yield {
                "product": product.css("a::text").get(),
                "description": descr[index].css("p::text").get(),
            }
            index += 1
