# processes/urban/mumbai/summary.py

STATUS_PRIORITY = {

    "NORMAL": 0,

    "INFO": 1,

    "ACTIVE": 1,

    "MONITORING": 1,

    "ADVISORY": 2,

    "ALERT": 3,

    "CRITICAL": 4

}


def highest_status(statuses):

    highest = "NORMAL"

    for status in statuses:

        if STATUS_PRIORITY.get(
            status,
            0
        ) > STATUS_PRIORITY.get(
            highest,
            0
        ):

            highest = status

    return highest


def build_summary(summary):

    overall = highest_status([

        summary["weather"]["status"],

        summary["warnings"]["status"],

        summary["high_tide"]["status"],

        summary["flooding"]["status"],

        summary["traffic"]["status"]

    ])

    executive = (

        f"Mumbai operational status is "

        f"{overall}. "

        +

        summary["weather"]["message"]

        +

        " "

        +

        summary["warnings"]["message"]

        +

        " "

        +

        summary["traffic"]["message"]

    )

    business = (

        "No significant operational "

        "disruptions currently indicated. "

        "Continue monitoring official advisories."

    )

    if overall == "ADVISORY":

        business = (

            "Minor weather-related "

            "disruptions are possible. "

            "Monitor local advisories."

        )

    if overall == "ALERT":

        business = (

            "Weather conditions could affect "

            "employee commute and local operations."

        )

    if overall == "CRITICAL":

        business = (

            "Significant operational disruptions "

            "are possible. Review business continuity measures."

        )

    return {

        "overall_status": overall,

        "executive_summary": executive,

        "business_implication": business

    }