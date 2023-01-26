import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QPushButton

from dependencies.get_test import get_json_tests_to_python, get_filtered_list_files
from dependencies.work_with_data import gen_q, open_test_text
from display import mainWindow, testsWindow


class Tests(QtWidgets.QWidget, testsWindow.Ui_Form):
    def __init__(self, read_data: dict):
        super().__init__()
        self.setupUi(self)

        self.count_answers = []

        questions: list[dict] = list(gen_q(read_data["response"]))
        buttons: list[QPushButton] = [self.btnFirsAnswer, self.btnSecondAnswer, self.btnThirdAnswer, self.btnFourAnswer]
        gen = open_test_text(label=self.lblTextQuestion, buttons=buttons, data=questions)
        for btn in buttons:
            btn.setCheckable(True)
        self.btnFirsAnswer.clicked.connect(lambda: self.is_end(next(gen, False), buttons))
        self.btnSecondAnswer.clicked.connect(lambda: self.is_end(next(gen, False), buttons))
        self.btnThirdAnswer.clicked.connect(lambda: self.is_end(next(gen, False), buttons))
        self.btnFourAnswer.clicked.connect(lambda: self.is_end(next(gen, False), buttons))

    def is_end(self, data: bool | dict, buttons: list[QPushButton]):
        if data is False:
            self.__message_with_results(self.count_answers)
            self.close()
        else:
            match data:
                case _:
                    for ind, btn in enumerate(buttons):
                        if btn.isChecked():
                            btn.setChecked(False)
                            self.count_answers.append(data.get("answers")[ind].get("mass"))

    def __message_with_results(self, answers: list[bool]):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Поздравляю!")
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(f"Количество ваших баллов равно: {sum(answers)}")
        btn_continue = msg.addButton("Продолжить выполнять тесты", QtWidgets.QMessageBox.ButtonRole.NoRole)
        msg.setDefaultButton(btn_continue)
        msg.exec()


class Application(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.count_answers: list[bool] = []
        self.questions: dict = {}
        self.stackedWidget.setCurrentIndex(3)

        for btn in get_filtered_list_files():
            btn_: QPushButton = QtWidgets.QPushButton()
            btn_.setText(btn.upper())
            btn_.setObjectName(f"BTN_{btn.upper().replace(' ', '_')}")
            _btn = f'{btn.replace(" ", "_")}'
            self.questions = get_json_tests_to_python(_btn)
            btn_.clicked.connect(lambda: self.__open_test(self.questions))
            self.verticalLayout_3.addWidget(btn_)

    def __open_test(self, read_data: dict):
        self.tests_window = Tests(read_data=read_data)
        self.tests_window.show()

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
