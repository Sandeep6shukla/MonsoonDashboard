import json

INPUT_FILE="data/processed/business_alerts.json"
OUTPUT_FILE="data/processed/state_summary.json"

STATES=[

"Kerala",
"Maharashtra",
"Rajasthan",
"West Bengal",
"Andhra Pradesh",
"Karnataka",
"Tamil Nadu",
"Delhi",
"Uttar Pradesh",
"Gujarat",
"Punjab",
"Haryana",
"Bihar",
"Jharkhand",
"Odisha",
"Assam",
"Telangana",
"Madhya Pradesh",
"Chhattisgarh"

]

PRIORITY={

"INFO":1,
"WATCH":2,
"ORANGE":3,
"RED":4

}

ACTIONS={

"INFO":"NO ACTION",

"WATCH":"MONITOR",

"ORANGE":"CHECK LOCAL SPOC",

"RED":"SEND ALERT"

}


def find_state(title):

    for state in STATES:

        if state.lower() in title.lower():

            return state

    return "Unknown"


def aggregate_alerts():

    with open(
        INPUT_FILE,
        encoding="utf-8"
    ) as f:

        alerts=json.load(f)

    summary={}

    for alert in alerts:

        state=find_state(
            alert["title"]
        )

        if state not in summary:

            summary[state]={

                "state":state,

                "government_alerts":0,

                "severity":"INFO",

                "primary_risk":"",

                "action":"NO ACTION"

            }

        summary[state][
            "government_alerts"
        ]+=1

        if PRIORITY[
            alert["severity"]
        ]>PRIORITY[
            summary[state][
                "severity"
            ]
        ]:

            summary[state][
                "severity"
            ]=alert[
                "severity"
            ]

            summary[state][
                "primary_risk"
            ]=alert[
                "title"
            ]

            summary[state][
                "action"
            ]=ACTIONS[
                alert[
                    "severity"
                ]
            ]

    output=list(
        summary.values()
    )

    output.sort(

        key=lambda x:
        PRIORITY[
            x["severity"]
        ],

        reverse=True

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
        "State Summary Created"
    )

    print(
        OUTPUT_FILE
    )