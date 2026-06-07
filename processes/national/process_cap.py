import json

INPUT_FILE="data/processed/geography_alerts.json"

OUTPUT_FILE="data/processed/business_alerts.json"

SEVERITY_MAP={

    "Extreme":"RED",

    "Severe":"ORANGE",

    "Moderate":"WATCH"

}

URGENCY_MAP={

    "Immediate":"TAKE ACTION",

    "Expected":"MONITOR"

}

EVENT_MAP={

    "Very Heavy Rain":

    "Flood Risk",

    "Heavy Rain":

    "Transport Risk",

    "Moderate Rain":

    "Transport Risk",

    "Light Rain":

    "Weather Watch",

    "Lightning":

    "Employee Safety",

    "Thunderstorm with Lightning":

    "Employee Safety",

    "Lightning, Gusty winds, and Thunderstorm":

    "Employee Safety",

    "Light Thunderstorm with surface wind":

    "Travel Risk",

    "Moderate Thunderstorms with surface wind":

    "Travel Risk",

    "Severe Thunderstorms with surface wind":

    "Travel Risk",

    "Thunder shower with strong wind":

    "Travel Risk",

    "Thunderstorms with Hail":

    "Property Risk",

    "Festival/ Fair/Temple Stampedes":

    "Crowd Safety"

}

ACTION_MAP={

    "Flood Risk":

    "Monitor transport and local operations.",

    "Transport Risk":

    "Review road and employee travel conditions.",

    "Employee Safety":

    "Advise employees to avoid open areas.",

    "Travel Risk":

    "Monitor transport disruptions.",

    "Property Risk":

    "Review facility preparedness.",

    "Crowd Safety":

    "Monitor public gathering risks.",

    "Weather Watch":

    "Continue monitoring."
}

def get_business_category(event):

    return EVENT_MAP.get(

        event,

        "General Weather"

    )

def get_priority(

    severity,

    urgency

):

    if severity=="RED":

        return "CRITICAL"

    if severity=="ORANGE":

        return "HIGH"

    if urgency=="TAKE ACTION":

        return "HIGH"

    return "MEDIUM"

def process_cap():

    print()

    print("="*50)

    print(

        "CAP BUSINESS PROCESSOR"

    )

    print("="*50)

    with open(

        INPUT_FILE,

        encoding="utf-8"

    ) as f:

        alerts=json.load(f)

    output=[]

    for alert in alerts:

        new_alert=alert.copy()

        dashboard_severity=SEVERITY_MAP.get(

            alert.get(

                "severity",

                ""

            ),

            "INFO"

        )

        action_status=URGENCY_MAP.get(

            alert.get(

                "urgency",

                ""

            ),

            "MONITOR"

        )

        category=get_business_category(

            alert.get(

                "event",

                ""

            )

        )

        priority=get_priority(

            dashboard_severity,

            action_status

        )

        recommendation=ACTION_MAP.get(

            category,

            "Continue monitoring."

        )

        new_alert[

            "dashboard_severity"

        ]=dashboard_severity

        new_alert[

            "action_status"

        ]=action_status

        new_alert[

            "business_category"

        ]=category

        new_alert[

            "business_priority"

        ]=priority

        new_alert[

            "recommended_action"

        ]=recommendation

        output.append(

            new_alert

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

        "Business Alerts Created"

    )

    print(

        OUTPUT_FILE

    )

if __name__=="__main__":

    process_cap()