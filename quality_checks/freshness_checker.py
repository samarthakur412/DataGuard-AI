from datetime import datetime

FRESHNESS_THRESHOLD_SECONDS = 30


def check_freshness(data):

    event_time = datetime.strptime(
        data["timestamp"],
        "%Y-%m-%d %H:%M:%S.%f"
    )

    current_time = datetime.now()

    delay = (current_time - event_time).total_seconds()

    if delay > FRESHNESS_THRESHOLD_SECONDS:

        return (
            False,
            f"Stale data detected. Delay: {delay:.2f} seconds",
            delay
        )

    return (
        True,
        f"Fresh data. Delay: {delay:.2f} seconds",
        delay
    )