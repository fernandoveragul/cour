import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QPushButton

from dependencies.get_test import get_json_tests_to_python, get_filtered_list_files, post_python_to_json_test
from dependencies.work_with_data import gen_q, open_test_text, filtered_answers, load_default_test
from display import mainWindow, testsWindow


class Tests(QtWidgets.QWidget, testsWindow.Ui_Form):
    def __init__(self, read_data: dict, user_data: tuple):
        super().__init__()
        self.user_data = user_data
        self.setupUi(self)
        self.setWindowTitle("Текущий тест")

        self.count_answers: list = []
        self.count_gen_iter: list = []

        questions: list[dict] = list(gen_q(read_data["response"]))
        buttons: list[QPushButton] = [self.btnFirstAnswer, self.btnSecondAnswer, self.btnThirdAnswer,
                                      self.btnFourAnswer]
        gen = open_test_text(label=self.lblTextQuestion, buttons=buttons, data=questions)

        self.is_end(next(gen))

        self.lblTextQuestion.setText(read_data.get("response")[0].get("text"))
        for ind, btn in enumerate(buttons):
            btn.setCheckable(True)
            btn.setText(read_data.get("response")[0].get("answers")[ind].get("answer"))

        self.btnFirstAnswer.clicked.connect(lambda: self.is_end(next(gen, False)))
        self.btnSecondAnswer.clicked.connect(lambda: self.is_end(next(gen, False)))
        self.btnThirdAnswer.clicked.connect(lambda: self.is_end(next(gen, False)))
        self.btnFourAnswer.clicked.connect(lambda: self.is_end(next(gen, False)))

    def is_end(self, data: bool | dict):
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
        msg.setText(f"{self.user_data[0]} {self.user_data[-1]}, количество ваших баллов равно: {sum(answers)}")
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
        self.__user_info = None
        self._tmp = load_default_test()
        self._tmp_count = 0

        self.__add_placeholders()

        self.stackedWidget.setCurrentIndex(0)
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
        self.tests_window = Tests(read_data=read_data, user_data=self.__user_info)
        self.tests_window.show()

    def __login(self):
        lg, ps = [self.ledtLogin.text(), self.ledtPassword.text()]
        self.ledtLogin.setText("")
        self.ledtPassword.setText("")
        if lg == "" and ps == "":
            ps, lg = "user", "user"
            self.__user_info = lg, ps
        if f'{lg}' == f'{ps[::-1]}':
            self.stackedWidget.setCurrentIndex(2)
        else:
            self.stackedWidget.setCurrentIndex(1)

    def __add_to_test(self, default_data: dict[str, list], count_q: int = 0):
        dt = default_data.get("response")
        q = {
            "question": count_q,
            "text": self.ledtTextQuestion.text(),
            "answers": [
                {"answer": self.ledtAnswerFirst.text(), "mass": self.rbtnFirstTrue.isChecked()},
                {"answer": self.ledtAnswerSecond.text(), "mass": self.rbtnSecondTrue.isChecked()},
                {"answer": self.ledtAnswerThird.text(), "mass": self.rbtnThirdTrue.isChecked()},
                {"answer": self.ledtAnswerFour.text(), "mass": self.rbtnFourTrue.isChecked()}
            ]
        }
        dt_ = dt + [q]
        count_q += 1
        default_data.update({"response": dt_})
        self._tmp = default_data
        self._tmp_count = count_q
        print(self._tmp)
        self.__clear_admin_interface()
        print(dict(self._tmp.get("response")[-1]), type(self._tmp))
        QtWidgets.QMessageBox.information(self, "Важная информация",
                                          f'Вопрос: {self._tmp.get("response")[-1].get("text")}\n'
                                          f'Ответ: {filtered_answers(self._tmp.get("response")[-1].get("answers"))}')

    def create_test(self, write_data):
        post_python_to_json_test(write_data=write_data, number_var=self.ledtVarNumber.text())
        QtWidgets.QMessageBox.information(self, "Успех", f"Был создан тест {get_filtered_list_files()[-1]}")
        self.__clear_admin_interface()
        self._tmp = load_default_test()
        self._tmp_count = 0
        self.stackedWidget.setCurrentIndex(0)

    def __clear_admin_interface(self):
        self.ledtTextQuestion.setText("")
        self.ledtAnswerFirst.setText("")
        self.ledtAnswerSecond.setText("")
        self.ledtAnswerThird.setText("")
        self.ledtAnswerFour.setText("")
        self.ledtVarNumber.setText("")

    def __add_placeholders(self):
        self.ledtLogin.setPlaceholderText("Введите имя")
        self.ledtPassword.setPlaceholderText("Введите фамилию")
        self.ledtVarNumber.setPlaceholderText("Введите номер варианта (может быть автоматическим)")
        self.ledtAnswerFirst.setPlaceholderText("Введите первый ответ")
        self.ledtAnswerSecond.setPlaceholderText("Введите второй ответ")
        self.ledtAnswerThird.setPlaceholderText("Введите третий ответ")
        self.ledtAnswerFour.setPlaceholderText("Введите четвёртый ответ")
        self.ledtTextQuestion.setPlaceholderText("Введите текст вопроса")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())
