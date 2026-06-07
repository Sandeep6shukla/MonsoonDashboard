def build_national_cards(alerts):

    red_html = ""

    orange_html = ""

    for alert in alerts:

        severity = alert.get(
            "severity",
            ""
        )

        state = alert.get(
            "state",
            ""
        )

        event = alert.get(
            "event",
            ""
        )

        districts = "<br>".join(

            alert.get(
                "districts",
                []
            )[:10]

        )

        card = f"""

        <div class="alert-card {severity.lower()}">

            <h3>
                {state}
            </h3>

            <p>
                {event}
            </p>

            <details>

                <summary>
                    Affected Areas
                </summary>

                <div>
                    {districts}
                </div>

            </details>

        </div>

        """

        if severity == "RED":

            red_html += card

        elif severity == "ORANGE":

            orange_html += card

    return f"""

    <section>

        <h2>
            🔴 Red Alerts
        </h2>

        <div class="card-grid">

            {red_html}

        </div>

    </section>

    <section>

        <h2>
            🟠 Orange Alerts
        </h2>

        <div class="card-grid">

            {orange_html}

        </div>

    </section>

    """