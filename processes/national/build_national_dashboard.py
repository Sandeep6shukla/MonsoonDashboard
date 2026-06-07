import json

INPUT_FILE = "data/processed/dashboard_alerts.json"

OUTPUT_FILE = "data/processed/national_dashboard.json"


def build_national_dashboard():

    print()
    print("=" * 60)
    print("NATIONAL DASHBOARD BUILDER")
    print("=" * 60)

    with open(
        INPUT_FILE,
        encoding="utf-8"
    ) as f:

        alerts = json.load(f)

    dashboard = []

    for alert in alerts:

        districts = []

        if alert.get("affected_areas"):
            districts = alert["affected_areas"]

        elif alert.get("area_description"):

            districts = [

                x.strip()

                for x in alert[
                    "area_description"
                ].split(",")

            ]

        dashboard.append({

            "severity":

            alert.get(
                "severity"
            ),

            "state":

            alert.get(
                "state"
            ),

            "event":

            alert.get(
                "event"
            ),

            "districts":

            districts,

            "reason":

            alert.get(
                "headline"
            ),

            "advisory":

            alert.get(
                "instruction"
            )

        })

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
        "National Dashboard Created"
    )
    print(
        OUTPUT_FILE
    )

    print()
    print(
        "Alerts:",
        len(dashboard)
    )


if __name__ == "__main__":

    build_national_dashboard()