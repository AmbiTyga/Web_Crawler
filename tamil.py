import scrapy
from w3lib.html import remove_tags

class MySpider(scrapy.Spider):
  name = "tamil"

  def start_requests(self):
    
    url = "https://tamil.oneindia.com/topic/fake"
    yield scrapy.Request(url=url, callback=self.parse)

  def parse_sites(self,response):
    container = response.css("div.oi-article-lt")

    title = response.css('div.oi-article-lt h1::text').get()
    content = response.css("div.oi-article-lt p::text").getall()
    content = "\n".join(content)

    yield {'title': title, 'content':content}

  def parse(self, response):
    content_links = response.css('li.clearfix div.cityblock-desc a::attr(href)').getall()
    content_links = ["https://tamil.oneindia.com"+i for i in content_links]
    for link in content_links:
      yield scrapy.Request(link, callback=self.parse_sites)
    next_page_id = "https://tamil.oneindia.com" + response.css('div.oi-city-prevnext.clearfix .oi-city-next::attr(href)').get()

    if "page-no=100" not in next_page_id[3:]:
        next_page = response.urljoin(next_page_id)
        yield scrapy.Request(next_page, callback=self.parse)