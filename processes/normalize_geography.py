import json
import re

INPUT_FILE = "data/raw/cap_alerts.json"
OUTPUT_FILE = "data/processed/geography_alerts.json"

# State abbreviations

STATE_CODES = {
    "HR": "Haryana",
    "MH": "Maharashtra",
    "UP": "Uttar Pradesh",
    "UK": "Uttarakhand",
    "KL": "Kerala",
    "TN": "Tamil Nadu",
    "KA": "Karnataka",
    "AP": "Andhra Pradesh",
    "WB": "West Bengal",
    "OD": "Odisha",
    "RJ": "Rajasthan",
    "BR": "Bihar",
    "JH": "Jharkhand",
    "CG": "Chhattisgarh",
    "GA": "Goa"
}

# Full state names

STATE_NAMES = [
    "Haryana",
    "Maharashtra",
    "Kerala",
    "Karnataka",
    "Tamil Nadu",
    "Andhra Pradesh",
    "West Bengal",
    "Odisha",
    "Rajasthan",
    "Bihar",
    "Jharkhand",
    "Chhattisgarh",
    "Goa",
    "Uttar Pradesh",
    "Uttarakhand"
]


def extract_states(text):

    states = set()

    text = text.strip()
    text_lower = text.lower()

    # Exact state codes

    for code, state in STATE_CODES.items():

        if text.upper() == code:
            states.add(state)

    # Full state names using word boundaries

    for state in STATE_NAMES:

        pattern = r"\b" + re.escape(state.lower()) + r"\b"

        if re.search(pattern, text_lower):
            states.add(state)

    return sorted(list(states))


def extract_districts(text):

    districts = []

    BAD_WORDS = [
        "district",
        "districts",
        "mandal",
        "mandals"
    ]

    text_lower = text.lower()

    if "districts of" in text_lower:

        part = text_lower.split(
            "districts of"
        )[0]

        items = part.split(",")

        for item in items:

            item = item.strip()

            if not item:
                continue

            if item.isdigit():
                continue

            if item in BAD_WORDS:
                continue

            if item.startswith("and "):
                item = item[4:]

            districts.append(
                item.title()
            )

    return districts


def normalize_geography():

    print()
    print("=" * 50)
    print("GEOGRAPHY NORMALIZER")
    print("=" * 50)

    with open(
        INPUT_FILE,
        encoding="utf-8"
    ) as f:

        alerts = json.load(f)

    output = []

    for alert in alerts:

        new_alert = alert.copy()

        area = alert.get(
            "area_desc",
            ""
        ).strip()

        sender = alert.get(
            "sender",
            ""
        )

        # Preserve issuing authority

        new_alert[
            "issuing_authority"
        ] = sender

        # State extraction

        states = extract_states(
            area
        )

        # Fallback to sender

        if not states:

            sender_lower = sender.lower()

            for state in STATE_NAMES:

                sender_key = state.lower().replace(
                    " ",
                    "-"
                )

                if sender_key in sender_lower:

                    states.append(
                        state
                    )

                    break

        new_alert[
            "affected_states"
        ] = states

        # District extraction

        new_alert[
            "affected_districts"
        ] = extract_districts(
            area
        )

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
        "Total Alerts :",
        len(output)
    )

    print()

    print(
        "Geography Added"
    )

    print(
        OUTPUT_FILE
    )


if __name__ == "__main__":

    normalize_geography()