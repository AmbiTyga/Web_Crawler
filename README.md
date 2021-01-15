# Web_Crawler
This repo contains crawlers I used in my projects or research. This repo will be updated with new methods and techniques loaded in scripts. Most of the work will be done using [Scrapy](https://scrapy.org/). I haven't started using beautifulsoup up till now but will update the code if I required that library.

This repo currently contains 2 spiders:
- [cb_spider.py](/cb_spider.py): This spider crawls on [Amazon.com-smartphone](https://www.amazon.com/s?k=SMARTPHONE&ref=nb_sb_noss_2) to fetch product description, price(in $) and ratings(out of 5). The output is stored in an JSON file. This is the [output](/amazon_cb_output.json).
- [corona.py](/corona.py): This spider crawls on [Poynter-IFCN Covid-19 Misinformation](https://www.poynter.org/ifcn-covid-19-misinformation/?covid_countries=0&covid_rating=0&covid_fact_checkers=0#038;covid_rating=0&covid_fact_checkers=0) to fetch fake data. The output is stored in an CSV file. This is the [output](/poynter_mis_info_covid.csv) 
- [snope.py](/snope.py): This spider crawls on [Snope's fact checker page](https://www.snopes.com/fact-check/) and retrieves news and related contents(question, comments, claim and origin)along with their labels whether it's true, false or unknown.
- [samayam.py](/samayam.py): This spider crawls on [Samayam's fact check news](https://tamil.samayam.com/latest-news/fact-check/articlelist/66761758.cms?curpg=1), to fetch news data in tamil language.
-[tamil.py](/tamil.py)/[tamil18.py](/tamil18.py): These spiders is similar to [samayam.py](/samayam.py) and scrapes data from [Tamil OneIndia](https://tamil.oneindia.com/topic/fake) and [Tamil News18](https://tamil.news18.com/news/) respectively.
