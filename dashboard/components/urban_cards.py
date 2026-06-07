def build_urban_cards(mumbai):

    return f"""

    <div class="urban-tabs">

        <button class="city-tab active">
            Mumbai
        </button>

        <button class="city-tab">
            Delhi
        </button>

        <button class="city-tab">
            Chennai
        </button>

        <button class="city-tab">
            Bengaluru
        </button>

    </div>

    <div class="card-grid">

        <div class="urban-card">

            <h3>
                🌦 Weather
            </h3>

            <p>
                {mumbai["weather"]["message"]}
            </p>

        </div>

        <div class="urban-card">

            <h3>
                ⚠ Warnings
            </h3>

            <p>
                {mumbai["warnings"]["message"]}
            </p>

        </div>

        <div class="urban-card">

            <h3>
                🌊 High Tide
            </h3>

            <p>
                {mumbai["high_tide"]["message"]}
            </p>

        </div>

        <div class="urban-card">

            <h3>
                🚦 Traffic
            </h3>

            <p>
                {mumbai["traffic"]["message"]}
            </p>

        </div>

        <div class="urban-card">

            <h3>
                🌧 Flood Monitoring
            </h3>

            <p>
                {mumbai["flooding"]["message"]}
            </p>

        </div>

        <div class="urban-card">

            <h3>
                💼 Business Impact
            </h3>

            <p>
                {mumbai["business_implication"]}
            </p>

        </div>

    </div>

    """