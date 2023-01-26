import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QPushButton

from dependencies.get_test import get_json_tests_to_python, get_filtered_list_files, get_test, get_path, \
    post_python_to_json_test
from dependencies.work_with_data import gen_q, open_test_text
from display import mainWindow, testsWindow


class Tests(QtWidgets.QWidget, testsWindow.Ui_Form):
    def __init__(self, read_data: dict):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Текущий тест")

        self.count_answers: list = []
        self.count_gen_iter: list = []

        questions: list[dict] = list(gen_q(read_data["response"]))
        buttons: list[QPushButton] = [self.btnFirstAnswer, self.btnSecondAnswer, self.btnThirdAnswer,
                                      self.btnFourAnswer]
        gen = open_test_text(label=self.lblTextQuestion, buttons=buttons, data=questions)

        self.is_end(read_data.get("response")[0], buttons)

        self.lblTextQuestion.setText(read_data.get("response")[0].get("text"))
        for ind, btn in enumerate(buttons):
            btn.setCheckable(True)
            btn.setText(read_data.get("response")[0].get("answers")[ind].get("answer"))

        self.btnFirstAnswer.clicked.connect(lambda: self.is_end(next(gen, False), buttons))
        self.btnSecondAnswer.clicked.connect(lambda: self.is_end(next(gen, False), buttons))
        self.btnThirdAnswer.clicked.connect(lambda: self.is_end(next(gen, False), buttons))
        self.btnFourAnswer.clicked.connect(lambda: self.is_end(next(gen, False), buttons))

    def is_end(self, data: bool | dict, buttons: list[QPushButton]):
        self.count_gen_iter.append(0 if data is False else None)
        print(data, self.count_gen_iter.count(None))
        match data:
            case False:
                self.__message_with_results(self.count_answers)
                self.close()
            case _:
                if self.btnFirstAnswer.isChecked():
                    self.count_answers.append(data.get("answers")[0].get("mass"))
                    self.btnFirstAnswer.setChecked(False)

                if self.btnSecondAnswer.isChecked():
                    self.count_answers.append(data.get("answers")[1].get("mass"))
                    self.btnSecondAnswer.setChecked(False)

                if self.btnThirdAnswer.isChecked():
                    self.count_answers.append(data.get("answers")[2].get("mass"))
                    self.btnThirdAnswer.setChecked(False)

                if self.btnFourAnswer.isChecked():
                    self.count_answers.append(data.get("answers")[3].get("mass"))
                    self.btnFourAnswer.setChecked(False)

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
        self.setWindowTitle("Тестирование")
        self.count_answers: list[bool] = []
        self.questions: dict = {}

        self.__auth_data = None
        self.__user_info = None
        self._tmp = self.__load_default_test()
        self._tmp_count = 0
        self.stackedWidget.setCurrentIndex(2)
        self.btnSugnUp.clicked.connect(lambda: self.__login())

        self.btnGoBack.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btnAccept.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

        self.btnAddQ.clicked.connect(lambda: self.__add_to_test(self._tmp, self._tmp_count))
        self.btnFinish.clicked.connect(lambda: self.create_test(self._tmp))

        for btn in get_filtered_list_files():
            btn_: QPushButton = QtWidgets.QPushButton()
            btn_.setText(btn.upper())
            btn_.setObjectName(f"BTN_{btn.upper().replace(' ', '_')}")
            path_to_questions = f'{btn.replace(" ", "_")}'
            self.questions = get_json_tests_to_python(path_to_questions)
            btn_.clicked.connect(lambda: self.__open_test(self.questions))
            self.verticalLayout_3.addWidget(btn_)

    def __open_test(self, read_data: dict):
        self.tests_window = Tests(read_data=read_data)
        self.tests_window.show()

    def __login(self):
        lg, ps = [self.ledtLogin.text(), self.ledtPassword.text()]
        if f'{lg}' == f'{ps[::-1]}':
            self.ledtLogin.setText("")
            self.ledtPassword.setText("")
            self.stackedWidget.setCurrentIndex(2)
        else:
            self.stackedWidget.setCurrentIndex(1)

    def __add_to_test(self, default_data: dict[str, list], count_q: int = 0):
        dt = default_data.get("response")
        q = {
            "question": count_q
        }, {
            "text": self.ledtTextQuestion.text()
        }, {
            "answers": [
                {"answer": self.ledtAnswerFirst.text(), "mass": self.rbtnFirstTrue.isChecked()},
                {"answer": self.ledtAnswerSecond.text(), "mass": self.rbtnSecondTrue.isChecked()},
                {"answer": self.ledtAnswerThird.text(), "mass": self.rbtnThirdTrue.isChecked()},
                {"answer": self.ledtAnswerFour.text(), "mass": self.rbtnFourTrue.isChecked()}
            ]
        }
        dt.append(q)
        count_q += 1
        default_data.update({"response": dt})
        self._tmp = default_data
        self._tmp_count = count_q

    def __load_default_test(self):
        path_from_read: str = get_path("display/origin_files")
        return get_test(f'{path_from_read}origin_schema.json')

    def create_test(self, write_data):
        post_python_to_json_test(write_data=write_data, number_var=self.ledtVarNumber.text())
        self.ledtTextQuestion.setText("")
        self.ledtAnswerFirst.setText("")
        self.ledtAnswerSecond.setText("")
        self.ledtAnswerThird.setText("")
        self.ledtAnswerFour.setText("")
        self.ledtVarNumber.setText("")
        self.stackedWidget.setCurrentIndex(0)

    def get_name_executor(self):
        ...


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())
