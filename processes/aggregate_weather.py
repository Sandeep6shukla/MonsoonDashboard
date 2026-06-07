import json

INPUT_FILE="data/processed/geography_alerts.json"

OUTPUT_FILE="data/processed/weather_summary.json"


def aggregate_weather():

    print()
    print("="*50)
    print("WEATHER AGGREGATION")
    print("="*50)

    with open(
        INPUT_FILE,
        encoding="utf-8"
    ) as f:

        alerts=json.load(f)

    weather=[]

    for alert in alerts:

        severity=alert.get(
            "severity",
            ""
        )

        if severity not in [

            "Extreme",
            "Severe"

        ]:

            continue

        states=alert.get(

            "affected_states",

            []

        )

        if not states:

            continue

        for state in states:

            weather.append({

                "severity":

                "RED"
                if severity=="Extreme"
                else
                "ORANGE",

                "state":

                state,

                "event":

                alert.get(
                    "event",
                    ""
                ),

                "headline":

                alert.get(
                    "headline",
                    ""
                ),

                "affected_areas":

                alert.get(
                    "affected_districts",
                    []
                ),

                "area_description":

                alert.get(
                    "area_desc",
                    ""
                ),

                "instruction":

                alert.get(
                    "instruction",
                    ""
                ),

                "sender":

                alert.get(
                    "sender",
                    ""
                ),

                "effective":

                alert.get(
                    "effective",
                    ""
                ),

                "expires":

                alert.get(
                    "expires",
                    ""
                ),

                "source":

                alert.get(
                    "rss_link",
                    ""
                )
            })

    weather.sort(

        key=lambda x:

        (
            0
            if x["severity"]=="RED"
            else
            1,

            x["expires"]

        )

    )

    with open(

        OUTPUT_FILE,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            weather,

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

    print()
    print(
        "Dashboard Alerts :",
        len(weather)
    )


if __name__=="__main__":

    aggregate_weather()