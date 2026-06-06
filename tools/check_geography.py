import json

INPUT="data/processed/geography_alerts.json"

with open(
    INPUT,
    encoding="utf-8"
) as f:

    alerts=json.load(f)

print()

print("="*50)
print("GEOGRAPHY COVERAGE")
print("="*50)

total=len(alerts)

states=0

districts=0

for alert in alerts:

    if alert.get(
        "affected_states"
    ):

        states+=1

    if alert.get(
        "affected_districts"
    ):

        districts+=1

print()

print(
    "Total Alerts:",
    total
)

print(
    "State Coverage:",
    states
)

print(
    "District Coverage:",
    districts
)

print()

print(
    "State %",
    round(
        states*100/total,
        2
    )
)

print(
    "District %",
    round(
        districts*100/total,
        2
    )
)