import json

INPUT_FILE = "data/processed/dashboard_alerts.json"
OUTPUT_FILE = "data/processed/weather_dashboard_summary.json"


def build_weather_summary():

    print()
    print("=" * 50)
    print("WEATHER SUMMARY")
    print("=" * 50)

    with open(
        INPUT_FILE,
        encoding="utf-8"
    ) as f:

        alerts = json.load(f)

    red = [
        a for a in alerts
        if a["severity"] == "RED"
    ]

    orange = [
        a for a in alerts
        if a["severity"] == "ORANGE"
    ]

    text = []

    if red:

        states = sorted(
            set(
                a["state"]
                for a in red
            )
        )

        text.append(
            "Red alerts are active across "
            + ", ".join(states)
            + "."
        )

    if orange:

        states = sorted(
            set(
                a["state"]
                for a in orange
            )
        )

        text.append(
            "Orange alerts are active across "
            + ", ".join(states)
            + "."
        )

    events = sorted(
        set(
            a["event"]
            for a in alerts
        )
    )

    if events:

        text.append(
            "Major weather events include "
            + ", ".join(events)
            + "."
        )

    text.append(
        "Please follow official SDMA advisories."
    )

    output = {

        "national_summary":

        " ".join(text)

    }

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            output,
            f,
            indent=4,
            ensure_ascii=False
        )

    print()
    print(
        "Weather Summary Created"
    )

    print(
        OUTPUT_FILE
    )


if __name__ == "__main__":

    build_weather_summary()