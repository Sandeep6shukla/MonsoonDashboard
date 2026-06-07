# processes/urban/mumbai/traffic.py

def process_traffic(data):

    traffic = data.get(
        "traffic",
        {}
    )

    count = 0

    if isinstance(
        traffic,
        list
    ):

        count = len(
            traffic
        )

    if count == 0:

        return {

            "status": "NORMAL",

            "message":

            "No active traffic diversions reported."

        }

    return {

        "status": "ALERT",

        "message":

        f"{count} active traffic diversion(s)."

    }