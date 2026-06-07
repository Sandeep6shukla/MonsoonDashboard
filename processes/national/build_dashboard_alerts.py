import json
from datetime import datetime

INPUT_FILE = "data/processed/weather_summary.json"
OUTPUT_FILE = "data/processed/dashboard_alerts.json"

def format_time(value):

    if not value:

        return ""

    try:

        dt = datetime.fromisoformat(
            value
        )

        return dt.strftime(
            "%d %b %H:%M IST"
        )

    except:

        return value


def build_dashboard_alerts():

    print()
    print("=" * 50)
    print("DASHBOARD ALERTS")
    print("=" * 50)

    with open(
        INPUT_FILE,
        encoding="utf-8"
    ) as f:

        alerts = json.load(f)

    grouped = {}

    for alert in alerts:

        key = (

            alert.get(
                "severity",
                ""
            ),

            alert.get(
                "state",
                ""
            ),

            alert.get(
                "event",
                ""
            )

        )

        if key not in grouped:

            grouped[key] = {

                "severity":

                alert.get(
                    "severity",
                    ""
                ),

                "state":

                alert.get(
                    "state",
                    ""
                ),

                "event":

                alert.get(
                    "event",
                    ""
                ),

                "alert_count":

                0,

                "affected_areas":

                set(),

                "headline":

                "",

                "instruction":

                "",

                "sender":

                "",

                "effective":

                "",

                "expires":

                "",

                "source":

                ""

            }

        item = grouped[key]

        item["alert_count"] += 1

        # affected areas

        for area in alert.get(

            "affected_areas",

            []

        ):

            if area:

                item[
                    "affected_areas"
                ].add(

                    area.strip()

                )

        # fallback

        area_desc = alert.get(

            "area_description",

            ""

        )

        if area_desc:

            parts = area_desc.split(",")

            for part in parts:

                part = part.strip()

                if part:

                    item[
                        "affected_areas"
                    ].add(

                        part.title()

                    )

        # keep latest alert

        if (

            alert.get(
                "effective",
                ""
            )

            >

            item[
                "effective"
            ]

        ):

            item[
                "headline"
            ] = alert.get(

                "headline",

                ""

            )

            item[
                "instruction"
            ] = alert.get(

                "instruction",

                ""

            )

            item[
                "sender"
            ] = alert.get(

                "sender",

                ""

            )

            item[
                "effective"
            ] = alert.get(

                "effective",

                ""

            )

            item[
                "source"
            ] = alert.get(

                "source",

                ""

            )

        # latest expiry

        if (

            alert.get(
                "expires",
                ""
            )

            >

            item[
                "expires"
            ]

        ):

            item[
                "expires"
            ] = alert.get(

                "expires",

                ""

            )

    dashboard = []

    for item in grouped.values():

        item[
            "affected_areas"
        ] = sorted(

            list(

                item[
                    "affected_areas"
                ]

            )

        )

        item["valid_from"] = format_time(
            item["effective"]
        )

        item["valid_until"] = format_time(
            item["expires"]
        )

        dashboard.append(

            item

        )

    dashboard.sort(

        key=lambda x:

        (

            0
            if x["severity"] == "RED"
            else 1,

            x["state"],

            x["event"]

        )

    )

    with open(

        OUTPUT_FILE,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            dashboard,

            f,

            indent=4,

            ensure_ascii=False

        )

    print()
    print(
        "Dashboard Alerts Created"
    )
    print(
        OUTPUT_FILE
    )

    print()
    print(
        "Dashboard Cards :",
        len(dashboard)
    )


if __name__ == "__main__":

    build_dashboard_alerts()