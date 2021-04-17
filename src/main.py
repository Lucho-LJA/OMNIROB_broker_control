#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from config import globales
import sys
from ventanas import *




if __name__ == "__main__":
	globales.dir_work=os.path.dirname(os.path.abspath(__file__))
	globales.dir_work_aux=os.path.dirname(os.path.abspath(__file__))
	recuperar_variable_total()
	Init_cuad()
	init_dep()




	app = QtWidgets.QApplication([])

	Ventana_Inicio=Ui_Inicio()
	Ventana_Inicio.show()
	#wConfig.show()
	app.exec_()