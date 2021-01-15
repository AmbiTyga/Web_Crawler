import scrapy
COUNT = 1
class MySpider(scrapy.Spider):
  name = "samayam"

  def start_requests(self):
    
    url = "https://tamil.samayam.com/latest-news/fact-check/articlelist/66761758.cms?curpg=1"
    yield scrapy.Request(url=url, callback=self.parse)

  def parse_sites(self,response):

    title = response.css("div.news_card h1::text").get()
    content = response.css("div.story-article article.story-content::text").getall()
    content = "\n".join(content)

    yield {'title': title, 'content':content}

  def parse(self, response):
    global COUNT
    content_links = response.css('div.row.undefined span.con_wrap a::attr(href)').getall()
    for link in content_links:
      yield scrapy.Request(link, callback=self.parse_sites)
    COUNT+=1
    next_page_id = str(f'https://tamil.samayam.com/latest-news/fact-check/articlelist/66761758.cms?curpg={COUNT}')

    if "curpg=22" not in next_page_id:
        next_page = response.urljoin(next_page_id)
        yield scrapy.Request(next_page, callback=self.parse)