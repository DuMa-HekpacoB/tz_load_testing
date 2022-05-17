import sys
import os


def parse_args():
    massive_file = sys.argv[1]
    return massive_file


def main():
    file = os.path.join(os.getcwd(), "task4", parse_args())
    array: list = []
    with open(file, "r") as f_txt:
        for i_row in f_txt:
            array.append(int(i_row))
    if len(array) == 0:
        raise Exception("Незаполненный файл")
    average = sum(array) // len(array)
    count = 0
    for item in array:
        count += abs(average - item)
    print(count)


if __name__ == "__main__":
    main()
