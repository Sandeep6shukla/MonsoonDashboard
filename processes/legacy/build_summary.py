import json

INPUT_FILE = "data/processed/state_summary.json"
OUTPUT_FILE = "data/processed/executive_summary.json"


def build_summary():

    print()
    print("=" * 50)
    print("EXECUTIVE SUMMARY")
    print("=" * 50)

    with open(
        INPUT_FILE,
        encoding="utf-8"
    ) as f:

        states = json.load(f)

    critical = []
    high = []
    watch = []

    risks = set()
    actions = set()

    overall = "NORMAL"

    for state in states:

        severity = state.get(
            "highest_severity",
            "INFO"
        )

        name = state.get(
            "state",
            ""
        )

        if severity == "RED":

            critical.append(
                name
            )

            overall = "CRITICAL"

        elif severity == "ORANGE":

            high.append(
                name
            )

            if overall != "CRITICAL":

                overall = "ELEVATED"

        elif severity == "WATCH":

            watch.append(
                name
            )

            if overall == "NORMAL":

                overall = "WATCH"

        for risk in state.get(
            "business_categories",
            []
        ):

            risks.add(
                risk
            )

        for action in state.get(
            "recommended_actions",
            []
        ):

            actions.add(
                action
            )

    assessment = []

    assessment.append(

        f"Overall business continuity status is {overall}."

    )

    if critical:

        assessment.append(

            "Critical states: "

            + ", ".join(
                critical
            )
            + "."
        )

    if high:

        assessment.append(

            "High risk states: "

            + ", ".join(
                high
            )
            + "."
        )

    if risks:

        assessment.append(

            "Primary business risks include "

            + ", ".join(
                sorted(
                    risks
                )
            )
            + "."
        )

    assessment.append(

        "Continue monitoring official advisories."

    )

    summary = {

        "overall_status":

        overall,

        "critical_states":

        critical,

        "high_risk_states":

        high,

        "watch_states":

        watch,

        "top_business_risks":

        sorted(
            list(
                risks
            )
        ),

        "recommended_actions":

        sorted(
            list(
                actions
            )
        ),

        "todays_assessment":

        " ".join(
            assessment
        )

    }

    with open(

        OUTPUT_FILE,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            summary,

            f,

            indent=4,

            ensure_ascii=False

        )

    print()

    print(

        "Executive Summary Created"

    )

    print(

        OUTPUT_FILE

    )


if __name__ == "__main__":

    build_summary()