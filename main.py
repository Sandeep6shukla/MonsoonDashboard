from collectors.sachet import fetch_sachet
from processes.process_sachet import process_sachet
from processes.aggregate_alerts import aggregate_alerts
from dashboard.generate_dashboard import generate_dashboard

def main():

    print("="*50)
    print("INDIA BUSINESS CONTINUITY")
    print("="*50)

    fetch_sachet()

    process_sachet()

    aggregate_alerts()

    generate_dashboard()

if __name__=="__main__":
    main()