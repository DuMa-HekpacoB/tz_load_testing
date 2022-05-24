import json
import os
import sys
from typing import Tuple


def parse_args() -> Tuple[str, str]:
    tests_json = sys.argv[1]
    values_json = sys.argv[2]
    return tests_json, values_json


def parse_file(tests_json: str, values_json: str) -> Tuple[dict, dict]:
    dir_for_tests = os.path.join(os.getcwd(), "task3", tests_json)
    with open(dir_for_tests, "r") as fp:
        data_tests = json.load(fp)
    dir_for_values = os.path.join(os.getcwd(), "task3", values_json)
    with open(dir_for_values, "r") as fp:
        data_values = json.load(fp)
    return data_tests, data_values


def recursive_going_in_tree(dict_id: dict, node: dict) -> None:
    node["value"] = dict_id.get(node["id"], "")
    for i_node in node.get("values", []):
        recursive_going_in_tree(dict_id, i_node)


def main() -> None:
    first_file, second_file = parse_args()
    data_tests, data_values = parse_file(first_file, second_file)
    dict_id = {}
    for i_dict in data_values["values"]:
        key = i_dict["id"]
        value = i_dict["value"]
        dict_id[key] = value
    for i_node in data_tests.get("tests", []):
        recursive_going_in_tree(dict_id, i_node)
    with open(os.path.join(os.getcwd(), "task3", "report.json"), 'w') as fjson:
        json.dump(data_tests, fjson, indent=4)


if __name__ == "__main__":
    main()
