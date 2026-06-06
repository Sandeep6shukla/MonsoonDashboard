from collectors.sachet import fetch_sachet

from collectors.cap_collector import collect_cap

from processes.normalize_geography import normalize_geography

from processes.process_cap import process_cap

from processes.aggregate_states import aggregate_states

from processes.build_summary import build_summary

from dashboard.generate_dashboard import generate_dashboard


def main():

    print()

    print("=" * 60)
    print("INDIA BUSINESS CONTINUITY PLATFORM")
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

    print()
    print("STEP 4 : Business Processing")
    process_cap()

    print()
    print("STEP 5 : Aggregate States")
    aggregate_states()

    print()
    print("STEP 6 : Build Executive Summary")
    build_summary()

    print()
    print("STEP 7 : Generate Dashboard")
    generate_dashboard()

    print()

    print("=" * 60)
    print("PIPELINE COMPLETED")
    print("=" * 60)

    print()

    print("Dashboard :")
    print("docs/index.html")

    print()

    print("GitHub Pages:")
    print(
        "https://sandeep6shukla.github.io/MonsoonDashboard/"
    )

    print()


if __name__ == "__main__":

    main()