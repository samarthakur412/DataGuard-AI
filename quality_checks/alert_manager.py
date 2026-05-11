from datetime import datetime


def send_alert(alert_type, severity, message):

    timestamp = datetime.now()

    alert = {
        "timestamp": str(timestamp),
        "alert_type": alert_type,
        "severity": severity,
        "message": message
    }

    print("\n" + "=" * 60)
    print("ALERT GENERATED")
    print("=" * 60)

    print(f"Timestamp : {alert['timestamp']}")
    print(f"Type      : {alert['alert_type']}")
    print(f"Severity  : {alert['severity']}")
    print(f"Message   : {alert['message']}")

    print("=" * 60 + "\n")