EXPECTED_SCHEMA = {
    "timestamp": str,
    "temperature": float,
    "humidity": float,
    "pressure": float
}


def validate_schema(data):

    # Check missing fields
    for field in EXPECTED_SCHEMA:

        if field not in data:
            return False, f"Missing field: {field}"

    # Check datatype mismatches
    for field, expected_type in EXPECTED_SCHEMA.items():

        value = data[field]
        
        if value is None:
            continue

        if not isinstance(value, expected_type):

            # Allow integers where float expected
            if expected_type == float and isinstance(value, int):
                continue

            return False, (
                f"Datatype mismatch for {field}. "
                f"Expected {expected_type.__name__}, "
                f"got {type(value).__name__}"
            )

    # Check unexpected fields
    for field in data:

        if field not in EXPECTED_SCHEMA:
            return False, f"Unexpected field: {field}"

    return True, "Schema valid"