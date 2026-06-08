import tkinter as tk
import subprocess
import webbrowser
import os
from datetime import datetime

PROJECT = r"C:\Projects\IndiaWeatherIntelligence"

LIVE_URL = (
    "https://sandeep6shukla.github.io/MonsoonDashboard/"
)


def update_dashboard():

    status.config(
        text="Collecting and processing data..."
    )

    root.update()

    try:

        subprocess.run(
            "uv run python run_dashboard.py",
            cwd=PROJECT,
            shell=True,
            check=True
        )

        status.config(
            text="Publishing to GitHub..."
        )

        root.update()

        subprocess.run(
            "git add .",
            cwd=PROJECT,
            shell=True,
            check=True
        )

        subprocess.run(
            'git commit -m "Dashboard update"',
            cwd=PROJECT,
            shell=True
        )

        subprocess.run(
            "git push",
            cwd=PROJECT,
            shell=True,
            check=True
        )

        status.config(
            text="Dashboard Published Successfully"
        )

    except Exception as e:

        status.config(
            text=f"Failed: {str(e)}"
        )


def open_dashboard():

    timestamp = int(
        datetime.now().timestamp()
    )

    webbrowser.open(
        f"{LIVE_URL}?v={timestamp}"
    )


def open_project():

    os.startfile(
        PROJECT
    )


root = tk.Tk()

root.title(
    "India Business Continuity"
)

root.geometry(
    "450x320"
)

title = tk.Label(
    root,
    text="🇮🇳 India Business Continuity",
    font=("Arial", 16, "bold")
)

title.pack(
    pady=20
)

tk.Button(
    root,
    text="Update Dashboard",
    width=30,
    command=update_dashboard
).pack(
    pady=5
)

tk.Button(
    root,
    text="Open Live Dashboard",
    width=30,
    command=open_dashboard
).pack(
    pady=5
)

tk.Button(
    root,
    text="Open Project Folder",
    width=30,
    command=open_project
).pack(
    pady=5
)

tk.Button(
    root,
    text="Exit",
    width=30,
    command=root.destroy
).pack(
    pady=5
)

status = tk.Label(
    root,
    text="Ready",
    font=("Arial", 10)
)

status.pack(
    pady=20
)

root.mainloop()