import requests
import json

BASE_URL = "https://dmwebtwo.mcgm.gov.in/api/"

ENDPOINTS = [

    "weatherForecast/loadAll",

    "warningDetails/loadAll",

    "tidesview/getTidesOrderedByTime",

    "floodSpot/loadAll",

    "trafficDiversion/loadAllTrafficData",

    "location/loadActiveLocations",

    "location/loadActiveAWSLocations",

    "reports/loadReportData15Min",

    "reports/loadWaterLevelReportData15Min"

]

print()
print("=" * 60)
print("MCGM API TESTER")
print("=" * 60)

print()
print(
    "Base URL:"
)
print(
    BASE_URL
)

print()

for endpoint in ENDPOINTS:

    url = BASE_URL + endpoint

    print("=" * 60)

    print(
        "ENDPOINT"
    )

    print(
        endpoint
    )

    print()

    print(
        "URL"
    )

    print(
        url
    )

    print()

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

        print(
            "HTTP Status :",
            response.status_code
        )

        print()

        print(
            "Content Type :"
        )

        print(
            response.headers.get(
                "Content-Type"
            )
        )

        print()

        text = response.text

        try:

            data = response.json()

            print(
                "JSON Response"
            )

            print(
                "-" * 40
            )

            if isinstance(
                data,
                list
            ):

                print(
                    "List Length :",
                    len(data)
                )

                if len(data):

                    print()

                    print(
                        "First Record"
                    )

                    print(
                        json.dumps(

                            data[0],

                            indent=4,

                            ensure_ascii=False

                        )[:1000]
                    )

            elif isinstance(
                data,
                dict
            ):

                print(
                    "Dictionary"
                )

                print()

                print(
                    "Keys:"
                )

                print(
                    list(
                        data.keys()
                    )
                )

                print()

                print(
                    json.dumps(

                        data,

                        indent=4,

                        ensure_ascii=False

                    )[:1000]
                )

            else:

                print(
                    data
                )

        except:

            print(
                "Non JSON Response"
            )

            print()

            print(
                text[:1000]
            )

    except Exception as e:

        print(
            "ERROR"
        )

        print(
            e
        )

    print()