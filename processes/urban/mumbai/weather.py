# processes/urban/mumbai/weather.py

def process_weather(data):

    weather = data.get(
        "weather_forecast",
        []
    )

    if not weather:

        return {

            "status": "NORMAL",

            "message":
            "No weather forecast available."

        }

    w = weather[0]

    forecast = w.get(
        "forecast",
        ""
    ).lower()

    status = "NORMAL"

    if (
        "light rain" in forecast
        or
        "thundershower" in forecast
    ):
        status = "ADVISORY"

    if "heavy rain" in forecast:
        status = "ALERT"

    if "extremely heavy" in forecast:
        status = "CRITICAL"

    return {

        "status": status,

        "message":

        f"{w.get('forecast','').strip()} "

        f"Temperature "

        f"{w.get('min')}°C - "

        f"{w.get('max')}°C.",

        "valid_for":
        w.get("validfor")

    }