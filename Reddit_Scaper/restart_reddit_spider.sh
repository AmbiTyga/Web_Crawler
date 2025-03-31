# #!/bin/bash
total_entries=341821

while true; do
    echo "Starting the spider..."
    sed -i ':a;N;$!ba;s/\n]\n\[\|]\[\|\n]\[/,/g' subreddit_details.json
    scrapy runspider get_subreddit_details.py -o subreddit_details.json
    entries=$(jq '. | length' subreddit_details.json 2>/dev/null)
    entries=${entries:-0}  # Default to 0 if jq fails or returns empty
    if [[ "$entries" =~ ^[0-9]+$ ]]; then
        echo "Number of entries left: $((total_entries - entries))"
    else
        echo "Error: 'entries' is not a valid number: $entries"
    fi

    echo "Received 429 Too Many Requests. Waiting for 10 seconds before restarting..."
    sleep 5
    sed -i ':a;N;$!ba;s/\n]\n\[\|]\[\|\n]\[/,/g' subreddit_details.json
done