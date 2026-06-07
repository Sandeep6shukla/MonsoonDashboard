import requests
import xml.etree.ElementTree as ET

URL = "https://sachet.ndma.gov.in/cap_public_website/FetchXMLFile?identifier=1780737869866024"


def inspect(element, level=0):

    indent = " " * level

    value = ""

    if element.text:
        value = element.text.strip()

    if len(value) > 120:
        value = value[:120] + "..."

    print(f"{indent}{element.tag}: {value}")

    for child in element:
        inspect(child, level + 2)


def inspect_cap():

    print("=" * 60)
    print("SACHET CAP XML INSPECTOR")
    print("=" * 60)

    response = requests.get(URL)

    print()
    print("HTTP Status:", response.status_code)

    if response.status_code != 200:
        print("Unable to fetch CAP XML")
        return

    root = ET.fromstring(response.content)

    print()
    print("=" * 60)
    print("CAP CONTENT")
    print("=" * 60)
    print()

    inspect(root)


if __name__ == "__main__":
    inspect_cap()