import json
import sys
import time

from pathlib import Path
from parsers.cap_parser import parse_cap

sys.path.append(
    str(
        Path(__file__).resolve().parent.parent
    )
)

INPUT_FILE = "data/raw/sachet_alerts.json"
OUTPUT_FILE = "data/raw/cap_alerts.json"


def collect_cap():

    print()
    print("=" * 50)
    print("COLLECTING CAP ALERTS")
    print("=" * 50)

    with open(
        INPUT_FILE,
        encoding="utf-8"
    ) as f:

        alerts = json.load(f)

    cap_alerts = []

    total = len(alerts)

    for index, alert in enumerate(alerts, start=1):

        try:

            print(
                f"Processing {index}/{total}"
            )

            cap = parse_cap(
                alert["link"]
            )

            cap["rss_title"]=alert.get(
                "title",
                ""
            )

            cap["rss_published"]=alert.get(
                "published",
                ""
            )

            cap["rss_link"]=alert.get(
                "link",
                ""
            )

            cap_alerts.append(
                cap
            )

            time.sleep(
                1
            )

        except Exception as e:

            print(
                "Error:",
                e
            )

            time.sleep(
                5
            )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            cap_alerts,
            f,
            indent=4,
            ensure_ascii=False
        )

    print()
    print("CAP Alerts Saved")
    print(OUTPUT_FILE)


if __name__ == "__main__":

    collect_cap()