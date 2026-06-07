import json
from datetime import datetime

from processes.urban.mumbai.weather import process_weather
from processes.urban.mumbai.warnings import process_warnings
from processes.urban.mumbai.tides import process_tides
from processes.urban.mumbai.flooding import process_flooding
from processes.urban.mumbai.traffic import process_traffic
from processes.urban.mumbai.aws import process_aws
from processes.urban.mumbai.summary import build_summary

INPUT_FILE = "data/raw/mcgm_alerts.json"

OUTPUT_FILE = "data/processed/mumbai_summary.json"


def process_mcgm():

    print()
    print("=" * 60)
    print("MUMBAI URBAN PROCESSOR")
    print("=" * 60)

    with open(
        INPUT_FILE,
        encoding="utf-8"
    ) as f:

        data = json.load(f)

    summary = {}

    # --------------------------------
    # DOMAIN PROCESSORS
    # --------------------------------

    summary["weather"] = process_weather(data)

    summary["warnings"] = process_warnings(data)

    summary["high_tide"] = process_tides(data)

    summary["flooding"] = process_flooding(data)

    summary["traffic"] = process_traffic(data)

    summary["aws"] = process_aws(data)

    # --------------------------------
    # EXECUTIVE SUMMARY
    # --------------------------------

    summary.update(
        build_summary(summary)
    )

    # --------------------------------
    # UPDATED
    # --------------------------------

    summary["updated_at"] = (
        datetime.now()
        .isoformat()
    )

    # --------------------------------
    # SAVE
    # --------------------------------

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

    # --------------------------------
    # CONSOLE OUTPUT
    # --------------------------------

    print()

    print(
        "Mumbai Summary Created"
    )

    print(
        OUTPUT_FILE
    )

    print()

    print(
        "Overall Status:"
    )

    print(
        summary[
            "overall_status"
        ]
    )

    print()

    print(
        "Executive Summary:"
    )

    print(
        summary[
            "executive_summary"
        ]
    )

    print()

    print(
        "Business Implication:"
    )

    print(
        summary[
            "business_implication"
        ]
    )

    print()

    print(
        "Weather:"
    )

    print(
        summary[
            "weather"
        ][
            "message"
        ]
    )

    print()

    print(
        "Warnings:"
    )

    print(
        summary[
            "warnings"
        ][
            "message"
        ]
    )

    print()

    print(
        "Traffic:"
    )

    print(
        summary[
            "traffic"
        ][
            "message"
        ]
    )

    print()

    print(
        "High Tide:"
    )

    print(
        summary[
            "high_tide"
        ][
            "message"
        ]
    )

    print()

    print(
        "Flood Monitoring:"
    )

    print(
        summary[
            "flooding"
        ][
            "message"
        ]
    )

    print()

    print(
        "AWS:"
    )

    print(
        summary[
            "aws"
        ][
            "message"
        ]
    )


if __name__ == "__main__":

    process_mcgm()