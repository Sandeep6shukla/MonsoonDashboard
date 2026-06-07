import json

INPUT_FILE = "data/processed/business_alerts.json"
OUTPUT_FILE = "data/processed/state_summary.json"

SEVERITY_ORDER = {

    "RED": 3,
    "ORANGE": 2,
    "WATCH": 1,
    "INFO": 0

}

PRIORITY_ORDER = {

    "CRITICAL": 3,
    "HIGH": 2,
    "MEDIUM": 1,
    "LOW": 0

}


def aggregate_states():

    print()
    print("=" * 50)
    print("STATE AGGREGATION")
    print("=" * 50)

    with open(
        INPUT_FILE,
        encoding="utf-8"
    ) as f:

        alerts = json.load(f)

    states = {}

    for alert in alerts:

        affected_states = alert.get(
            "affected_states",
            []
        )

        if not affected_states:
            continue

        for state in affected_states:

            if state not in states:

                states[state] = {

                    "state": state,

                    "highest_severity": "INFO",

                    "business_priority": "LOW",

                    "alert_count": 0,

                    "business_categories": set(),

                    "recommended_actions": set()

                }

            summary = states[state]

            summary["alert_count"] += 1

            # Highest severity

            current = summary[
                "highest_severity"
            ]

            new = alert.get(
                "dashboard_severity",
                "INFO"
            )

            if SEVERITY_ORDER[new] > SEVERITY_ORDER[current]:

                summary[
                    "highest_severity"
                ] = new

            # Highest business priority

            current_priority = summary[
                "business_priority"
            ]

            new_priority = alert.get(
                "business_priority",
                "LOW"
            )

            if PRIORITY_ORDER[new_priority] > PRIORITY_ORDER[current_priority]:

                summary[
                    "business_priority"
                ] = new_priority

            # Categories

            category = alert.get(
                "business_category",
                ""
            )

            if category:

                summary[
                    "business_categories"
                ].add(category)

            # Recommended actions

            action = alert.get(
                "recommended_action",
                ""
            )

            if action:

                summary[
                    "recommended_actions"
                ].add(action)

    output = []

    for state in states.values():

        output.append({

            "state":

            state["state"],

            "highest_severity":

            state["highest_severity"],

            "business_priority":

            state["business_priority"],

            "alert_count":

            state["alert_count"],

            "business_categories":

            sorted(
                list(
                    state[
                        "business_categories"
                    ]
                )
            ),

            "recommended_actions":

            sorted(
                list(
                    state[
                        "recommended_actions"
                    ]
                )
            )

        })

    output = sorted(

        output,

        key=lambda x: (

            -SEVERITY_ORDER[
                x[
                    "highest_severity"
                ]
            ],

            x["state"]

        )

    )

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

        "States Found :",

        len(output)

    )

    print()

    print(

        "State Summary Created"

    )

    print(

        OUTPUT_FILE

    )


if __name__ == "__main__":

    aggregate_states()