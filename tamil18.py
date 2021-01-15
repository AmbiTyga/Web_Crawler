import scrapy
class MySpider(scrapy.Spider):
  name = "tamil18"
  header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
  def start_requests(self):
    
    url = "https://tamil.news18.com/news/"
    yield scrapy.Request(url=url, callback=self.parse,headers = header)

  def parse_sites(self,response):

    title = response.css('div#article h1::text').get()
    content = response.css('div.storypara strong::text').getall() + response.css('div.storypara::text').getall()
    content = list(filter(('').__ne__,[i.strip() for i in content]))
    
    content = "\n".join(content)

    yield {'title': title, 'content':content}

  def parse(self, response):
    content_links = response.css('div.blog-list-blog p a::attr(href)').getall()
    content_links = ['https://tamil.news18.com'+i for i in content_links]
    for link in content_links:
      yield scrapy.Request(link, callback=self.parse_sites,headers = header)
    next_page_id = 'https://tamil.news18.com' + response.css('div.pagination li.next a::attr(href)').get()

    if "page-150" not in next_page_id:
        next_page = response.urljoin(next_page_id)
        yield scrapy.Request(next_page, callback=self.parse,headers = header)