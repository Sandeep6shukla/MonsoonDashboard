import json
from datetime import datetime

EXECUTIVE_FILE = "data/processed/executive_summary.json"
STATE_FILE = "data/processed/state_summary.json"

OUTPUT_FILE = "docs/index.html"


STATUS_ICON = {
    "CRITICAL": "🔴",
    "ELEVATED": "🟠",
    "WATCH": "🟡",
    "NORMAL": "🟢"
}

SEVERITY_ICON = {
    "RED": "🔴",
    "ORANGE": "🟠",
    "WATCH": "🟡",
    "INFO": "🟢"
}


def generate_dashboard():

    print()
    print("=" * 50)
    print("GENERATING DASHBOARD")
    print("=" * 50)

    with open(
        EXECUTIVE_FILE,
        encoding="utf-8"
    ) as f:

        executive = json.load(f)

    with open(
        STATE_FILE,
        encoding="utf-8"
    ) as f:

        states = json.load(f)

    timestamp = datetime.now().strftime(
        "%d %b %Y %H:%M"
    )

    html = f"""

<html>

<head>

<title>

India Business Continuity Dashboard

</title>

<style>

body{{
font-family:Arial;
margin:30px;
background:#f4f4f4;
}}

.card{{
background:white;
padding:15px;
margin:10px;
border-radius:8px;
box-shadow:2px 2px 5px #ccc;
}}

table{{
border-collapse:collapse;
width:100%;
background:white;
}}

th,td{{
border:1px solid #ddd;
padding:8px;
text-align:left;
}}

th{{
background:#eee;
}}

ul{{
margin-top:5px;
}}

</style>

</head>

<body>

<div class="card">

<h1>

🇮🇳 INDIA BUSINESS CONTINUITY

</h1>

<h3>

National Weather Intelligence Dashboard

</h3>

<p>

Assessment Time :
{timestamp} IST

</p>

</div>

<div class="card">

<h2>

{STATUS_ICON.get(
executive["overall_status"],
"⚪"
)}

Overall Status :

{executive["overall_status"]}

</h2>

<p>

{executive["todays_assessment"]}

</p>

</div>

<div class="card">

<h2>

🔴 Critical States

</h2>

<ul>

"""

    for state in executive["critical_states"]:

        html += f"<li>{state}</li>"

    html += "</ul>"

    html += """

<h2>

🟠 High Risk States

</h2>

<ul>

"""

    for state in executive["high_risk_states"]:

        html += f"<li>{state}</li>"

    html += "</ul>"

    html += """

<h2>

🟡 Watch States

</h2>

<ul>

"""

    for state in executive["watch_states"]:

        html += f"<li>{state}</li>"

    html += """

</ul>

</div>

"""

    html += """

<div class="card">

<h2>

Top Business Risks

</h2>

<ul>

"""

    for risk in executive["top_business_risks"]:

        if risk in [
            "General Weather",
            "Weather Watch"
        ]:
            continue

        html += f"<li>{risk}</li>"

    html += """

</ul>

</div>

"""

    html += """

<div class="card">

<h2>

Recommended Actions

</h2>

<ul>

"""

    for action in executive["recommended_actions"]:

        if action == "Continue monitoring.":
            continue

        html += f"<li>{action}</li>"

    html += """

</ul>

</div>

"""

    html += """

<div class="card">

<h2>

State Risk Matrix

</h2>

<table>

<tr>

<th>State</th>

<th>Severity</th>

<th>Priority</th>

<th>Alerts</th>

<th>Business Risks</th>

</tr>

"""

    for state in states:

        html += f"""

<tr>

<td>

{state["state"]}

</td>

<td>

{SEVERITY_ICON.get(
state["highest_severity"],
"⚪"
)}

{state["highest_severity"]}

</td>

<td>

{state["business_priority"]}

</td>

<td>

{state["alert_count"]}

</td>

<td>

{", ".join(
state["business_categories"]
)}

</td>

</tr>

"""

    html += """

</table>

</div>

"""

    html += """

<div class="card">

<h2>

Detailed State Summary

</h2>

"""

    for state in states:

        html += f"""

<hr>

<h3>

{SEVERITY_ICON.get(
state["highest_severity"],
"⚪"
)}

{state["state"]}

</h3>

<p>

Highest Severity :

{state["highest_severity"]}

</p>

<p>

Business Priority :

{state["business_priority"]}

</p>

<p>

Active Alerts :

{state["alert_count"]}

</p>

<p>

Business Risks :

{", ".join(
state["business_categories"]
)}

</p>

<p>

Recommended Actions :

</p>

<ul>

"""

        for action in state["recommended_actions"]:

            html += f"<li>{action}</li>"

        html += "</ul>"

    html += """

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