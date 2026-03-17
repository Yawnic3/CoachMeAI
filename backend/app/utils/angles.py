import math
from typing import Tuple


Point = Tuple[float, float]


def calculate_angle(a: Point, b: Point, c: Point) -> float:
    """
    Returns the angle ABC in degrees.
    b is the vertex.
    """
    ab = (a[0] - b[0], a[1] - b[1])
    cb = (c[0] - b[0], c[1] - b[1])

    dot = ab[0] * cb[0] + ab[1] * cb[1]
    mag_ab = math.sqrt(ab[0] ** 2 + ab[1] ** 2)
    mag_cb = math.sqrt(cb[0] ** 2 + cb[1] ** 2)

    if mag_ab == 0 or mag_cb == 0:
        return 0.0

    cosine_angle = dot / (mag_ab * mag_cb)
    cosine_angle = max(-1.0, min(1.0, cosine_angle))

    angle = math.degrees(math.acos(cosine_angle))
    return angle


def knee_angle(hip: Point, knee: Point, ankle: Point) -> float:
    return calculate_angle(hip, knee, ankle)


def hip_angle(shoulder: Point, hip: Point, knee: Point) -> float:
    return calculate_angle(shoulder, hip, knee)


def elbow_angle(shoulder: Point, elbow: Point, wrist: Point) -> float:
    return calculate_angle(shoulder, elbow, wrist)