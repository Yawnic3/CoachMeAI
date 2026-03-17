from typing import List


def count_reps_from_signal(values: List[float], threshold: float) -> int:
    """
    Simple rep counting based on threshold crossings.
    Counts a rep when the value drops below threshold and comes back above it.
    """
    if not values:
        return 0

    in_rep = False
    reps = 0

    for value in values:
        if value < threshold and not in_rep:
            in_rep = True
        elif value >= threshold and in_rep:
            reps += 1
            in_rep = False

    return reps