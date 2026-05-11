from datetime import datetime

event_timestamps = []

MAX_EVENTS_PER_MINUTE = 20


def check_volume():

    global event_timestamps

    current_time = datetime.now()

    # Keep only last 60 seconds
    event_timestamps = [
        ts for ts in event_timestamps
        if (current_time - ts).total_seconds() < 60
    ]

    # Add current event timestamp
    event_timestamps.append(current_time)

    current_volume = len(event_timestamps)

    if current_volume > MAX_EVENTS_PER_MINUTE:

        return (
            False,
            f"Volume spike detected: {current_volume} events/minute",
            current_volume
        )

    return (
        True,
        f"Current volume normal: {current_volume} events/minute",
        current_volume
    )