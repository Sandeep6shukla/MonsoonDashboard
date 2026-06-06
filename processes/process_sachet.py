import json
import re

INPUT_FILE="data/raw/sachet_alerts.json"
OUTPUT_FILE="data/processed/business_alerts.json"

RED=[
    "very heavy rain",
    "flood",
    "cyclone",
    "landslide",
    "storm surge"
]

ORANGE=[
    "heavy rain",
    "lightning",
    "gusty wind",
    "50-60 kmph",
    "50 kmph"
]

WATCH=[
    "thunderstorm",
    "moderate rain",
    "wind"
]


def classify(title):

    text=title.lower()

    for word in RED:
        if word in text:
            return "RED","SEND ALERT"

    for word in ORANGE:
        if word in text:
            return "ORANGE","CHECK LOCAL SPOC"

    for word in WATCH:
        if word in text:
            return "WATCH","MONITOR"

    return "INFO","NO ACTION"


def process_sachet():

    with open(
        INPUT_FILE,
        encoding="utf-8"
    ) as f:

        alerts=json.load(f)

    processed=[]

    for alert in alerts:

        severity,action=classify(
            alert["title"]
        )

        processed.append({

            "severity":severity,

            "action":action,

            "title":alert["title"],

            "published":alert["published"],

            "source":alert["source"]

        })

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            processed,
            f,
            indent=4,
            ensure_ascii=False
        )

    print()

    print(
        "Business Alerts Created"
    )

    print(
        OUTPUT_FILE
    )