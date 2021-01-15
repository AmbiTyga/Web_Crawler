import scrapy
from w3lib.html import remove_tags

class MySpider(scrapy.Spider):
  name = "snope"

  def start_requests(self):
    
    url = "https://www.snopes.com/fact-check/"
    yield scrapy.Request(url=url, callback=self.parse)

  def parse_sites(self,response):
    container = response.css("div.base-default main.base-main")
    try:
      true = container.css(".whats-true p::text").get()
    except:
      true = None
    try:
      fal = container.css(".whats-false p::text").get()
    except:
      fal = None
    try:
      unk = container.css(".whats-undetermined p::text").get()
    except:
      unk = None
    question = container.css(".title::text").get()
    comment = container.css(".subtitle::text").get()
    claim = container.css(".claim p::text").get()
    rate = container.css(".rating-wrapper.card .media-body h5::text").get()
    origin = response.css("div.content p").getall()
    origin = [remove_tags(x).strip() for x in origin]
    origin = "\n".join(origin)

    yield {'question': question, 'comment':comment, 'claim':claim,'rate':rate,"what's true":true,"what's false":fal,
        "what's unknown":unk,"origin":origin}
  def parse(self, response):
    content_links = response.css("article.media-wrapper a::attr(href)").getall()
    for link in content_links:
      yield scrapy.Request(link, callback=self.parse_sites)
    next_page_id = response.css("main.base-main a.btn-prev.btn::attr(href)").get()

    if "/1/" not in next_page_id[38:]:
        next_page = response.urljoin(next_page_id)
        yield scrapy.Request(next_page, callback=self.parse)