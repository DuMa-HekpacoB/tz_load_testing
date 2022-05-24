import os
import sys
from math import sqrt
from typing import Tuple


def parse_args() -> Tuple[str, str]:
    file_radius_and_center = sys.argv[1]
    file_points = sys.argv[2]
    return file_radius_and_center, file_points


def get_args(first_file: str) -> list:
    f_file = os.path.join(os.getcwd(), "task2", first_file)
    with open(f_file, "r") as f_f:
        central_point = f_f.readline()
        central_point = list(map(lambda x: float(x), central_point.strip().split(" ")))
        radius = f_f.readline()
        central_point.append(float(radius))
        return central_point


def get_point(second_file: str) -> tuple:
    s_file = os.path.join(os.getcwd(), "task2", second_file)
    list_points = []
    with open(s_file, "r") as s_f:
        for points in s_f:
            points = tuple(map(lambda x: float(x), points.strip().split(" ")))
            list_points.append(points)
    return list_points


def main() -> None:
    first_file, second_file = parse_args()
    point_a, point_b, radius = get_args(first_file=first_file)
    list_points = get_point(second_file=second_file)
    for x, y in list_points:
        result = sqrt((x - point_a) ** 2 + (y - point_b) ** 2)
        if result < radius:
            print(0)
        elif result == radius:
            print(1)
        else:
            print(2)


if __name__ == "__main__":
    main()
