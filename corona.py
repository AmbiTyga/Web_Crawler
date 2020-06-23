import scrapy


class MySpider(scrapy.Spider):
    name = "corona"

    def start_requests(self):
        urls = [
            "https://www.poynter.org/ifcn-covid-19-misinformation/?covid_countries=0&covid_rating=0&covid_fact_checkers=0#038;covid_rating=0&covid_fact_checkers=0",
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        containers = response.css("div.articles.covid-articles div.post-wrapper.container div.post-container header.entry-header")
        for container in containers:
            label = container.css("span::text").get()
            text = container.css('h2 a::text').get()
            yield {'label': label, 'text':text}
        next_page_id = response.css("a.next.page-numbers::attr(href)").get()

        if next_page_id[58] is not '493':
            next_page = response.urljoin(next_page_id)
            yield scrapy.Request(next_page, callback=self.parse)