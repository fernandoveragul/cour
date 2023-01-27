import os
import sys
import json


def get_filtered_list_files() -> list[str]:
    files: list[str] = os.listdir(f'{os.path.dirname(sys.argv[0])}\\tests\\')
    return list(map(lambda file: file.split(".")[0].replace("_", " "), files))[1:]


def get_test(path_file: str) -> dict[str, list[dict[str, int | str | list[str, bool]]]]:
    with open(path_file, "r") as test:
        test_json: dict = json.loads(test.read())
    return test_json


def get_last_test_name() -> str:
    try:
        number: str = get_filtered_list_files()[-1].split()[-1]
    except Exception:
        number = "0"
    return str(int(number) + 1)


def get_path(path: str) -> str:
    return f"{os.path.dirname(sys.argv[0])}\\{path}\\"


def get_json_tests_to_python(file_name: str) -> dict | None:
    file_name_ = file_name.replace(" ", "_") + ".json"
    path: str = get_path("tests")
    return get_test(path + file_name_) if file_name else None


def post_python_to_json_test(write_data: list, number_var: str):
    path_to_write: str = get_path("tests")
    nv = get_last_test_name()
    with open(f"{path_to_write}Вариант_{number_var if number_var else nv}.json", "w") as file:
        file.write(json.dumps(write_data, indent=4))
