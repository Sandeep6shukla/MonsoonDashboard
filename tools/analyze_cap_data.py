import json

INPUT_FILE="data/raw/cap_alerts.json"


def analyze():

    with open(
        INPUT_FILE,
        encoding="utf-8"
    ) as f:

        alerts=json.load(f)

    print()

    print("="*50)
    print("CAP DATA ANALYSIS")
    print("="*50)

    print()

    print(
        "Total Alerts :",
        len(alerts)
    )

    fields=[

        "sender",

        "severity",

        "urgency",

        "certainty",

        "event",

        "area_desc",

        "msg_type",

        "status"

    ]

    for field in fields:

        print()

        print("-"*50)

        print(field.upper())

        print("-"*50)

        values=set()

        for alert in alerts:

            value=alert.get(
                field,
                ""
            )

            if value:

                values.add(
                    value
                )

        for value in sorted(values):

            print(
                value
            )


if __name__=="__main__":

    analyze()