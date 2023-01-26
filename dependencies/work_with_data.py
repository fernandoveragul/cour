from PyQt6.QtWidgets import QLabel, QPushButton


def gen_q(questions: list[dict]):
    for q in questions:
        yield q


def open_test_text(*, label: QLabel, buttons: list[QPushButton], data: list[dict]):
    for ind_dt, dt in enumerate(data):
        label.setText(dt.get("text"))
        for ind, btn in enumerate(buttons):
            btn.setText(dt.get("answers")[ind].get("answer"))
        yield dt

