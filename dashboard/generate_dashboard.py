import json

from dashboard.components.header import build_header
from dashboard.components.summary_cards import build_summary_cards
from dashboard.components.national_cards import build_national_cards
from dashboard.components.urban_cards import build_urban_cards
from dashboard.components.health_strip import build_health_strip
from dashboard.components.footer import build_footer


NATIONAL_ALERTS_FILE = (
    "data/processed/national_dashboard.json"
)

NATIONAL_BRIEFING_FILE = (
    "data/processed/national_briefing.json"
)

MUMBAI_FILE = (
    "data/processed/mumbai_summary.json"
)

OUTPUT_FILE = "docs/index.html"


def load_json(path):

    with open(
        path,
        encoding="utf-8"
    ) as f:

        return json.load(f)


def generate_dashboard():

    print()
    print("=" * 60)
    print("GENERATING DASHBOARD")
    print("=" * 60)

    alerts = load_json(
        NATIONAL_ALERTS_FILE
    )

    briefing = load_json(
        NATIONAL_BRIEFING_FILE
    )

    mumbai = load_json(
        MUMBAI_FILE
    )

    html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="utf-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>
India Weather Intelligence
</title>

<style>

:root {{

    --bg:#f8fafc;
    --card:#ffffff;
    --text:#0f172a;
    --border:#e2e8f0;

}}

body.dark {{

    --bg:#0f172a;
    --card:#1e293b;
    --text:#f8fafc;
    --border:#334155;

}}

body {{

    margin:0;
    padding:20px;

    background:var(--bg);

    color:var(--text);

    font-family:
    Segoe UI,
    Arial,
    sans-serif;

}}

.header {{

    display:flex;

    justify-content:space-between;

    align-items:center;

    margin-bottom:20px;

}}

.updated-time {{

    color:#64748b;

    font-size:14px;

}}

.theme-btn {{

    border:none;

    cursor:pointer;

    font-size:20px;

    background:none;

}}

.tabs {{

    display:flex;

    gap:10px;

    margin-bottom:20px;

}}

.tab-button {{

    border:none;

    padding:10px 16px;

    border-radius:8px;

    cursor:pointer;

}}

.tab-button.active {{

    font-weight:bold;

}}

.tab-content {{

    display:none;

}}

.tab-content.active {{

    display:block;

}}

.summary-grid {{

    display:grid;

    grid-template-columns:
    repeat(auto-fit,minmax(450px,1fr));

    gap:16px;

    margin-bottom:25px;

}}

.summary-card {{

    background:var(--card);

    border-radius:12px;

    padding:20px;

}}

.red-summary {{

    border-left:8px solid #dc2626;

}}

.orange-summary {{

    border-left:8px solid #ea580c;

}}

.card-grid {{

    display:grid;

    grid-template-columns:
    repeat(auto-fit,minmax(350px,1fr));

    gap:16px;

    margin-bottom:25px;

}}

.alert-card {{

    background:var(--card);

    border-radius:12px;

    padding:16px;

}}

.alert-card.red {{

    border-left:8px solid #dc2626;

}}

.alert-card.orange {{

    border-left:8px solid #ea580c;

}}

.urban-card {{

    background:var(--card);

    border-radius:12px;

    padding:16px;

}}

.city-tab {{

    padding:8px 14px;

    margin-right:10px;

    border:none;

    border-radius:8px;

}}

details {{

    margin-top:10px;

}}

h1,h2,h3 {{

    margin-top:0;

}}

footer {{

    margin-top:30px;

    color:#64748b;

}}

.health-strip {{

    display:grid;

    grid-template-columns:
    repeat(auto-fit,minmax(180px,1fr));

    gap:12px;

    margin-bottom:20px;

}}

.health-strip div {{

    background:var(--card);

    padding:14px;

    border-radius:12px;

    text-align:center;

    box-shadow:
    0 1px 3px rgba(0,0,0,0.08);

}}

.health-strip strong {{

    display:block;

    margin-top:8px;

    font-size:20px;

}}

.source-card {{

    background:var(--card);

    border-radius:12px;

    padding:20px;

    max-width:500px;

    margin:auto;

    text-align:left;

}}

.source-card ul {{

    margin:0;

    padding-left:20px;

}}

.source-card li {{

    margin-bottom:8px;

}}

a {{

    color:#2563eb;

    text-decoration:none;

}}

a:hover {{

    text-decoration:underline;

}}

</style>

</head>

<body>

{build_header()}
{build_health_strip(
    alerts,
    briefing
)}

<div
    id="national"
    class="tab-content active"
>

{build_summary_cards(briefing)}

{build_national_cards(alerts)}

</div>

<div
    id="urban"
    class="tab-content"
>

{build_urban_cards(mumbai)}

</div>

{build_footer()}

<script>

function showTab(tabId) {{

    document
        .querySelectorAll(
            '.tab-content'
        )
        .forEach(
            tab =>
            tab.classList.remove(
                'active'
            )
        );

    document
        .getElementById(
            tabId
        )
        .classList.add(
            'active'
        );

}}

function toggleTheme() {{

    document.body
        .classList.toggle(
            'dark'
        );

}}

</script>

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
    print("Dashboard Generated")
    print(OUTPUT_FILE)
    print()


if __name__ == "__main__":

    generate_dashboard()