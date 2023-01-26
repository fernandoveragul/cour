# Form implementation generated from reading ui file 'display/origin_files/mainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(437, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.helloPage = QtWidgets.QWidget()
        self.helloPage.setObjectName("helloPage")
        self.gridLayout = QtWidgets.QGridLayout(self.helloPage)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 189, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(131, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.ledtLogin = QtWidgets.QLineEdit(self.helloPage)
        self.ledtLogin.setObjectName("ledtLogin")
        self.gridLayout.addWidget(self.ledtLogin, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(131, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        self.ledtPassword = QtWidgets.QLineEdit(self.helloPage)
        self.ledtPassword.setObjectName("ledtPassword")
        self.gridLayout.addWidget(self.ledtPassword, 2, 1, 1, 1)
        self.btnSugnUp = QtWidgets.QPushButton(self.helloPage)
        self.btnSugnUp.setObjectName("btnSugnUp")
        self.gridLayout.addWidget(self.btnSugnUp, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 189, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 1, 1, 1)
        self.stackedWidget.addWidget(self.helloPage)
        self.instructionsPage = QtWidgets.QWidget()
        self.instructionsPage.setObjectName("instructionsPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.instructionsPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tboxInstruction = QtWidgets.QTextBrowser(self.instructionsPage)
        self.tboxInstruction.setObjectName("tboxInstruction")
        self.gridLayout_2.addWidget(self.tboxInstruction, 0, 0, 1, 2)
        self.btnGoBack = QtWidgets.QPushButton(self.instructionsPage)
        self.btnGoBack.setObjectName("btnGoBack")
        self.gridLayout_2.addWidget(self.btnGoBack, 1, 0, 1, 1)
        self.btnAccept = QtWidgets.QPushButton(self.instructionsPage)
        self.btnAccept.setObjectName("btnAccept")
        self.gridLayout_2.addWidget(self.btnAccept, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.instructionsPage)
        self.adminPage = QtWidgets.QWidget()
        self.adminPage.setObjectName("adminPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.adminPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ledtAnswerSecond = QtWidgets.QLineEdit(self.adminPage)
        self.ledtAnswerSecond.setObjectName("ledtAnswerSecond")
        self.gridLayout_3.addWidget(self.ledtAnswerSecond, 3, 1, 1, 1)
        self.rbtnFirstTrue = QtWidgets.QRadioButton(self.adminPage)
        self.rbtnFirstTrue.setObjectName("rbtnFirstTrue")
        self.gridLayout_3.addWidget(self.rbtnFirstTrue, 2, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.adminPage)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 1, 1, 3)
        self.rbtnFourTrue = QtWidgets.QRadioButton(self.adminPage)
        self.rbtnFourTrue.setObjectName("rbtnFourTrue")
        self.gridLayout_3.addWidget(self.rbtnFourTrue, 5, 2, 1, 1)
        self.ledtAnswerThird = QtWidgets.QLineEdit(self.adminPage)
        self.ledtAnswerThird.setObjectName("ledtAnswerThird")
        self.gridLayout_3.addWidget(self.ledtAnswerThird, 4, 1, 1, 1)
        self.rbtnSecondTrue = QtWidgets.QRadioButton(self.adminPage)
        self.rbtnSecondTrue.setObjectName("rbtnSecondTrue")
        self.gridLayout_3.addWidget(self.rbtnSecondTrue, 3, 2, 1, 1)
        self.btnFinish = QtWidgets.QPushButton(self.adminPage)
        self.btnFinish.setObjectName("btnFinish")
        self.gridLayout_3.addWidget(self.btnFinish, 7, 2, 1, 1)
        self.ledtAnswerFour = QtWidgets.QLineEdit(self.adminPage)
        self.ledtAnswerFour.setObjectName("ledtAnswerFour")
        self.gridLayout_3.addWidget(self.ledtAnswerFour, 5, 1, 1, 1)
        self.ledtAnswerFirst = QtWidgets.QLineEdit(self.adminPage)
        self.ledtAnswerFirst.setObjectName("ledtAnswerFirst")
        self.gridLayout_3.addWidget(self.ledtAnswerFirst, 2, 1, 1, 1)
        self.rbtnThirdTrue = QtWidgets.QRadioButton(self.adminPage)
        self.rbtnThirdTrue.setObjectName("rbtnThirdTrue")
        self.gridLayout_3.addWidget(self.rbtnThirdTrue, 4, 2, 1, 1)
        self.ledtTextQuestion = QtWidgets.QLineEdit(self.adminPage)
        self.ledtTextQuestion.setObjectName("ledtTextQuestion")
        self.gridLayout_3.addWidget(self.ledtTextQuestion, 0, 1, 1, 3)
        self.btnAddQ = QtWidgets.QPushButton(self.adminPage)
        self.btnAddQ.setObjectName("btnAddQ")
        self.gridLayout_3.addWidget(self.btnAddQ, 7, 1, 1, 1)
        self.ledtVarNumber = QtWidgets.QLineEdit(self.adminPage)
        self.ledtVarNumber.setObjectName("ledtVarNumber")
        self.gridLayout_3.addWidget(self.ledtVarNumber, 6, 1, 1, 1)
        self.stackedWidget.addWidget(self.adminPage)
        self.choicePage = QtWidgets.QWidget()
        self.choicePage.setObjectName("choicePage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.choicePage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gboxVars = QtWidgets.QGroupBox(self.choicePage)
        self.gboxVars.setObjectName("gboxVars")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gboxVars)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addWidget(self.gboxVars)
        spacerItem4 = QtWidgets.QSpacerItem(20, 471, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.stackedWidget.addWidget(self.choicePage)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тестирование"))
        self.btnSugnUp.setText(_translate("MainWindow", "ВЕРИФИЦИРОВАТЬСЯ"))
        self.btnGoBack.setText(_translate("MainWindow", "ВЕРНУТЬСЯ"))
        self.btnAccept.setText(_translate("MainWindow", "ПОНЯТНО"))
        self.rbtnFirstTrue.setText(_translate("MainWindow", "ВЕРНЫЙ"))
        self.rbtnFourTrue.setText(_translate("MainWindow", "ВЕРНЫЙ"))
        self.rbtnSecondTrue.setText(_translate("MainWindow", "ВЕРНЫЙ"))
        self.btnFinish.setText(_translate("MainWindow", "ЗАКОНЧИТЬ"))
        self.rbtnThirdTrue.setText(_translate("MainWindow", "ВЕРНЫЙ"))
        self.btnAddQ.setText(_translate("MainWindow", "ДОБАВИТЬ"))
        self.gboxVars.setTitle(_translate("MainWindow", "Варианты"))
