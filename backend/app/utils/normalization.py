from typing import List, Tuple


Point = Tuple[float, float]


def normalize_points(points: List[Point], reference_distance: float) -> List[Point]:
    """
    Normalizes point coordinates by a reference body distance
    like shoulder width or hip width.
    """
    if reference_distance == 0:
        return points

    return [(x / reference_distance, y / reference_distance) for x, y in points]


def compute_distance(p1: Point, p2: Point) -> float:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5