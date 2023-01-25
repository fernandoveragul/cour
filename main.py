import sys
import time
from typing import Generator

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QPushButton, QLabel
from dependencies.get_test import get_json_tests_to_python, get_filtered_list_files
from dependencies.work_with_data import open_test_text, gen_q
from display import mainWindow


class ApplicationData:
    ...


class Application(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.count_answers: list[bool] = []
        self.questions: dict = {}
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(3)

        for btn in get_filtered_list_files():
            btn_ = QtWidgets.QPushButton()
            btn_.setText(btn.upper())
            btn_.setObjectName(f"BTN_{btn.upper().replace(' ', '_')}")
            _btn = f'{btn.replace(" ", "_")}'
            self.questions = get_json_tests_to_python(_btn)
            btn_.clicked.connect(lambda: self.open_test(self.questions))
            self.verticalLayout_3.addWidget(btn_)

    def open_test(self, read_data: dict):
        self.stackedWidget.setCurrentIndex(4)
        questions: list[dict] = list(gen_q(read_data["response"]))
        buttons: list[QPushButton] = [self.btnFirsAnswer, self.btnSecondAnswer, self.btnThirdAnswer, self.btnFourAnswer]
        gen = open_test_text(label=self.lblTextQuestion, buttons=buttons, data=questions)
        self.btnFirsAnswer.clicked.connect(lambda: next(gen))
        self.btnSecondAnswer.clicked.connect(lambda: next(gen))
        self.btnThirdAnswer.clicked.connect(lambda: next(gen))
        self.btnFourAnswer.clicked.connect(lambda: next(gen))


    def add_test(self):
        ...

    def get_question(self):
        ...

    def get_name_executor(self):
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())

