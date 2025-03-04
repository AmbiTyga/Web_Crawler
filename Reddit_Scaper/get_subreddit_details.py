import json
import scrapy
import subprocess

class SubredditSpider(scrapy.Spider):
    name = 'subreddit_spider'
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0',
        'ROBOTSTXT_OBEY': False,
        # 'DOWNLOAD_DELAY': 10,  # Add a 10-second delay between requests
        'FEEDS': {
            'reddit_communities.json': {
                'format': 'json',
                'encoding': 'utf8',
                'indent': 4,
            }
        }
    }
    
    # Read subreddit names from a JSON file
    def start_requests(self):
        previously_parsed = json.load(open("subreddit_details.json"))
        already_parsed = [g.get('name') for g in previously_parsed]
        with open('scarpy_reddit_communities.json', 'r') as f:
            subreddits = json.load(f)
            for subreddit in subreddits[::-1]:
                subreddit_name = subreddit.get("community_name").replace('r/', '')
                if subreddit_name in already_parsed:
                    continue
                url = f'https://www.reddit.com/r/{subreddit_name}/'
                yield scrapy.Request(url, callback=self.parse, meta={'subreddit_name': subreddit_name}, errback=self.handle_failure)

    def parse(self, response):
        subreddit_name = response.meta['subreddit_name']
        header = response.css('shreddit-subreddit-header')

        yield {
            'name': header.css('::attr(name)').get(),
            'display-name': header.css('::attr(display-name)').get(),
            'description': header.css('::attr(description)').get(),
            'subscribers': header.css('::attr(subscribers)').get(),
        }

    def handle_failure(self, failure):
        if failure.value.response.status == 429:  # If rate-limited
            print("Received 429 Too Many Requests. Running Bash script to restart.")
            self.crawler.engine.close_spider(self, 'Rate limit hit')

    
# Save this file as get_subreddit_details.py and run with the following command:
# scrapy runspider get_subreddit_details.py -o output.json

# Ensure the input JSON file (subreddits.json) is in the same directory, with content like:
# [
#   {"community_name": "r/ArtPorn"},
#   {"community_name": "r/Pics"}
# ]
