import requests
import xml.etree.ElementTree as ET

# CAP Namespace
NS = {
    "cap": "urn:oasis:names:tc:emergency:cap:1.2"
}


def get_text(parent, tag):

    try:

        element = parent.find(
            f"cap:{tag}",
            NS
        )

        if element is not None and element.text:

            return element.text.strip()

    except:
        pass

    return ""


def parse_cap(url):

    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    root = ET.fromstring(
        response.content
    )

    info = root.find(
        "cap:info",
        NS
    )

    area = None

    if info is not None:

        area = info.find(
            "cap:area",
            NS
        )

    polygon_url = ""

    if info is not None:

        for parameter in info.findall(
            "cap:parameter",
            NS
        ):

            name = get_text(
                parameter,
                "valueName"
            )

            if name == "Polygon URL":

                polygon_url = get_text(
                    parameter,
                    "value"
                )

    result = {

        "identifier":

        get_text(
            root,
            "identifier"
        ),

        "sender":

        get_text(
            root,
            "sender"
        ),

        "sent":

        get_text(
            root,
            "sent"
        ),

        "status":

        get_text(
            root,
            "status"
        ),

        "msg_type":

        get_text(
            root,
            "msgType"
        ),

        "scope":

        get_text(
            root,
            "scope"
        ),

        "category":

        get_text(
            info,
            "category"
        ) if info else "",

        "event":

        get_text(
            info,
            "event"
        ) if info else "",

        "urgency":

        get_text(
            info,
            "urgency"
        ) if info else "",

        "severity":

        get_text(
            info,
            "severity"
        ) if info else "",

        "certainty":

        get_text(
            info,
            "certainty"
        ) if info else "",

        "effective":

        get_text(
            info,
            "effective"
        ) if info else "",

        "expires":

        get_text(
            info,
            "expires"
        ) if info else "",

        "headline":

        get_text(
            info,
            "headline"
        ) if info else "",

        "description":

        get_text(
            info,
            "description"
        ) if info else "",

        "instruction":

        get_text(
            info,
            "instruction"
        ) if info else "",

        "area_desc":

        get_text(
            area,
            "areaDesc"
        ) if area else "",

        "polygon_url":

        polygon_url

    }

    return result

if __name__ == "__main__":

    TEST_URL = "https://sachet.ndma.gov.in/cap_public_website/FetchXMLFile?identifier=1780737869866024"

    data = parse_cap(
        TEST_URL
    )

    import json

    print(

        json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        )

    )