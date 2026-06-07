from collectors.national.sachet import fetch_sachet
from collectors.national.cap_collector import collect_cap

from processes.national.normalize_geography import normalize_geography

# Existing business pipeline
from processes.national.process_cap import process_cap
from processes.legacy.aggregate_states import aggregate_states
from processes.legacy.build_summary import build_summary

# New weather pipeline
from processes.national.aggregate_weather import aggregate_weather
from processes.national.build_dashboard_alerts import build_dashboard_alerts
from processes.national.build_weather_summary import build_weather_summary

from dashboard.generate_dashboard import generate_dashboard


def main():

    print("=" * 60)
    print("INDIA WEATHER INTELLIGENCE PLATFORM")
    print("=" * 60)

    print()
    print("STEP 1 : Fetch Sachet RSS")
    fetch_sachet()

    print()
    print("STEP 2 : Collect CAP Alerts")
    collect_cap()

    print()
    print("STEP 3 : Normalize Geography")
    normalize_geography()

    # Keep existing pipeline
    print()
    print("STEP 4 : Business Processing")
    process_cap()

    print()
    print("STEP 5 : Aggregate States")
    aggregate_states()

    print()
    print("STEP 6 : Build Business Summary")
    build_summary()

    # New weather pipeline
    print()
    print("STEP 7 : Aggregate Weather")
    aggregate_weather()

    print()
    print("STEP 8 : Build Dashboard Alerts")
    build_dashboard_alerts()

    print()
    print("STEP 9 : Build Weather Summary")
    build_weather_summary()

    print()
    print("STEP 10 : Generate Dashboard")
    generate_dashboard()

    print()
    print("=" * 60)
    print("PIPELINE COMPLETED")
    print("=" * 60)
    print()
    print("Dashboard:")
    print("docs/index.html")
    print()
    print("GitHub Pages:")
    print("https://sandeep6shukla.github.io/MonsoonDashboard/")


if __name__ == "__main__":

    main()