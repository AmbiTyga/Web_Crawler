# Reddit Scrape:
- Scrape Best of Reddit communities

## Step 1:
- Configure python and install `scrapy`
- Fetch all Subreddits: 
```
scrapy runspider best_of_reddit.py -o scrapy_reddit_communities.json -t json
```

## Step 2:
- Fetch Details about these communities:
```
bash restart_reddit_spider.sh
```

## Note:
- It took me 25 mintues to fetch 3,44,105 names of subreddit on 150Mbps
- It took me 36 hours to fetch their details on same speed.