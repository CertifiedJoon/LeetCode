from math import sqrt


def get_k_closest_points_from_origin(
    points: list[list[int]], k: int
) -> list[list[int]]:
    # calculate distance from origin
    def get_distance_from_origin(point: list[list[int]]):
        return sqrt(point[0] ** 2 + point[1] ** 2)

    # prepare variables for quick select
    lo, hi = 0, len(points) - 1

    while lo < hi:
        pivot = lo
        sample = points[lo]
        i = lo
        while i <= hi:
            if get_distance_from_origin(points[i]) < get_distance_from_origin(sample):
                points[pivot], points[i] = points[i], points[pivot]
                pivot += 1
            i += 1
        if pivot < k:
            lo = pivot
        elif pivot > k:
            hi = pivot - 1
        else:
            return points[:k]


print(get_k_closest_points_from_origin([[3, 3], [5, -1], [-2, 4]], 2))
