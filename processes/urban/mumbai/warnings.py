# processes/urban/mumbai/warnings.py


def clean_warning(text):

    return (
        text
        .lower()
        .replace(".", "")
        .strip()
    )


def process_warnings(data):

    active = []

    for item in data.get(
        "weather_warnings",
        []
    ):

        msg = item.get(
            "warningDetails",
            ""
        )

        if clean_warning(msg) in [

            "nil",

            "no warning"

        ]:
            continue

        active.append({

            "type":
            item.get(
                "warningFor"
            ),

            "message":
            msg.strip()

        })

    if not active:

        return {

            "status": "NORMAL",

            "message":
            "No active weather warnings."

        }

    return {

        "status": "ADVISORY",

        "message":(

            active[0]["type"]

            +": "

            + active[0]["message"]
        ),


        "details":
        active

    }