import requests
import re

JS_URL = "https://dm.mcgm.gov.in/main.b3fa1c45a28b2635.js"

print()
print("=" * 60)
print("MCGM CONFIG INSPECTOR")
print("=" * 60)

try:

    r = requests.get(
        JS_URL,
        timeout=60,
        headers={
            "User-Agent":
            "Mozilla/5.0"
        }
    )

    print()
    print(
        "HTTP Status :",
        r.status_code
    )

    js = r.text

    print(
        "JS Size :",
        len(js)
    )

    print()

    SEARCH_TERMS = [

        "Bt.BASE_URL",

        "Bt.BASE_NODE_SERVER_URL",

        "BASE_URL",

        "BASE_NODE_SERVER_URL",

        "baseUrl",

        "apiUrl",

        "this.warnings",

        "this.tides",

        "this.selectedDateTideData",

        "this.allWeatherData",

        "this.weatherForecastByID",

        "this.aws",

        "this.allTrafficData",

        "this.flightCreate",

        "this.railwayCreate",

        "this.bestCreate",

        "this.monorailCreate",

        "this.metrorailCreate",

        "this.reportJSON15Min",

        "this.reportJSON1Hr",

        "this.reportJSON3Hr",

        "this.reportJSON6Hr",

        "this.reportJSON12Hr",

        "this.reportJSON24Hr",

        "this.reportJSONWeekly",

        "this.reportJSONMonthly",

        "this.map15Mins",

        "this.map1Hour",

        "this.map3Hours",

        "this.map6Hours",

        "this.map12Hours",

        "this.map24Hours",

        "loadFloodingSpotData24Hr"

    ]

    WINDOW = 300

    found = set()

    print("=" * 60)
    print("CONFIG REFERENCES")
    print("=" * 60)

    count = 0

    for term in SEARCH_TERMS:

        for match in re.finditer(

            re.escape(term),

            js,

            flags=re.IGNORECASE

        ):

            start = max(

                0,

                match.start() - WINDOW

            )

            end = min(

                len(js),

                match.end() + WINDOW

            )

            snippet = js[
                start:end
            ]

            snippet = snippet.replace(
                "\n",
                " "
            )

            snippet = snippet.replace(
                "\r",
                " "
            )

            key = snippet[:150]

            if key in found:
                continue

            found.add(
                key
            )

            count += 1

            print()

            print("-" * 60)

            print(
                "MATCH",
                count
            )

            print()

            print(
                "SEARCH TERM :",
                term
            )

            print()

            print(
                snippet
            )

            print()

    print()

    print("=" * 60)
    print("BASE_URL ASSIGNMENTS")
    print("=" * 60)

    base_patterns = [

        r'BASE_URL[^;]{0,300}',

        r'BASE_NODE_SERVER_URL[^;]{0,300}',

        r'Bt\.BASE_URL[^;]{0,300}',

        r'Bt\.BASE_NODE_SERVER_URL[^;]{0,300}'

    ]

    printed = set()

    for pattern in base_patterns:

        matches = re.findall(

            pattern,

            js,

            flags=re.IGNORECASE

        )

        for item in matches:

            if item in printed:
                continue

            printed.add(
                item
            )

            print()
            print(item)

    print()

    print("=" * 60)
    print("URL LIKE STRINGS")
    print("=" * 60)

    urls = set(

        re.findall(

            r'https?://[^"\', ]+',

            js

        )

    )

    for url in sorted(urls):

        if "mcgm" in url.lower():

            print(
                url
            )

    print()

    print("=" * 60)
    print("DONE")
    print("=" * 60)

except Exception as e:

    print()

    print(
        "ERROR"
    )

    print(
        e
    )