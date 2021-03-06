# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startWindows.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Inicio(object):
    def setupUi(self, Inicio):
        Inicio.setObjectName("Inicio")
        Inicio.resize(315, 326)
        Inicio.setMinimumSize(QtCore.QSize(315, 326))
        Inicio.setMaximumSize(QtCore.QSize(315, 326))
        Inicio.setWindowOpacity(13.0)
        Inicio.setStyleSheet("image: url(:/logos/PyqtImg/logos/logoESPE.png);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(Inicio)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Ecuador))
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 311, 81))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 90, 223, 110))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(62, 142, 180);")
        self.pushButton.setText("INICIAR CONTROL")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(62, 142, 180);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(62, 142, 180);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 240, 91, 42))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_fecha = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_fecha.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_fecha.setObjectName("label_fecha")
        self.verticalLayout_2.addWidget(self.label_fecha)
        self.label_hora = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_hora.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_hora.setObjectName("label_hora")
        self.verticalLayout_2.addWidget(self.label_hora)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 210, 160, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setStyleSheet("border-image: url(:/logos/lib/libPyqt/PyqtImg/logos/logoMKT.png);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("border-image: url(:/logos/lib/libPyqt/PyqtImg/logos/logoESPE.png);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        Inicio.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(Inicio)
        self.statusBar.setObjectName("statusBar")
        Inicio.setStatusBar(self.statusBar)

        self.retranslateUi(Inicio)
        QtCore.QMetaObject.connectSlotsByName(Inicio)

    def retranslateUi(self, Inicio):
        _translate = QtCore.QCoreApplication.translate
        Inicio.setWindowTitle(_translate("Inicio", "Inicio - OmniROB"))
        self.label_3.setText(_translate("Inicio", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#23cb14;\">OMNIROB</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#23cb14;\">Control de plataforma multirobot</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Inicio", "CONFIGURACI??N"))
        self.pushButton_3.setText(_translate("Inicio", "MANUAL DE USUARIO"))
        self.label_fecha.setText(_translate("Inicio", "00 Ene. 20"))
        self.label_hora.setText(_translate("Inicio", "mar. 00:00"))
        self.label_2.setText(_translate("Inicio", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("Inicio", "<html><head/><body><p><br/></p></body></html>"))
import imgPyqt_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Inicio = QtWidgets.QMainWindow()
    ui = Ui_Inicio()
    ui.setupUi(Inicio)
    Inicio.show()
    sys.exit(app.exec_())
