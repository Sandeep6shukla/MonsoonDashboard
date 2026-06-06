from pathlib import Path
import requests

# Cache folder

CACHE_DIR = Path("cache/xml")

CACHE_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def extract_identifier(url):

    """
    Extract identifier from CAP URL.
    """

    if "identifier=" not in url:
        return None

    return url.split(
        "identifier="
    )[1]


def get_cache_path(identifier):

    """
    Return XML cache path.
    """

    return CACHE_DIR / f"{identifier}.xml"


def get_cached_xml(identifier):

    """
    Return cached XML if available.
    """

    cache_path = get_cache_path(
        identifier
    )

    if cache_path.exists():

        print(
            f"Cache Hit : {identifier}"
        )

        with open(
            cache_path,
            encoding="utf-8"
        ) as f:

            return f.read()

    return None


def download_and_cache(
    url,
    identifier
):

    """
    Download XML and save.
    """

    print(
        f"Downloading : {identifier}"
    )

    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    xml = response.text

    cache_path = get_cache_path(
        identifier
    )

    with open(
        cache_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(xml)

    return xml


def get_xml(url):

    """
    Main function.
    """

    identifier = extract_identifier(
        url
    )

    if identifier is None:

        raise Exception(
            "Invalid CAP URL"
        )

    cached = get_cached_xml(
        identifier
    )

    if cached:

        return cached

    return download_and_cache(
        url,
        identifier
    )

if __name__ == "__main__":

    TEST_URL = (
        "https://sachet.ndma.gov.in/"
        "cap_public_website/"
        "FetchXMLFile?"
        "identifier=1780737869866024"
    )

    xml = get_xml(
        TEST_URL
    )

    print()

    print("="*50)

    print("FIRST 500 CHARACTERS")

    print("="*50)

    print()

    print(
        xml[:500]
    )