# #!/bin/bash
while true; do
    echo "Starting the spider..."
    scrapy runspider get_subreddit_details.py -o subreddit_details.json
    echo "Received 429 Too Many Requests. Waiting for 10 seconds before restarting..."
    sleep 5
    sed -i ':a;N;$!ba;s/\n]\n\[\|]\[\|\n]\[/,/g' subreddit_details.json
done