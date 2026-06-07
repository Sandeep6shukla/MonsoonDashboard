# processes/urban/mumbai/tides.py

def process_tides(data):

    tides = data.get(
        "high_tides",
        []
    )

    if not tides:

        return {

            "status": "INFO",

            "message":

            "No tide information available."

        }

    tide = tides[0]

    height = tide.get(
        "height",
        0
    )

    status = "INFO"

    if height >= 4:

        status = "ADVISORY"

    if height >= 4.5:

        status = "ALERT"

    return {

        "status": status,

        "message":

        f"Next "

        f"{tide.get('tidelabel')} "

        f"Tide "

        f"{height} m "

        f"at "

        f"{tide.get('tidetime')}."

    }