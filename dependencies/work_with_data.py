from PyQt6.QtWidgets import QLabel, QPushButton

from dependencies.get_test import get_path, get_test


def gen_q(questions: list[dict]):
    for q in questions:
        yield q


def open_test_text(*, label: QLabel, buttons: list[QPushButton], data: list[dict]):
    for ind_dt, dt in enumerate(data):
        label.setText(dt.get("text"))
        for ind, btn in enumerate(buttons):
            btn.setText(dt.get("answers")[ind].get("answer"))
        yield dt


def filtered_answers(d: list[dict]):
    for val in d:
        if val.get("mass"):
            return val.get("answer")
    return "Ответ"


def load_default_test():
    path_from_read: str = get_path("display\\origin_files")
    return get_test(f'{path_from_read}origin_schema.json')
