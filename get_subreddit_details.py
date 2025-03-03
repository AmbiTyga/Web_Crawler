
import praw
import json
from dotenv import load_dotenv
import os, sys
from tqdm.auto import tqdm
# Load environment variables from .env file
load_dotenv()

# Provide your Reddit API credentials from environment variables
reddit = praw.Reddit(
    client_id=os.getenv('PRAWAPI_ID'),
    client_secret=os.getenv('PRAWAPI_SECRET'),
    password=os.getenv("PRAWPASSWORD"),
    user_agent=os.getenv("PRAWUSER_AGENT"),
    username=os.getenv("PRAWUSER_ID"),
)

# List of subreddits to fetch details for
with open("scarpy_reddit_communities.json", 'r') as f:
    subreddits = json.load(f)
subreddit_details = []
errors = []
count = 0
for subreddit_name in tqdm(subreddits[::-1]):
    name = subreddit_name['community_name'].replace('r/','')
    if count>100:
        print('Found more than 100 None details')
        print(*errors, sep='\n')
        break
    try:
        subreddit = reddit.subreddit(name)
        detail = subreddit.public_description or None
        subreddit_details.append({
            "subreddit": f"r/{name}",
            "detail": detail
        })
        count-=1
    except Exception as e:
        subreddit_details.append({
            "subreddit": f"r/{name}",
            "detail": None
        })
        errors.append(e)
        count+=1

# Save the output to a JSON file
with open('subreddit_details.json', 'w', encoding='utf-8') as f:
    json.dump(subreddit_details, f, indent=4)

print('Details fetched and saved to subreddit_details.json')

# To run the script, save it as fetch_subreddit_details.py and execute in terminal with:
# python3 get_subreddit_details.py