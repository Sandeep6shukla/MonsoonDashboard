import json

INPUT_FILE = "data/processed/national_dashboard.json"

OUTPUT_FILE = "data/processed/national_briefing.json"


def build_national_briefing():

    print()
    print("=" * 60)
    print("NATIONAL BRIEFING BUILDER")
    print("=" * 60)

    with open(
        INPUT_FILE,
        encoding="utf-8"
    ) as f:

        alerts = json.load(f)

    severity_rank = {

        "RED": 3,

        "ORANGE": 2,

        "YELLOW": 1

    }

    state_summary = {}

    # --------------------------------
    # AGGREGATE ALERTS BY STATE
    # --------------------------------

    for alert in alerts:

        state = alert.get(
            "state",
            "Unknown"
        )

        severity = alert.get(
            "severity",
            "YELLOW"
        )

        event = alert.get(
            "event",
            "Weather Alert"
        )

        districts = alert.get(
            "districts",
            []
        )

        advisory = alert.get(
            "advisory",
            ""
        )

        if state not in state_summary:

            state_summary[state] = {

                "state": state,

                "severity": severity,

                "events": set(),

                "districts": set(),

                "advisories": set()

            }

        current = state_summary[state]

        # Keep highest severity

        if severity_rank.get(
            severity,
            0
        ) > severity_rank.get(
            current["severity"],
            0
        ):

            current["severity"] = severity

        # Events

        current["events"].add(
            event
        )

        # Districts

        current["districts"].update(
            districts
        )

        # Advisories

        if advisory:

            current["advisories"].add(
                advisory
            )

    # --------------------------------
    # CONVERT TO LIST
    # --------------------------------

    states = []

    for state_data in state_summary.values():

        states.append({

            "state":

            state_data["state"],

            "severity":

            state_data["severity"],

            "events":

            sorted(
                list(
                    state_data["events"]
                )
            ),

            "district_count":

            len(
                state_data["districts"]
            ),

            "districts":

            sorted(
                list(
                    state_data["districts"]
                )
            )[:10],

            "advisories":

            sorted(
                list(
                    state_data["advisories"]
                )
            )

        })

    # --------------------------------
    # SORT STATES
    # --------------------------------

    states.sort(

        key=lambda x:

        severity_rank.get(
            x["severity"],
            0
        ),

        reverse=True

    )

    # --------------------------------
    # OVERALL STATUS
    # --------------------------------

    overall_status = "NORMAL"

    if any(
        state["severity"] == "RED"
        for state in states
    ):

        overall_status = "CRITICAL"

    elif any(
        state["severity"] == "ORANGE"
        for state in states
    ):

        overall_status = "HIGH"

    # --------------------------------
    # RED / ORANGE SUMMARY
    # --------------------------------

    red_states = [

        state

        for state in states

        if state["severity"] == "RED"

    ]

    orange_states = [

        state

        for state in states

        if state["severity"] == "ORANGE"

    ]

    red_summary = []

    for state in red_states:

        events = ", ".join(

            state["events"][:3]

        )

        red_summary.append(

            f"{state['state']} faces "

            f"{events} risks."

        )

    orange_summary = []

    for state in orange_states:

        events = ", ".join(

            state["events"][:2]

        )

        orange_summary.append(

            f"{state['state']} faces "

            f"{events} risks."

        )

    # --------------------------------
    # EXECUTIVE SUMMARY
    # --------------------------------

    executive_summary = (

        red_summary +

        orange_summary[:5]

    )

    # --------------------------------
    # BUILD OUTPUT
    # --------------------------------

    briefing = {

        "overall_status":

        overall_status,

        "red_summary":

        red_summary,

        "orange_summary":

        orange_summary,

        "states":

        states,

        "executive_summary":

        executive_summary

    }

    # --------------------------------
    # SAVE
    # --------------------------------

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(

            briefing,

            f,

            indent=4,

            ensure_ascii=False

        )

    # --------------------------------
    # CONSOLE OUTPUT
    # --------------------------------

    print()

    print(
        "National Briefing Created"
    )

    print(
        OUTPUT_FILE
    )

    print()

    print(
        "Overall Status:",
        overall_status
    )

    print()

    print(
        "States:",
        len(states)
    )

    print()

    print(
        "RED ALERT SUMMARY"
    )

    print("-" * 60)

    for item in red_summary:

        print(
            "🔴",
            item
        )

    print()

    print(
        "ORANGE ALERT SUMMARY"
    )

    print("-" * 60)

    for item in orange_summary:

        print(
            "🟠",
            item
        )

    print()


if __name__ == "__main__":

    build_national_briefing()