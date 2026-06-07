# processes/urban/mumbai/flooding.py

def process_flooding(data):

    flood_spots = data.get(
        "flood_spots",
        []
    )

    return {

        "status": "INFO",

        "message":

        f"{len(flood_spots)} official "

        f"flood-prone locations "

        f"under monitoring."

    }