import requests
import re

JS_URL = "https://dm.mcgm.gov.in/main.b3fa1c45a28b2635.js"

print()
print("=" * 60)
print("MCGM ANGULAR SERVICE INSPECTOR")
print("=" * 60)

try:

    response = requests.get(
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
        response.status_code
    )

    print()

    js = response.text

    print(
        "JS Size :",
        len(js),
        "characters"
    )

    print()

    patterns = [

        "HttpClient",

        "http.get",

        "http.post",

        "api",

        "baseUrl",

        "apiUrl",

        "environment",

        "service",

        "/api",

        "backend",

        "getData",

        "postData",

        "fetch",

        "weather",

        "tide",

        "traffic",

        "warning",

        "alert",

        "rain",

        "radar"

    ]

    WINDOW = 120

    found = []

    print("=" * 60)
    print("POTENTIAL SERVICE REFERENCES")
    print("=" * 60)

    for pattern in patterns:

        for match in re.finditer(
            re.escape(pattern),
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

            found.append(
                (
                    pattern,
                    snippet
                )
            )

    seen = set()

    count = 0

    for pattern, snippet in found:

        key = snippet[:80]

        if key in seen:
            continue

        seen.add(key)

        count += 1

        print()
        print("-" * 60)

        print(
            "MATCH",
            count
        )

        print(
            "PATTERN :",
            pattern
        )

        print()

        print(
            snippet
        )

        print()

        if count >= 100:
            break

    print()

    print("=" * 60)
    print("JSON FILE REFERENCES")
    print("=" * 60)

    jsons = set(

        re.findall(
            r'[^"\']+\.json',
            js
        )

    )

    for item in sorted(
        jsons
    ):

        print(
            item
        )

    print()

    print("=" * 60)
    print("API PATH REFERENCES")
    print("=" * 60)

    apis = set(

        re.findall(
            r'/api/[A-Za-z0-9_/\-]*',
            js
        )

    )

    for item in sorted(
        apis
    ):

        print(
            item
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