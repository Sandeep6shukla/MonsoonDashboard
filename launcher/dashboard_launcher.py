import tkinter as tk
import subprocess
import webbrowser
import os

PROJECT = r"C:\Projects\IndiaWeatherIntelligence"

LIVE_URL = "https://sandeep6shukla.github.io/MonsoonDashboard/"


def update_dashboard():

    status.config(
        text="Updating dashboard..."
    )

    root.update()

    try:

        subprocess.run(

            "uv run python main.py",

            cwd=PROJECT,

            shell=True,

            check=True

        )

        subprocess.run(

            "git add .",

            cwd=PROJECT,

            shell=True

        )

        subprocess.run(

            'git commit -m "Dashboard update"',

            cwd=PROJECT,

            shell=True

        )

        subprocess.run(

            "git push",

            cwd=PROJECT,

            shell=True

        )

        status.config(

            text="Dashboard Updated!"

        )

    except:

        status.config(

            text="Update Failed"

        )


def open_dashboard():

    webbrowser.open(

        LIVE_URL

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

    "400x300"

)

title = tk.Label(

    root,

    text="🇮🇳 India Business Continuity",

    font=("Arial",16)

)

title.pack(

    pady=20

)

tk.Button(

    root,

    text="Update Dashboard",

    width=25,

    command=update_dashboard

).pack(

    pady=5

)

tk.Button(

    root,

    text="Open Live Dashboard",

    width=25,

    command=open_dashboard

).pack(

    pady=5

)

tk.Button(

    root,

    text="Open Project Folder",

    width=25,

    command=open_project

).pack(

    pady=5

)

tk.Button(

    root,

    text="Exit",

    width=25,

    command=root.destroy

).pack(

    pady=5

)

status = tk.Label(

    root,

    text="Ready",

    font=("Arial",10)

)

status.pack(

    pady=20

)

root.mainloop()