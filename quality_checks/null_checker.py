NULL_THRESHOLD = 20  # percent


def check_nulls(data):

    total_fields = len(data)

    null_count = 0

    for value in data.values():

        if value is None:
            null_count += 1

    null_percentage = (null_count / total_fields) * 100

    if null_percentage > NULL_THRESHOLD:

        return (
            False,
            f"High null percentage detected: {null_percentage:.2f}%",
            null_percentage
        )

    return (
        True,
        f"Null percentage acceptable: {null_percentage:.2f}%",
        null_percentage
    )