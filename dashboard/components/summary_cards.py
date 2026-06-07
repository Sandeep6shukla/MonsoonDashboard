def build_summary_cards(briefing):

    red_items = ""

    for item in briefing.get(
        "red_summary",
        []
    ):

        red_items += f"<li>{item}</li>"

    orange_items = ""

    for item in briefing.get(
        "orange_summary",
        []
    ):

        orange_items += f"<li>{item}</li>"

    return f"""

    <div class="summary-grid">

        <div class="summary-card red-summary">

            <h2>
                🔴 Red Alert Summary
            </h2>

            <ul>
                {red_items}
            </ul>

        </div>

        <div class="summary-card orange-summary">

            <h2>
                🟠 Orange Alert Summary
            </h2>

            <ul>
                {orange_items}
            </ul>

        </div>

    </div>

    """