import json

SUMMARY_FILE = "data/processed/weather_dashboard_summary.json"
ALERT_FILE = "data/processed/dashboard_alerts.json"
OUTPUT_FILE = "docs/index.html"


def build_card(alert, color):

    areas = alert.get(
        "affected_areas",
        []
    )

    if areas:
        areas = " • ".join(areas)
    else:
        areas = alert.get(
            "area_description",
            "Not Available"
        )

    border = "red"

    if color == "ORANGE":
        border = "orange"

    return f"""

<div class="card" style="border-left:10px solid {border};">

<h2>{alert['state']}</h2>

<h3>⚠️ {alert['event']}</h3>

<p>
<b>Affected Areas</b><br>
{areas}
</p>

<p>
<b>Official Alert</b><br>
{alert['headline']}
</p>

<p>
<b>Official Advisory</b><br>
{alert['instruction']}
</p>

<p>
<b>Valid Until</b><br>
{alert.get('valid_until',alert.get('expires',""))}
</p>

<p>
<b>Active Alerts</b><br>
{alert['alert_count']}
</p>

</div>

"""


def generate_dashboard():

    print()
    print("=" * 60)
    print("GENERATING DASHBOARD")
    print("=" * 60)

    with open(
        SUMMARY_FILE,
        encoding="utf-8"
    ) as f:

        summary = json.load(f)

    with open(
        ALERT_FILE,
        encoding="utf-8"
    ) as f:

        alerts = json.load(f)

    html = """

<html>

<head>

<title>

India Weather Intelligence

</title>

<style>

body{

font-family:Arial,Helvetica,sans-serif;

margin:40px;

background:#f5f5f5;

}

h1{

color:#003366;

}

.summary{

background:#d9edf7;

padding:20px;

border-radius:10px;

margin-bottom:30px;

}

.card{

background:white;

padding:20px;

margin-top:20px;

margin-bottom:20px;

border-radius:10px;

box-shadow:0px 0px 5px #cccccc;

}

.footer{

margin-top:50px;

font-size:14px;

color:gray;

}

</style>

</head>

<body>

<h1>

🇮🇳 India Weather Intelligence

</h1>

<h3>

Business Continuity Platform

</h3>

<hr>

"""

    html += f"""

<div class="summary">

<h2>

Today's National Weather Situation

</h2>

<p>

{summary['national_summary']}

</p>

</div>

"""

    html += """

<h2>

🔴 RED ALERTS

</h2>

"""

    red_found = False

    for alert in alerts:

        if alert["severity"] == "RED":

            red_found = True

            html += build_card(
                alert,
                "RED"
            )

    if not red_found:

        html += """

<p>

No active RED alerts.

</p>

"""

    html += """

<hr>

<h2>

🟠 ORANGE ALERTS

</h2>

"""

    orange_found = False

    for alert in alerts:

        if alert["severity"] == "ORANGE":

            orange_found = True

            html += build_card(
                alert,
                "ORANGE"
            )

    if not orange_found:

        html += """

<p>

No active ORANGE alerts.

</p>

"""

    html += """

<hr>

<div class="footer">

<h3>

Data Sources

</h3>

<ul>

<li>

NDMA Sachet CAP

</li>

<li>

State Disaster Management Authorities

</li>

<li>

India Meteorological Department (Future Integration)

</li>

</ul>

<p>

Dashboard generated automatically from official weather alerts.

</p>

</div>

</body>

</html>

"""

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)

    print()
    print("Dashboard Created")
    print(OUTPUT_FILE)


if __name__ == "__main__":

    generate_dashboard()