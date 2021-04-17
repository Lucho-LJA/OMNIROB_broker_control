# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_controlWindow(object):
    def setupUi(self, controlWindow):
        controlWindow.setObjectName("controlWindow")
        controlWindow.resize(1300, 690)
        controlWindow.setMinimumSize(QtCore.QSize(1300, 690))
        controlWindow.setMaximumSize(QtCore.QSize(1300, 690))
        controlWindow.setMouseTracking(True)
        controlWindow.setTabletTracking(True)
        self.centralwidget = QtWidgets.QWidget(controlWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 530, 300, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setMinimumSize(QtCore.QSize(76, 76))
        self.label_9.setMaximumSize(QtCore.QSize(76, 76))
        self.label_9.setStyleSheet("border-image: url(:/logos/lib/libPyqt/PyqtImg/logos/logoESPE.png);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_10.setMinimumSize(QtCore.QSize(76, 76))
        self.label_10.setMaximumSize(QtCore.QSize(76, 76))
        self.label_10.setStyleSheet("border-image: url(:/logos/lib/libPyqt/PyqtImg/logos/logoMKT.png);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(1100, 560, 91, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_fecha = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_fecha.setMinimumSize(QtCore.QSize(89, 17))
        self.label_fecha.setMaximumSize(QtCore.QSize(89, 17))
        self.label_fecha.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_fecha.setObjectName("label_fecha")
        self.verticalLayout_4.addWidget(self.label_fecha)
        self.label_hora = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_hora.setMinimumSize(QtCore.QSize(89, 17))
        self.label_hora.setMaximumSize(QtCore.QSize(89, 17))
        self.label_hora.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_hora.setObjectName("label_hora")
        self.verticalLayout_4.addWidget(self.label_hora)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 620, 200, 15))
        self.label.setMinimumSize(QtCore.QSize(200, 15))
        self.label.setMaximumSize(QtCore.QSize(200, 15))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 500, 17))
        self.label_3.setMaximumSize(QtCore.QSize(500, 500))
        self.label_3.setObjectName("label_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(750, 20, 530, 500))
        self.tabWidget.setMinimumSize(QtCore.QSize(530, 500))
        self.tabWidget.setMaximumSize(QtCore.QSize(530, 500))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setGeometry(QtCore.QRect(140, 130, 80, 63))
        self.pushButton_8.setStyleSheet("background-image: url(:/teclas/lib/libPyqt/PyqtImg/teclas/tia.jpg);")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 360, 501, 61))
        self.tableWidget_3.setTabletTracking(True)
        self.tableWidget_3.setRowCount(1)
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setObjectName("tableWidget_3")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(110)
        self.pushButton_30 = QtWidgets.QPushButton(self.tab)
        self.pushButton_30.setGeometry(QtCore.QRect(140, 200, 80, 63))
        self.pushButton_30.setStyleSheet("background-image: url(:/teclas/lib/libPyqt/PyqtImg/teclas/ti.jpg);")
        self.pushButton_30.setText("")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.tab)
        self.pushButton_31.setGeometry(QtCore.QRect(140, 270, 80, 63))
        self.pushButton_31.setStyleSheet("background-image: url(:/teclas/lib/libPyqt/PyqtImg/teclas/tib.jpg);")
        self.pushButton_31.setText("")
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.tab)
        self.pushButton_32.setGeometry(QtCore.QRect(220, 130, 80, 63))
        self.pushButton_32.setStyleSheet("background-image: url(:/teclas/lib/libPyqt/PyqtImg/teclas/ta.jpg);")
        self.pushButton_32.setText("")
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.tab)
        self.pushButton_33.setGeometry(QtCore.QRect(300, 130, 80, 63))
        self.pushButton_33.setStyleSheet("background-image: url(:/teclas/lib/libPyqt/PyqtImg/teclas/tda.jpg);")
        self.pushButton_33.setText("")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.tab)
        self.pushButton_34.setGeometry(QtCore.QRect(220, 200, 80, 63))
        self.pushButton_34.setStyleSheet("background-image: url(:/teclas/lib/libPyqt/PyqtImg/teclas/tgc.jpg);")
        self.pushButton_34.setText("")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.tab)
        self.pushButton_35.setGeometry(QtCore.QRect(300, 200, 80, 63))
        self.pushButton_35.setStyleSheet("background-image: url(:/teclas/lib/libPyqt/PyqtImg/teclas/td.jpg);")
        self.pushButton_35.setText("")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.tab)
        self.pushButton_36.setGeometry(QtCore.QRect(220, 270, 80, 63))
        self.pushButton_36.setStyleSheet("background-image: url(:/teclas/lib/libPyqt/PyqtImg/teclas/tb.jpg);")
        self.pushButton_36.setText("")
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(self.tab)
        self.pushButton_37.setGeometry(QtCore.QRect(300, 270, 80, 63))
        self.pushButton_37.setStyleSheet("background-image: url(:/teclas/lib/libPyqt/PyqtImg/teclas/tdb.jpg);")
        self.pushButton_37.setText("")
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab)
        self.pushButton_9.setGeometry(QtCore.QRect(140, 60, 80, 63))
        self.pushButton_9.setStyleSheet("background-image: url(:/teclas/lib/libPyqt/PyqtImg/teclas/tah.jpg);")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab)
        self.pushButton_16.setGeometry(QtCore.QRect(300, 60, 80, 63))
        self.pushButton_16.setStyleSheet("background-image: url(:/teclas/lib/libPyqt/PyqtImg/teclas/th.jpg);")
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(20, 80, 53, 28))
        self.spinBox.setMaximum(90)
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 91, 20))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 0, 491, 111))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 191, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 30, 281, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 80, 111, 23))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(160, 80, 181, 23))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(360, 80, 112, 23))
        self.radioButton_5.setObjectName("radioButton_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 140, 141, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 30, 89, 25))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_18.setEnabled(False)
        self.pushButton_18.setGeometry(QtCore.QRect(20, 60, 89, 25))
        self.pushButton_18.setObjectName("pushButton_18")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_2.setGeometry(QtCore.QRect(10, 110, 53, 28))
        self.spinBox_2.setMaximum(2920)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_3.setGeometry(QtCore.QRect(70, 110, 53, 28))
        self.spinBox_3.setMaximum(1860)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 21, 19))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(70, 90, 21, 19))
        self.label_6.setObjectName("label_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setGeometry(QtCore.QRect(360, 110, 151, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_12 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_12.setGeometry(QtCore.QRect(10, 30, 112, 23))
        self.radioButton_12.setChecked(True)
        self.radioButton_12.setObjectName("radioButton_12")
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_10.setGeometry(QtCore.QRect(10, 70, 112, 23))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_11 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_11.setGeometry(QtCore.QRect(10, 110, 121, 23))
        self.radioButton_11.setObjectName("radioButton_11")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_14.setEnabled(False)
        self.pushButton_14.setGeometry(QtCore.QRect(190, 310, 151, 25))
        self.pushButton_14.setObjectName("pushButton_14")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 340, 521, 121))
        self.tableWidget_2.setTabletTracking(True)
        self.tableWidget_2.setRowCount(3)
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(114)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(40)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 110, 141, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setGeometry(QtCore.QRect(190, 110, 141, 101))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_19.setGeometry(QtCore.QRect(20, 30, 89, 25))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_21.setGeometry(QtCore.QRect(20, 60, 89, 25))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_28 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_28.setEnabled(False)
        self.pushButton_28.setGeometry(QtCore.QRect(200, 210, 111, 25))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_29.setEnabled(False)
        self.pushButton_29.setGeometry(QtCore.QRect(390, 310, 131, 25))
        self.pushButton_29.setObjectName("pushButton_29")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setGeometry(QtCore.QRect(170, 240, 191, 61))
        self.groupBox_5.setObjectName("groupBox_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 30, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setChecked(True)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_7.setGeometry(QtCore.QRect(110, 30, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setChecked(False)
        self.radioButton_7.setObjectName("radioButton_7")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_15.setGeometry(QtCore.QRect(230, 60, 89, 25))
        self.pushButton_15.setObjectName("pushButton_15")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(20, 170, 491, 121))
        self.tableWidget.setTabletTracking(True)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(105)
        self.tabWidget.addTab(self.tab_3, "")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 720, 480))
        self.label_2.setMinimumSize(QtCore.QSize(720, 480))
        self.label_2.setMaximumSize(QtCore.QSize(720, 480))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        controlWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(controlWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 24))
        self.menubar.setObjectName("menubar")
        self.menu_Archivo = QtWidgets.QMenu(self.menubar)
        self.menu_Archivo.setObjectName("menu_Archivo")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuConfiguraci_n = QtWidgets.QMenu(self.menubar)
        self.menuConfiguraci_n.setObjectName("menuConfiguraci_n")
        controlWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(controlWindow)
        self.statusbar.setObjectName("statusbar")
        controlWindow.setStatusBar(self.statusbar)
        self.actionExportar_Imagen = QtWidgets.QAction(controlWindow)
        self.actionExportar_Imagen.setObjectName("actionExportar_Imagen")
        self.actionSalir = QtWidgets.QAction(controlWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionManual = QtWidgets.QAction(controlWindow)
        self.actionManual.setObjectName("actionManual")
        self.actionConfiguraci_n_general = QtWidgets.QAction(controlWindow)
        self.actionConfiguraci_n_general.setObjectName("actionConfiguraci_n_general")
        self.actionAvanzada = QtWidgets.QAction(controlWindow)
        self.actionAvanzada.setObjectName("actionAvanzada")
        self.menu_Archivo.addAction(self.actionExportar_Imagen)
        self.menu_Archivo.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionManual)
        self.menuConfiguraci_n.addAction(self.actionConfiguraci_n_general)
        self.menuConfiguraci_n.addAction(self.actionAvanzada)
        self.menubar.addAction(self.menu_Archivo.menuAction())
        self.menubar.addAction(self.menuConfiguraci_n.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(controlWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(controlWindow)

    def retranslateUi(self, controlWindow):
        _translate = QtCore.QCoreApplication.translate
        controlWindow.setWindowTitle(_translate("controlWindow", "Ventana de Control"))
        self.label_9.setText(_translate("controlWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_10.setText(_translate("controlWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_fecha.setText(_translate("controlWindow", "00 Ene. 20"))
        self.label_hora.setText(_translate("controlWindow", "mar. 00:00"))
        self.label_3.setText(_translate("controlWindow", "<html><head/><body><p><span style=\" color:#2e3436;\">OBSTÁCULOS </span><span style=\" color:#ef2929;\">OB</span><span style=\" color:#204a87;\">JE</span><span style=\" color:#729fcf;\">TOS </span><span style=\" color:#ad7fa8;\">OMNI1 </span><span style=\" color:#fcaf3e;\">OMNI2 </span><span style=\" color:#c17d11;\">OMNI3</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("controlWindow", "Omni1"))
        self.comboBox.setItemText(1, _translate("controlWindow", "Omni2"))
        self.comboBox.setItemText(2, _translate("controlWindow", "Omni3"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("controlWindow", "Omni"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("controlWindow", "Coord. X"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("controlWindow", "Coord. Y"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("controlWindow", "Velocidad"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("controlWindow", "Dirección"))
        self.label_4.setText(_translate("controlWindow", "Velocidad:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("controlWindow", "Manual"))
        self.groupBox.setTitle(_translate("controlWindow", "Opciones de funcionamiento"))
        self.radioButton.setText(_translate("controlWindow", "Movimiento a punto"))
        self.radioButton_2.setText(_translate("controlWindow", "Trayectoria con Obstáculos Sim."))
        self.radioButton_3.setText(_translate("controlWindow", "Trayectoria"))
        self.radioButton_4.setText(_translate("controlWindow", "Simular Clasificador"))
        self.radioButton_5.setText(_translate("controlWindow", "Clasificador"))
        self.groupBox_2.setTitle(_translate("controlWindow", "Puntos"))
        self.pushButton_10.setText(_translate("controlWindow", "Cargar"))
        self.pushButton_18.setText(_translate("controlWindow", "Borrar"))
        self.label_5.setText(_translate("controlWindow", "x:"))
        self.label_6.setText(_translate("controlWindow", "y:"))
        self.groupBox_3.setTitle(_translate("controlWindow", "Objetos"))
        self.radioButton_12.setText(_translate("controlWindow", "Obj. Rojos"))
        self.radioButton_10.setText(_translate("controlWindow", "Obj. Azules"))
        self.radioButton_11.setText(_translate("controlWindow", "Obj. Celestes"))
        self.pushButton_14.setText(_translate("controlWindow", "INICIAR PROCESO"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("controlWindow", "Omni1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("controlWindow", "Omni2"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("controlWindow", "Omni3"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("controlWindow", "Coord. X"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("controlWindow", "Coord. Y"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("controlWindow", "Velocidad"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("controlWindow", "Dirección"))
        self.comboBox_2.setItemText(0, _translate("controlWindow", "Omni1"))
        self.comboBox_2.setItemText(1, _translate("controlWindow", "Omni2"))
        self.comboBox_2.setItemText(2, _translate("controlWindow", "Omni3"))
        self.groupBox_4.setTitle(_translate("controlWindow", "Obstáculos"))
        self.pushButton_19.setText(_translate("controlWindow", "Cargar"))
        self.pushButton_21.setText(_translate("controlWindow", "Detectar"))
        self.pushButton_28.setText(_translate("controlWindow", "PARAR TODO"))
        self.pushButton_29.setText(_translate("controlWindow", "Guardar datos"))
        self.groupBox_5.setTitle(_translate("controlWindow", "Generador Trayectoria"))
        self.radioButton_6.setText(_translate("controlWindow", "Campos"))
        self.radioButton_7.setText(_translate("controlWindow", "A*"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("controlWindow", "Automático"))
        self.pushButton_15.setText(_translate("controlWindow", "Activar"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("controlWindow", "Omni1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("controlWindow", "Omni2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("controlWindow", "Omni3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("controlWindow", "Coord. X"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("controlWindow", "Coord. Y"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("controlWindow", "Velocidad"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("controlWindow", "Dirección"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("controlWindow", "IOT"))
        self.menu_Archivo.setTitle(_translate("controlWindow", "&Archivo"))
        self.menuAyuda.setTitle(_translate("controlWindow", "Ayuda"))
        self.menuConfiguraci_n.setTitle(_translate("controlWindow", "Configuración"))
        self.actionExportar_Imagen.setText(_translate("controlWindow", "Exportar Imagen"))
        self.actionSalir.setText(_translate("controlWindow", "Salir"))
        self.actionManual.setText(_translate("controlWindow", "Manual"))
        self.actionConfiguraci_n_general.setText(_translate("controlWindow", "Configuración general"))
        self.actionAvanzada.setText(_translate("controlWindow", "Avanzada"))
import imgPyqt_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controlWindow = QtWidgets.QMainWindow()
    ui = Ui_controlWindow()
    ui.setupUi(controlWindow)
    controlWindow.show()
    sys.exit(app.exec_())
