import feedparser
import json

RSS_URL="https://sachet.ndma.gov.in/cap_public_website/rss/rss_india.xml"

def fetch_sachet():

    print("Connecting to Sachet RSS Feed...")

    feed=feedparser.parse(RSS_URL)

    print()

    print(
        f"Alerts Found : {len(feed.entries)}"
    )

    alerts=[]

    for entry in feed.entries:

        alert={

            "source":"Sachet",

            "title":entry.title,

            "published":entry.published,

            "link":entry.link

        }

        alerts.append(alert)

    with open(

        "data/raw/sachet_alerts.json",

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            alerts,

            f,

            indent=4,

            ensure_ascii=False

        )

    print()

    print(

        "Sachet Alerts Saved."

    )

    print()

    print(

        "Output File :"

    )

    print(

        "data/raw/sachet_alerts.json"

    )