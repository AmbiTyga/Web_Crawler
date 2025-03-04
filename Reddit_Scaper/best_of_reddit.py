import scrapy

class RedditCommunitiesSpider(scrapy.Spider):
    name = 'reddit_communities'
    allowed_domains = ['reddit.com']
    start_urls = [f'https://www.reddit.com/best/communities/{i}/' for i in range(1368, 0, -1)]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0',
        'ROBOTSTXT_OBEY': False,  # Bypass robots.txt restrictions
        'DOWNLOAD_DELAY': 1,  # Add a 5-second delay between requests
        'FEEDS': {
            'reddit_communities.json': {
                'format': 'json',
                'encoding': 'utf8',
                'indent': 4,
            }
        }
    }

    def parse(self, response):
        communities = response.css('div.community-list div.flex.flex-wrap.justify-center a.m-0.font-bold.text-12.text-current.truncate::text').getall()
        for community in communities:
            yield {'community_name': community.strip()}


# To run the script, save it as best_of_reddit.py and execute in terminal with:
# scrapy runspider best_of_reddit.py -o scrapy_reddit_communities.json -t json
