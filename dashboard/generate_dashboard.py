import json
import os
from datetime import datetime

INPUT_FILE = "data/processed/state_summary.json"
OUTPUT_FILE = "outputs/dashboard.html"


def create_state_card(alert):

    return f"""
    <div class="card">

    <h3>{alert['state']}</h3>

    <p><b>Government Alerts:</b> {alert['government_alerts']}</p>

    <p><b>Primary Risk:</b><br>
    {alert['primary_risk']}</p>

    <p><b>Recommended Action:</b>
    {alert['action']}</p>

    </div>
    """


def generate_dashboard():

    with open(INPUT_FILE, encoding="utf-8") as f:
        alerts = json.load(f)

    red = [a for a in alerts if a["severity"] == "RED"]
    orange = [a for a in alerts if a["severity"] == "ORANGE"]
    watch = [a for a in alerts if a["severity"] == "WATCH"]
    info = [a for a in alerts if a["severity"] == "INFO"]

    # Overall Status

    if len(red) > 0:
        overall = "🔴 CRITICAL"

    elif len(orange) > 0:
        overall = "🟠 ELEVATED"

    elif len(watch) > 0:
        overall = "🟡 WATCH"

    else:
        overall = "🟢 NORMAL"

    assessment = datetime.now().strftime(
        "%d %b %Y %H:%M"
    )

    html = f"""
<html>

<head>

<title>
India Business Continuity Weather Intelligence
</title>

<style>

body {{

font-family: Arial, Helvetica, sans-serif;
margin: 30px;
background-color: #f5f5f5;

}}

.card {{

background: white;
padding: 15px;
margin-bottom: 15px;
border-radius: 10px;
box-shadow: 2px 2px 5px lightgray;

}}

.section {{

margin-top:30px;

}}

.summary {{

background:white;
padding:20px;
border-radius:10px;
box-shadow:2px 2px 5px lightgray;

}}

h1 {{

color:#003366;

}}

h2 {{

color:#003366;

}}

</style>

</head>

<body>

<h1>
India Business Continuity Weather Intelligence
</h1>

<hr>

<div class="summary">

<h2>Assessment Time</h2>

<p>
{assessment} IST
</p>

<h2>Overall Business Status</h2>

<h2>
{overall}
</h2>

<hr>

<h2>Executive Summary</h2>

<p>
🔴 Critical States : {len(red)}
</p>

<p>
🟠 High Risk States : {len(orange)}
</p>

<p>
🟡 Monitoring States : {len(watch)}
</p>

<p>
🟢 Normal States : {len(info)}
</p>

</div>

<div class="section">

<h2>
🔴 States Requiring Action
</h2>

"""

    if len(red) == 0:

        html += """
        <div class="card">
        No Critical States
        </div>
        """

    else:

        for alert in red:
            html += create_state_card(alert)

    html += """

</div>

<div class="section">

<h2>
🟠 States Under Close Watch
</h2>

"""

    if len(orange) == 0:

        html += """
        <div class="card">
        No High Risk States
        </div>
        """

    else:

        for alert in orange:
            html += create_state_card(alert)

    html += """

</div>

<div class="section">

<h2>
🟡 Monitoring States
</h2>

"""

    if len(watch) == 0:

        html += """
        <div class="card">
        No Monitoring States
        </div>
        """

    else:

        for alert in watch:
            html += create_state_card(alert)

    html += """

</div>

<hr>

<p>

Generated automatically from Government Alert Sources.

</p>

<p>

Prototype Version 1.0

</p>

</body>

</html>

"""

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)

    print()
    print("=" * 50)
    print("Dashboard Generated Successfully")
    print("=" * 50)
    print(OUTPUT_FILE)