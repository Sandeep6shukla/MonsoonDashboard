def build_health_strip(
    alerts,
    briefing
):

    red_count = len([

        alert

        for alert in alerts

        if alert.get(
            "severity"
        ) == "RED"

    ])

    orange_count = len([

        alert

        for alert in alerts

        if alert.get(
            "severity"
        ) == "ORANGE"

    ])

    state_count = len(

        briefing.get(
            "states",
            []
        )

    )

    return f"""

    <div class="health-strip">

        <div>
            🔴 Red Alerts
            <strong>{red_count}</strong>
        </div>

        <div>
            🟠 Orange Alerts
            <strong>{orange_count}</strong>
        </div>

        <div>
            🗺 States
            <strong>{state_count}</strong>
        </div>

        <div>
            🏙 Urban Areas
            <strong>1</strong>
        </div>

        <div>
            📡 Sources
            <strong>2</strong>
        </div>

    </div>

    """