import json
import requests

OUTPUT_FILE = "data/raw/mcgm_alerts.json"

BASE_URL = "https://dmwebtwo.mcgm.gov.in/api/"

ENDPOINTS = {

    "weather_forecast":
    "weatherForecast/loadAll",

    "weather_warnings":
    "warningDetails/loadAll",

    "high_tides":
    "tidesview/getTidesOrderedByTime",

    "flood_spots":
    "floodSpot/loadAll",

    "traffic":
    "trafficDiversion/loadAllTrafficData",

    "aws_locations":
    "location/loadActiveAWSLocations"

}


def fetch_endpoint(endpoint):

    url = BASE_URL + endpoint

    try:

        response = requests.post(

            url,

            json={},

            timeout=30,

            headers={

                "User-Agent":
                "Mozilla/5.0",

                "Accept":
                "application/json",

                "Content-Type":
                "application/json"

            }

        )

        if response.status_code == 200:

            return response.json()

        return {

            "status":
            response.status_code,

            "error":
            response.text

        }

    except Exception as e:

        return {

            "error":
            str(e)

        }


def collect_mcgm():

    print()

    print("=" * 60)
    print("MCGM COLLECTOR")
    print("=" * 60)

    output = {}

    for name, endpoint in ENDPOINTS.items():

        print()

        print(
            "Collecting:",
            name
        )

        data = fetch_endpoint(
            endpoint
        )

        output[name] = data

        if isinstance(
            data,
            list
        ):

            print(
                "Records:",
                len(data)
            )

        else:

            print(
                "Collected"
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
        "=" * 60
    )

    print(
        "MCGM DATA SAVED"
    )

    print(
        OUTPUT_FILE
    )


if __name__ == "__main__":

    collect_mcgm()