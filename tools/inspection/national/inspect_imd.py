import requests
import json

URL = "https://api.imd.gov.in/api/v1/districtwarning"

print("=" * 50)
print("IMD API INSPECTOR")
print("=" * 50)

response = requests.get(URL)

print()
print("HTTP Status :", response.status_code)

print()
print("Headers:")
for k, v in response.headers.items():
    print(f"{k}: {v}")

print()

try:
    data = response.json()

    print("Response Type :", type(data))

    print()
    print("JSON Response")
    print("=" * 50)

    print(
        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        )
    )

except Exception:

    print("Raw Response")
    print("=" * 50)
    print(response.text)