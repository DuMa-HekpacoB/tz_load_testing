from typing import Tuple
import sys


def arg_parse() -> Tuple[int, int]:
    try:
        global n, m
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    except IndexError as e:
        print(e, "Нехватает аргумента!")
    except ValueError as e:
        print(e, "Ввели некорректное значение!")
    if (m > n):
        raise ValueError("Первый аргумент должен быть больше второго!")
    return n, m


def task_1(n: int, m: int) -> str:
    our_massive = [_ for _ in range(1, n + 1)]
    current_array = our_massive[:m]
    result = str(current_array[0])
    while current_array[-1] != 1:
        our_massive.extend(current_array[:-1])
        our_massive = our_massive[m-1:]
        current_array = our_massive[:m]
        result += str(current_array[0])
    return result


def main() -> None:
    n, m = arg_parse()
    print(task_1(n, m))


if __name__ == "__main__":
    main()
