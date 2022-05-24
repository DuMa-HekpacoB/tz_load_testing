import sys
import os


def parse_args() -> str:
    massive_file = sys.argv[1]
    return massive_file


def main() -> None:
    file = os.path.join(os.getcwd(), "task4", parse_args())
    array: list = []
    with open(file, "r") as f_txt:
        for i_row in f_txt:
            array.append(int(i_row))
    if len(array) == 0:
        raise Exception("Незаполненный файл")
    average_array = sorted(array)[len(array) // 2]
    count = sum([abs(item - average_array) for item in array])
    print(count)


if __name__ == "__main__":
    main()
