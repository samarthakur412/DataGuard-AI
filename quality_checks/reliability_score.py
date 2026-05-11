def calculate_reliability_score(
    schema_valid,
    null_percentage,
    freshness_delay,
    volume_normal
):

    score = 100

    # Schema penalty
    if not schema_valid:
        score -= 40

    # Null penalty
    score -= min(null_percentage * 2, 30)

    # Freshness penalty
    if freshness_delay > 30:
        score -= 20

    # Volume anomaly penalty
    if not volume_normal:
        score -= 10

    return max(score, 0)