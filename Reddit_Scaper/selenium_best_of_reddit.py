from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

# Configure Chrome WebDriver with headless mode
options = Options()
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

community_names = []

# Iterate through the pages
for i in range(1, 1369):
    url = f'https://www.reddit.com/best/communities/{i}/'
    driver.get(url)
    time.sleep(5)  # Wait for 5 seconds to allow the page to load completely

    # Extract community names using Selenium
    communities = driver.find_elements(By.CSS_SELECTOR, 'div.community-list div.flex.flex-wrap.justify-center a.m-0.font-bold.text-12.text-current.truncate')
    for community in communities:
        community_name = community.text.strip()
        community_names.append(community_name)

# Save the results to a JSON file
with open('reddit_communities.json', 'w', encoding='utf-8') as f:
    json.dump(community_names, f, indent=4)

# Quit the WebDriver
driver.quit()

print('Scraping completed. Data saved to reddit_communities.json.')

# To run the script, save it as selenium_best_of_reddit.py and execute in terminal with:
# python3 selenium_best_of_reddit.py
