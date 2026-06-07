import requests

URL="https://dmwebtwo.mcgm.gov.in/api/"

print()
print("="*50)
print("MCGM API INSPECTOR")
print("="*50)

try:

    r=requests.get(
        URL,
        timeout=30
    )

    print()

    print(
        "Status:",
        r.status_code
    )

    print()

    print(
        "Content Type:"
    )

    print(
        r.headers.get(
            "Content-Type"
        )
    )

    print()

    print(
        "First 1000 chars"
    )

    print("="*50)

    print(
        r.text[:1000]
    )

except Exception as e:

    print(e)