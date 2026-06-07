import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = "https://dm.mcgm.gov.in/monsoon-high-tide-details"

print()
print("=" * 50)
print("MCGM PAGE INSPECTOR")
print("=" * 50)

print()
print("URL:")
print(URL)

print()

try:

    response = requests.get(
        URL,
        timeout=30,
        headers={
            "User-Agent":
            "Mozilla/5.0"
        }
    )

    print(
        "HTTP Status :",
        response.status_code
    )

    print()

    print(
        "Content Type :",
        response.headers.get(
            "Content-Type",
            ""
        )
    )

    print()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    print("=" * 50)
    print("PAGE TITLE")
    print("=" * 50)

    print(
        soup.title.string
        if soup.title
        else "No title"
    )

    print()

    print("=" * 50)
    print("ALL LINKS")
    print("=" * 50)

    links = set()

    for a in soup.find_all("a"):

        href = a.get("href")

        if href:

            full = urljoin(
                URL,
                href
            )

            links.add(
                full
            )

    for link in sorted(links):

        print(link)

    print()

    print("=" * 50)
    print("PDF LINKS")
    print("=" * 50)

    for link in sorted(links):

        if ".pdf" in link.lower():

            print(link)

    print()

    print("=" * 50)
    print("SCRIPT FILES")
    print("=" * 50)

    for script in soup.find_all(
        "script"
    ):

        src = script.get(
            "src"
        )

        if src:

            print(
                urljoin(
                    URL,
                    src
                )
            )

    print()

    print("=" * 50)
    print("TABLE COUNT")
    print("=" * 50)

    tables = soup.find_all(
        "table"
    )

    print(
        len(tables)
    )

    print()

    print("=" * 50)
    print("IFRAMES")
    print("=" * 50)

    iframes = soup.find_all(
        "iframe"
    )

    print(
        len(iframes)
    )

    for iframe in iframes:

        print(
            iframe.get(
                "src"
            )
        )

except Exception as e:

    print()
    print(
        "ERROR"
    )
    print(
        e
    )