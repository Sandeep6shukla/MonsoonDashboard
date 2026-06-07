from datetime import datetime


def build_header():

    return f"""
    <header class="header">

        <div>

            <h1>
                India Weather Intelligence
            </h1>

            <div class="updated-time">
                Last Updated:
                {datetime.now().strftime("%d-%b-%Y %H:%M IST")}
            </div>

        </div>

        <div>

            <button
                onclick="toggleTheme()"
                class="theme-btn"
            >
                🌙
            </button>

        </div>

    </header>

    <div class="tabs">

        <button
            class="tab-button active"
            onclick="showTab('national')"
        >
            National
        </button>

        <button
            class="tab-button"
            onclick="showTab('urban')"
        >
            Urban
        </button>

    </div>
    """