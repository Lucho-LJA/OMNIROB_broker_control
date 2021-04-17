#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from config import globales
from PyQt5 import QtCore, QtGui, QtWidgets
from lib import ros_config as vros

from lib.global_funcion import *
from lib.function_path_planning import *
from lib.function_path_planning_A import *

from lib.libPyqt.startWindows import *
from lib.libPyqt.configWindow import *
from lib.libPyqt.PruebaVideo import *
from lib.libPyqt.configAvanWindow import *
from lib.libPyqt.controlWindow import *
import lib.planificador as pln

import base64
import cv2
import numpy as np
import math
import time



###################################################################################
########################VENTANA DE CONFIGURACION###################################
###################################################################################
class Ui_configWindow(QtWidgets.QMainWindow, Ui_configWindow):
	def __init__(self, *args, **kwargs):

		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self) 
		#Tiempo en pantalla
		self.timer = QtCore.QTimer(self)
		self.timer.setInterval(1000)
		self.timer.timeout.connect(self.mostrar_fh)
		self.timer.start()

		#Detección de camaras
		self.video_cam=detec_cam()
		self.config_list_cam.clear()
		self.config_list_cam.addItems(self.video_cam)

		if globales.tarjeta_camara<=self.config_list_cam.count() and globales.aux_vent_config==0 :
			self.config_list_cam.setCurrentRow(globales.tarjeta_camara)
		elif globales.aux_tarjeta<=self.config_list_cam.count() and globales.aux_vent_config==1 :
			self.config_list_cam.setCurrentRow(globales.aux_tarjeta)
			globales.aux_vent_config==0

		
		#Deteccion de robots marcados
		if globales.st_omni1==1:
			self.checkBox.setChecked(True)
		else:
			self.checkBox.setChecked(False)
		if globales.st_omni2==1:
			self.checkBox_2.setChecked(True)
		else:
			self.checkBox_2.setChecked(False)
		if globales.st_omni3==1:
			self.checkBox_3.setChecked(True)
		else:
			self.checkBox_3.setChecked(False)

		#Deteccion de boton actualizar camara
		self.pushButton_2.clicked.connect(self.act_cam)

		#Deteccion de boton recargar camara
		self.pushButton.clicked.connect(self.act_recam)

		#Deteccion boton regresar
		self.pushButton_4.clicked.connect(self.act_reg)

		#Deteccion boton probar camara
		self.pushButton_6.clicked.connect(self.act_prob)

		#Actualizar omnis en uso
		self.pushButton_3.clicked.connect(self.act_omni)

		#Dteccion boton conf avanzada
		self.pushButton_5.clicked.connect(self.act_confA)

###################################################################################
###################################################################################
	#Abrir ventana de Config Avanzada
	def act_confA(self):
		globales.aux_vent_config=1
		self.Ventana_configA=Ui_ConfigAvanWindow()
		self.Ventana_configA.show()
		self.close()
###################################################################################
###################################################################################	
	#Actualizar uso de Omnis
	def act_omni(self):
		if self.checkBox.isChecked():
			globales.st_omni1=1
		else:
			globales.st_omni1=0
		if self.checkBox_2.isChecked():
			globales.st_omni2=1
		else:
			globales.st_omni2=0
		if self.checkBox_3.isChecked():
			globales.st_omni3=1
		else:
			globales.st_omni3=0
		guardar_variable_total()
###################################################################################
###################################################################################
	#Abrir Ventana de camara
	def act_prob(self):
		globales.aux_tarjeta=int(self.config_list_cam.currentRow())
		globales.aux_vent_config=1
		self.Ventana_ProbarCam=Ui_PruebaVideo()
		self.Ventana_ProbarCam.show()
		self.close()
###################################################################################
###################################################################################
	#Deteccion boton cerrar
	def closeEvent(self, evnt):
		if globales.aux_vent_config==0:
			self.Ventana_Inicio=Ui_Inicio()
			self.Ventana_Inicio.show()
		self.close()
###################################################################################
###################################################################################		
	def act_reg(self):
		self.Ventana_Inicio=Ui_Inicio()
		self.Ventana_Inicio.show()
		self.close()
###################################################################################
###################################################################################			
	def act_cam(self):
		globales.tarjeta_camara=int(self.config_list_cam.currentRow())
		guardar_variable_total()
###################################################################################
###################################################################################
	def act_recam(self):
		#Detección de camaras
		self.video_cam=detec_cam()
		self.config_list_cam.clear()
		self.config_list_cam.addItems(self.video_cam)
		if globales.tarjeta_camara<=self.config_list_cam.count():
			self.config_list_cam.setCurrentRow(globales.tarjeta_camara)
###################################################################################
###################################################################################

	def mostrar_fh(self):
		self.label_hora.setText(QtCore.QDateTime.currentDateTime().toString("ddd hh:mm"))
		self.label_fecha.setText(QtCore.QDateTime.currentDateTime().toString("dd/MMM/yy"))

###################################################################################
###################################################################################
###################################################################################
###################################################################################


###################################################################################
###########################VENTANA DE INICIO#######################################
###################################################################################

class Ui_Inicio(QtWidgets.QMainWindow, Ui_Inicio):
	def __init__(self, *args, **kwargs):



		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self) 
		self.statusBar.showMessage("Designers: Luis Allauca - Gabriel Guerra")
		self.timer = QtCore.QTimer(self)
		self.timer.setInterval(1000)
		self.timer.timeout.connect(self.mostrar_fh)
		self.timer.start()

		self.pushButton_2.clicked.connect(self.abrir_config)
		self.pushButton.clicked.connect(self.abrir_control)

		#self.Ventana_config=Ui_configWindow()
###################################################################################
###################################################################################
	def abrir_control(self):
		self.Ventana_control=Ui_controlWindow()
		self.Ventana_control.show()
		self.close()
###################################################################################
###################################################################################
	def abrir_config(self):
		self.Ventana_config=Ui_configWindow()
		self.Ventana_config.show()
		self.close()
###################################################################################
###################################################################################
	def mostrar_fh(self):
		self.label_hora.setText(QtCore.QDateTime.currentDateTime().toString("ddd hh:mm"))
		self.label_fecha.setText(QtCore.QDateTime.currentDateTime().toString("dd/MMM/yy"))
###################################################################################
###################################################################################
###################################################################################


###################################################################################
###################VENTANA DE PRUEBA DE CAMARA#####################################
###################################################################################
class Ui_PruebaVideo(QtWidgets.QMainWindow, Ui_PruebaVideo):
	def __init__(self, *args, **kwargs):

		self.captura= cv2.VideoCapture(globales.aux_tarjeta)
		self.captura.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
		self.captura.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self) 
		self.timer = QtCore.QTimer(self)
		self.timer.setInterval(10)
		self.timer.timeout.connect(self.mostrar_cam)
		self.timer.start()
###################################################################################
###################################################################################
	#Deteccion boton cerrar
	def closeEvent(self, evnt):

		self.Ventana_config=Ui_configWindow()
		self.Ventana_config.show()
		self.captura.release()
		self.close()
###################################################################################
###################################################################################
	def mostrar_cam(self):
		# Tomamos una captura desde la webcam.
		ok, img = self.captura.read()
 
		if not ok:
			return
        # Creamos una imagen a partir de los datos.
        #
        # QImage
        # (
        #   Los pixeles que conforman la imagen,
        #   Ancho de de la imagen,
        #   Alto de de la imagen,
        #   Numero de bytes que conforman una linea (numero_de_bytes_por_pixel * ancho),
        #   Formato de la imagen
        # )
        # 
        # img.shape
        # (
        #   Alto,
        #   Ancho,
        #   Planos de color/canales/bytes por pixel
        # )
		image = QtGui.QImage(img, img.shape[1], img.shape[0], img.shape[1] * img.shape[2], QtGui.QImage.Format_RGB888)
 
        # Creamos un pixmap a partir de la imagen.
        # OpenCV entraga los pixeles de la imagen en formato BGR en lugar del tradicional RGB,
        # por lo tanto tenemos que usar el metodo rgbSwapped() para que nos entregue una imagen con
        # los bytes Rojo y Azul intercambiados, y asi poder mostrar la imagen de forma correcta.
		pixmap = QtGui.QPixmap()
		pixmap.convertFromImage(image.rgbSwapped())
 
        # Mostramos el QPixmap en la QLabel.
		self.label.setPixmap(pixmap)
###################################################################################
###################################################################################
###################################################################################


###################################################################################
###################################################################################
#####################VENTANA DE CONFIG AVANZADA####################################
###################################################################################
class Ui_ConfigAvanWindow(QtWidgets.QMainWindow, Ui_ConfigAvanWindow):
	def __init__(self, *args, **kwargs):

		self.captura= cv2.VideoCapture(globales.tarjeta_camara)
		self.captura.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
		self.captura.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self) 
		self.statusbar.showMessage("Designers: Luis Allauca - Gabriel Guerra")
		self.timer = QtCore.QTimer(self)
		self.timer.setInterval(10)
		self.timer.timeout.connect(self.Funciones_reloj)
		self.timer.start()

		self.label_7.setMouseTracking (False)


		#Inicializar variables dimensiones
		self.spinBox.setValue(globales.capIz)
		globales.limIz=globales.capIz
		self.spinBox_2.setValue(globales.capDe)
		globales.limDe=globales.capDe
		self.spinBox_3.setValue(globales.capSu)
		globales.limSup=globales.capSu
		self.spinBox_4.setValue(globales.capInf)
		globales.limInf=globales.capInf
		self.spinBox_9.setValue(globales.divH)
		globales.Grid_mm=globales.divH
		self.spinBox_10.setValue(globales.divV)
		globales.Grid_px=globales.divV


		self.doubleSpinBox.setValue(globales.EscPix)
		globales.rest_px=globales.EscPix
		self.doubleSpinBox_2.setValue(globales.EscMM)
		globales.rest_mm=globales.EscMM

		##Dimensiones de deteccion OMNIS
		#Omni1
		globales.aG[0]=globales.omni1_Area_Cent
		globales.aS[0]=globales.omni1_Area_Sec
		globales.dA[0]=globales.omni1_Sep_Area
		globales.dAc[0]=globales.omni1_Dist_Act
		#Omni2
		globales.aG[1]=globales.omni2_Area_Cent
		globales.aS[1]=globales.omni2_Area_Sec
		globales.dA[1]=globales.omni2_Sep_Area
		globales.dAc[1]=globales.omni2_Dist_Act
		#Omni3
		globales.aG[2]=globales.omni3_Area_Cent
		globales.aS[2]=globales.omni3_Area_Sec
		globales.dA[2]=globales.omni3_Sep_Area
		globales.dAc[2]=globales.omni3_Dist_Act

		self.doubleSpinBox_3.setValue(globales.omni1_Area_Cent)
		self.doubleSpinBox_4.setValue(globales.omni1_Area_Sec)
		self.doubleSpinBox_7.setValue(globales.omni1_Sep_Area)
		self.doubleSpinBox_10.setValue(globales.omni1_Dist_Act)



		self.spinBox.editingFinished.connect(self.ch_iz)
		self.spinBox_2.editingFinished.connect(self.ch_de)
		self.spinBox_3.editingFinished.connect(self.ch_su)
		self.spinBox_4.editingFinished.connect(self.ch_inf)
		self.spinBox_9.editingFinished.connect(self.ch_divh)
		self.spinBox_10.editingFinished.connect(self.ch_divv)

		#Cargar limites
		self.pushButton.clicked.connect(self.save_var)


		#Restaurar limites
		self.pushButton_2.clicked.connect(self.res_lim)

		#Definir dimension de grafica
		self.ptI=[self.label_7.x(), self.label_7.y()+22]
		self.ptF=[(self.label_7.geometry()).width()+self.ptI[0],(self.label_7.geometry()).height()+self.ptI[1]]
		
		

		self.radioButton_5.setChecked(True)
		self.pushButton_5.clicked.connect(self.borrar_dep)
		self.pushButton_4.clicked.connect(self.save_dep)

		#Variables de escala
		self.pushButton_13.clicked.connect(self.ch_esc)
		self.pushButton_12.clicked.connect(self.ch_esc_save)
		self.tabWidget.currentChanged.connect(self.ch_gen)

		#Variables de areas
		self.pushButton_19.clicked.connect(self.ch_res_a)
		self.doubleSpinBox_7.editingFinished.connect(self.ch_mm)
		self.doubleSpinBox_10.editingFinished.connect(self.ch_mm)
		self.toolBox.currentChanged.connect(self.quit_D)
		self.doubleSpinBox_8.editingFinished.connect(self.ch_px)
		self.doubleSpinBox_9.editingFinished.connect(self.ch_px)
		self.comboBox.currentIndexChanged.connect(self.ch_omni)
		self.doubleSpinBox_3.editingFinished.connect(self.ch_ar)
		self.doubleSpinBox_4.editingFinished.connect(self.ch_ar)
		self.pushButton_28.clicked.connect(self.ch_save_omni)
###################################################################################
###################################################################################
	def ch_save_omni(self):
		##Dimensiones de deteccion OMNIS
		#Omni1
		globales.omni1_Area_Cent=globales.aG[0]
		globales.omni1_Area_Sec=globales.aS[0]
		globales.omni1_Sep_Area=globales.dA[0]
		globales.omni1_Dist_Act=globales.dAc[0]
		#Omni2
		globales.omni2_Area_Cent=globales.aG[1]
		globales.omni2_Area_Sec=globales.aS[1]
		globales.omni2_Sep_Area=globales.dA[1]
		globales.omni2_Dist_Act=globales.dAc[1]
		#Omni3
		globales.omni3_Area_Cent=globales.aG[2]
		globales.omni3_Area_Sec=globales.aS[2]
		globales.omni3_Sep_Area=globales.dA[2]
		globales.omni3_Dist_Act=globales.dAc[2]
		self.quit_D()
		guardar_variable_total()
###################################################################################
###################################################################################

	def ch_ar(self):
		globales.aG[self.comboBox.currentIndex()]=self.doubleSpinBox_3.value()
		globales.aS[self.comboBox.currentIndex()]=self.doubleSpinBox_4.value()
###################################################################################
###################################################################################
	def ch_omni(self):
		self.quit_D()
		self.doubleSpinBox_3.setValue(globales.aG[self.comboBox.currentIndex()])
		self.doubleSpinBox_4.setValue(globales.aS[self.comboBox.currentIndex()])
		self.doubleSpinBox_7.setValue(globales.dA[self.comboBox.currentIndex()])
		self.doubleSpinBox_10.setValue(globales.dAc[self.comboBox.currentIndex()])
		self.ch_mm()
###################################################################################
###################################################################################
	def ch_px(self):
		if self.toolBox.currentIndex()==2:
			self.doubleSpinBox_7.setValue(self.doubleSpinBox_8.value()*globales.EscPix/globales.EscMM)
			globales.dA[self.comboBox.currentIndex()]=self.doubleSpinBox_7.value()
		elif self.toolBox.currentIndex()==3:
			self.doubleSpinBox_10.setValue(self.doubleSpinBox_9.value()*globales.EscPix/globales.EscMM)
			globales.dAc[self.comboBox.currentIndex()]=self.doubleSpinBox_10.value()
		self.quit_D()
###################################################################################
###################################################################################
	def quit_D(self):
		globales.glineI=False
		globales.glineT=False
		globales.glineTT=False
###################################################################################
###################################################################################
	def ch_mm(self):
		self.doubleSpinBox_8.setValue(self.doubleSpinBox_7.value()*globales.EscMM/globales.EscPix)
		globales.dA[self.comboBox.currentIndex()]=self.doubleSpinBox_7.value()
		self.doubleSpinBox_9.setValue(self.doubleSpinBox_10.value()*globales.EscMM/globales.EscPix)
		globales.dAc[self.comboBox.currentIndex()]=self.doubleSpinBox_10.value()
###################################################################################
###################################################################################
	def ch_res_a(self):
		globales.glineI=False
		globales.glineT=False
		globales.glineTT=False
		if self.comboBox.currentIndex()==0:
			self.doubleSpinBox_3.setValue(globales.omni1_Area_Cent)
			self.doubleSpinBox_4.setValue(globales.omni1_Area_Sec)
			self.doubleSpinBox_7.setValue(globales.omni1_Sep_Area)
			self.doubleSpinBox_10.setValue(globales.omni1_Dist_Act)
		elif self.comboBox.currentIndex()==1:
			self.doubleSpinBox_3.setValue(globales.omni2_Area_Cent)
			self.doubleSpinBox_4.setValue(globales.omni2_Area_Sec)
			self.doubleSpinBox_7.setValue(globales.omni2_Sep_Area)
			self.doubleSpinBox_10.setValue(globales.omni2_Dist_Act)
		elif self.comboBox.currentIndex()==2:
			self.doubleSpinBox_3.setValue(globales.omni3_Area_Cent)
			self.doubleSpinBox_4.setValue(globales.omni3_Area_Sec)
			self.doubleSpinBox_7.setValue(globales.omni3_Sep_Area)
			self.doubleSpinBox_10.setValue(globales.omni3_Dist_Act)

		self.doubleSpinBox_8.setValue(self.doubleSpinBox_7.value()*globales.EscMM/globales.EscPix)
		self.doubleSpinBox_9.setValue(self.doubleSpinBox_10.value()*globales.EscMM/globales.EscPix)

		##Dimensiones de deteccion OMNIS
		#Omni1
		globales.aG[0]=globales.omni1_Area_Cent
		globales.aS[0]=globales.omni1_Area_Sec
		globales.dA[0]=globales.omni1_Sep_Area
		globales.dAc[0]=globales.omni1_Dist_Act
		#Omni2
		globales.aG[1]=globales.omni2_Area_Cent
		globales.aS[1]=globales.omni2_Area_Sec
		globales.dA[1]=globales.omni2_Sep_Area
		globales.dAc[1]=globales.omni2_Dist_Act
		#Omni3
		globales.aG[2]=globales.omni3_Area_Cent
		globales.aS[2]=globales.omni3_Area_Sec
		globales.dA[2]=globales.omni3_Sep_Area
		globales.dAc[2]=globales.omni3_Dist_Act
###################################################################################
###################################################################################
	def ch_gen(self):
		glineI=False
		glineT=False
		glineTT=False
		vent_ca=self.tabWidget.currentIndex()

		if vent_ca==1:
			self.res_lim()
			
		if vent_ca==2:
			self.ch_esc()
		if vent_ca==3:
			self.ch_res_a()
###################################################################################
###################################################################################
	def ch_esc_save(self):
		globales.EscPix=self.doubleSpinBox.value()
		globales.EscMM=self.doubleSpinBox_2.value()
		self.spinBox_9.setValue(globales.divV*globales.EscMM/globales.EscPix)
		globales.divH=self.spinBox_9.value()
		guardar_variable_total()
###################################################################################
###################################################################################
	def ch_esc(self):
		self.doubleSpinBox.setValue(globales.rest_px)
		self.doubleSpinBox_2.setValue(globales.rest_mm)
		globales.glineI=False
		globales.glineT=False
		globales.glineTT=False

###################################################################################
###################################################################################
	#Guardas puntos de deposito
	def save_dep(self):
		##Puntos de depositos
		#Rojo
		globales.DepoRojoX=[]
		globales.DepoRojoY=[]
		#Azul
		globales.DepoAzulX=[]
		globales.DepoAzulY=[]
		#Celeste
		globales.DepoCelX=[]
		globales.DepoCelY=[]
		for i in range(len(globales.Drojo)):
			globales.DepoRojoX.append(globales.Drojo[i][0])
			globales.DepoRojoY.append(globales.Drojo[i][1])
		for i in range(len(globales.Dazul)):
			globales.DepoAzulX.append(globales.Dazul[i][0])
			globales.DepoAzulY.append(globales.Dazul[i][1])
		for i in range(len(globales.Dceleste)):
			globales.DepoCelX.append(globales.Dceleste[i][0])
			globales.DepoCelY.append(globales.Dceleste[i][1])
		guardar_variable_total()
###################################################################################
###################################################################################
	#Borrar depositos completos
	def borrar_dep(self):

		globales.cuadricula_rojo=[]
		globales.Drojo=[]
		globales.cuadricula_azul=[]
		globales.Dazul=[]
		globales.cuadricula_celeste=[]
		globales.Dceleste=[]
###################################################################################
###################################################################################
	def mouseMoveEvent(self, event):
		if self.tabWidget.currentIndex()==2 or self.tabWidget.currentIndex()==3:
			if event.x()>=self.ptI[0] and event.x()<= self.ptF[0] and event.y()>=self.ptI[1] and event.y() <= self.ptF[1]:
				if self.tabWidget.currentIndex()==2 and globales.glineT==True:
					globales.Esc_p2=[event.x()-self.ptI[0],event.y()-self.ptI[1]]
				if self.tabWidget.currentIndex()==3 and globales.glineT==True:
					globales.Esc_p2=[event.x()-self.ptI[0],event.y()-self.ptI[1]]
###################################################################################
###################################################################################
	def mouseReleaseEvent(self, event):
		if self.tabWidget.currentIndex()==2 or self.tabWidget.currentIndex()==3:
			if event.x()>=self.ptI[0] and event.x()<= self.ptF[0] and event.y()>=self.ptI[1] and event.y() <= self.ptF[1]:
				if self.tabWidget.currentIndex()==2 and globales.glineT==True:
					globales.Esc_p2=[event.x()-self.ptI[0],event.y()-self.ptI[1]]
					globales.glineI=False
					globales.glineTT=True
					self.doubleSpinBox.setValue(math.sqrt((globales.Esc_p2[0]-globales.Esc_p1[0])*(globales.Esc_p2[0]-globales.Esc_p1[0])+(globales.Esc_p2[1]-globales.Esc_p1[1])*(globales.Esc_p2[1]-globales.Esc_p1[1])))
				elif self.tabWidget.currentIndex()==3 and globales.glineT==True:
					globales.Esc_p2=[event.x()-self.ptI[0],event.y()-self.ptI[1]]
					globales.glineI=False
					globales.glineTT=True
					aux_dist=math.sqrt((globales.Esc_p2[0]-globales.Esc_p1[0])*(globales.Esc_p2[0]-globales.Esc_p1[0])+(globales.Esc_p2[1]-globales.Esc_p1[1])*(globales.Esc_p2[1]-globales.Esc_p1[1]))
					aux_p=abs((globales.Esc_p2[0]-globales.Esc_p1[0])*(globales.Esc_p2[1]-globales.Esc_p1[1]))
					if self.toolBox.currentIndex()==0:
						self.doubleSpinBox_3.setValue(aux_p)
						globales.aG[self.comboBox.currentIndex()]=aux_p
					elif self.toolBox.currentIndex()==1:
						self.doubleSpinBox_4.setValue(aux_p)
						globales.aS[self.comboBox.currentIndex()]=aux_p
					elif self.toolBox.currentIndex()==2:
						self.doubleSpinBox_7.setValue(aux_dist)
						
						self.ch_mm()
					elif self.toolBox.currentIndex()==3:
						self.doubleSpinBox_10.setValue(aux_dist)
						
						self.ch_mm()
###################################################################################
###################################################################################
	def mousePressEvent(self, event):
		if self.tabWidget.currentIndex()==1 or self.tabWidget.currentIndex()==2 or self.tabWidget.currentIndex()==3:
			if event.button() == QtCore.Qt.LeftButton:
				if event.x()>=self.ptI[0] and event.x()<= self.ptF[0] and event.y()>=self.ptI[1] and event.y() <= self.ptF[1]:
					if self.tabWidget.currentIndex()==1:
						if self.radioButton_5.isChecked():
							#print(event.x()-self.ptI[0],event.y()-self.ptI[1])
							aux_selec=[]
							aux_selec=Buscar_pt_cuadricula(event.x()-self.ptI[0],event.y()-self.ptI[1],globales.cuadricula)

							if not (aux_selec[2] in globales.cuadricula_rojo):
								if not (aux_selec[2] in globales.cuadricula_azul):
									if not (aux_selec[2] in globales.cuadricula_celeste):
										globales.cuadricula_rojo.append(aux_selec[2])
										globales.Drojo.append([aux_selec[0],aux_selec[1]])
										
							else:
								globales.cuadricula_rojo.remove(aux_selec[2])
								globales.Drojo.remove([aux_selec[0],aux_selec[1]])
								

						if self.radioButton_6.isChecked():
							#print(event.x()-self.ptI[0],event.y()-self.ptI[1])
							aux_selec=[]
							aux_selec=Buscar_pt_cuadricula(event.x()-self.ptI[0],event.y()-self.ptI[1],globales.cuadricula)
							#print(aux_selec)

							if not (aux_selec[2] in globales.cuadricula_azul):
								if not (aux_selec[2] in globales.cuadricula_rojo):
									if not (aux_selec[2] in globales.cuadricula_celeste):
										globales.cuadricula_azul.append(aux_selec[2])
										globales.Dazul.append([aux_selec[0],aux_selec[1]])
							else:
								globales.cuadricula_azul.remove(aux_selec[2])
								globales.Dazul.remove([aux_selec[0],aux_selec[1]])

						if self.radioButton_7.isChecked():
							#print(event.x()-self.ptI[0],event.y()-self.ptI[1])
							aux_selec=[]
							aux_selec=Buscar_pt_cuadricula(event.x()-self.ptI[0],event.y()-self.ptI[1],globales.cuadricula)
							#print(aux_selec)

							if not (aux_selec[2] in globales.cuadricula_celeste):
								if not (aux_selec[2] in globales.cuadricula_rojo):
									if not (aux_selec[2] in globales.cuadricula_azul):
										globales.cuadricula_celeste.append(aux_selec[2])
										globales.Dceleste.append([aux_selec[0],aux_selec[1]])
							else:
								globales.cuadricula_celeste.remove(aux_selec[2])
								globales.Dceleste.remove([aux_selec[0],aux_selec[1]])

					elif self.tabWidget.currentIndex()==2:
						if globales.glineI==False and globales.glineTT==False:
							globales.Esc_p1=[event.x()-self.ptI[0],event.y()-self.ptI[1]]
							globales.Esc_p2=globales.Esc_p1
							globales.glineI=True
							globales.glineT=True
						else:
							globales.glineT=False
							globales.glineTT=False

					elif self.tabWidget.currentIndex()==3:

						if globales.glineI==False and globales.glineTT==False:
							globales.Esc_p1=[event.x()-self.ptI[0],event.y()-self.ptI[1]]
							globales.Esc_p2=globales.Esc_p1
							globales.glineI=True
							globales.glineT=True
						else:
							globales.glineT=False
							globales.glineTT=False
###################################################################################
###################################################################################
	def res_lim(self):
		self.spinBox.setValue(globales.limIz)
		self.spinBox_2.setValue(globales.limDe)
		self.spinBox_3.setValue(globales.limSup)
		self.spinBox_4.setValue(globales.limInf)
		self.spinBox_9.setValue(globales.Grid_mm)
		self.spinBox_10.setValue(globales.Grid_px)
###################################################################################
###################################################################################
	def save_var(self):
		globales.limIz=globales.capIz
		globales.limDe=globales.capDe
		globales.limSup=globales.capSu
		globales.limInf=globales.capInf
		globales.Grid_mm=globales.divH
		globales.Grid_px=globales.divV
		globales.cuadricula_rojo=[]
		globales.cuadricula_azul=[]
		globales.cuadricula_celeste=[]
		globales.DepoRojoX=[]
		globales.DepoRojoY=[]
		globales.DepoAzulX=[]
		globales.DepoAzulY=[]
		globales.DepoCelX=[]
		globales.DepoCelY=[]
		guardar_variable_total()
###################################################################################
###################################################################################
#Deteccion de cambio de grid px
	def ch_divv(self):
		globales.divV=self.spinBox_10.value()
		self.spinBox_9.setValue(globales.divV*globales.EscMM/globales.EscPix)
		globales.divH=self.spinBox_9.value()
###################################################################################
###################################################################################
#Deteccion de cambio de grid mm
	def ch_divh(self):
		globales.divH=self.spinBox_9.value()
		self.spinBox_10.setValue(globales.divH*globales.EscPix/globales.EscMM)
		globales.divV=self.spinBox_10.value()
###################################################################################
###################################################################################
#Deteccion de cambio de limite inferior
	def ch_inf(self):
		if self.spinBox_4.value()>self.spinBox_3.value():
			globales.capInf=self.spinBox_4.value()
		else:
			self.spinBox_4.setValue(self.spinBox_3.value()+1)
			globales.capInf=self.spinBox_4.value()
###################################################################################
###################################################################################
#Deteccion de cambio de limite Superior
	def ch_su(self):
		if self.spinBox_3.value()<self.spinBox_4.value():
			globales.capSu=self.spinBox_3.value()
		else:
			self.spinBox_3.setValue(self.spinBox_4.value()-1)
			globales.capSu=self.spinBox_3.value()
###################################################################################
###################################################################################
#Deteccion de cambio de limite derecho
	def ch_de(self):
		if self.spinBox_2.value()>self.spinBox.value():
			globales.capDe=self.spinBox_2.value()
		else:
			self.spinBox_2.setValue(self.spinBox.value()+1)
			globales.capDe=self.spinBox_2.value()
###################################################################################
###################################################################################
#Deteccion de cambio de limite izquierdo
	def ch_iz(self):
		if self.spinBox.value()<self.spinBox_2.value():
			globales.capIz=self.spinBox.value()
		else:
			self.spinBox.setValue(self.spinBox_2.value()-1)
			globales.capIz=self.spinBox.value()
###################################################################################
###################################################################################
	def Funciones_reloj(self):
		self.mostrar_cam()
		self.mostrar_fh()
###################################################################################
###################################################################################
	#Mostrar imagen
	def mostrar_cam(self):
		# Tomamos una captura desde la webcam.
		ok, img = self.captura.read()

 
		if not ok:
			return

		if self.tabWidget.currentIndex()==0:

			img_rect=img.copy()

			#Valores paara cuadricula
			aux_cuadricula=[]
			di=globales.capDe-globales.capIz
			dj=globales.capInf- globales.capSu
			dh=globales.divV
			dl=globales.divV
			n_aux=di/dh
			if n_aux > int(n_aux):
				n=int(n_aux)+1
			else:
				n=int(n_aux)
			m_aux=dj/dl
			if m_aux > int(m_aux):
				m=int(m_aux)+1
			else:
				m=int(m_aux)

			for i in range(m):
				
				for j in range(n):
					#aux_cuadricula.append([])
					limIx=dh*(j)+globales.capIz
					limIy=dl*(i)+globales.capSu
					limDx=dh*(j+1)+globales.capIz
					limDy=dl*(i+1)+globales.capSu

					if limDx<=globales.capDe and limDy<=globales.capInf:
						aux_cuadricula.append(([limIx,limIy],[limDx,limDy]))
						imag_rect = cv2.rectangle(img_rect,(limIx,limIy),(limDx,limDy),(255,0,0),1)
					elif limDx>globales.capDe and limDy<= globales.capInf:
						aux_cuadricula.append(([limIx,limIy],[globales.capDe,limDy]))
						imag_rect = cv2.rectangle(img_rect,(limIx,limIy),(globales.capDe,limDy),(255,0,0),1)
					elif limDx<=globales.capDe and limDy>globales.capInf:
						aux_cuadricula.append(([limIx,limIy],[limDx,globales.capInf]))
						imag_rect = cv2.rectangle(img_rect,(limIx,limIy),(limDx,globales.capInf),(255,0,0),1)
					else:
						aux_cuadricula.append(([limIx,limIy],[globales.capDe,globales.capInf]))
						imag_rect = cv2.rectangle(img_rect,(limIx,limIy),(globales.capDe,globales.capInf),(255,0,0),1)


			globales.cuadricula=aux_cuadricula

		elif self.tabWidget.currentIndex()==1:

			imag_rect=img.copy()
			imag_rect=cv2.rectangle(imag_rect.copy(), (0,0), (globales.capIz,globales.capInf), (255,255,255),-1)
			imag_rect=cv2.rectangle(imag_rect.copy(), (0,globales.capInf),(720,480), (255,255,255),-1)
			imag_rect=cv2.rectangle(imag_rect.copy(), (0,0), (720,globales.capSu), (255,255,255),-1)
			imag_rect=cv2.rectangle(imag_rect.copy(), (globales.capDe,globales.capSu), (720,480), (255,255,255),-1)

			imag_rect=form_cuadricula(imag_rect,globales.cuadricula)
			imag_rect=form_cuad_dep(imag_rect,globales.cuadricula,globales.cuadricula_rojo,0)
			imag_rect=form_cuad_dep(imag_rect,globales.cuadricula,globales.cuadricula_azul,1)
			imag_rect=form_cuad_dep(imag_rect,globales.cuadricula,globales.cuadricula_celeste,2)

		elif self.tabWidget.currentIndex()==2:

			imag_rect=img.copy()
			imag_rect=cv2.rectangle(imag_rect.copy(), (0,0), (globales.capIz,globales.capInf), (255,255,255),-1)
			imag_rect=cv2.rectangle(imag_rect.copy(), (0,globales.capInf),(720,480), (255,255,255),-1)
			imag_rect=cv2.rectangle(imag_rect.copy(), (0,0), (720,globales.capSu), (255,255,255),-1)
			imag_rect=cv2.rectangle(imag_rect.copy(), (globales.capDe,globales.capSu), (720,480), (255,255,255),-1)
			if globales.Esc_p1!=[] and globales.Esc_p2!=[]:
				if globales.glineT==True:
					imag_rect=cv2.line(imag_rect, (globales.Esc_p1[0],globales.Esc_p1[1]), (globales.Esc_p2[0],globales.Esc_p2[1]), (0,255,0),1)

		elif self.tabWidget.currentIndex()==3:

			imag_rect=img.copy()
			imag_rect=cv2.rectangle(imag_rect.copy(), (0,0), (globales.capIz,globales.capInf), (255,255,255),-1)
			imag_rect=cv2.rectangle(imag_rect.copy(), (0,globales.capInf),(720,480), (255,255,255),-1)
			imag_rect=cv2.rectangle(imag_rect.copy(), (0,0), (720,globales.capSu), (255,255,255),-1)
			imag_rect=cv2.rectangle(imag_rect.copy(), (globales.capDe,globales.capSu), (720,480), (255,255,255),-1)

			if globales.Esc_p1!=[] and globales.Esc_p2!=[]:
				if globales.glineT==True:
					aux_d=math.sqrt((globales.Esc_p2[0]-globales.Esc_p1[0])*(globales.Esc_p2[0]-globales.Esc_p1[0])+(globales.Esc_p2[1]-globales.Esc_p1[1])*(globales.Esc_p2[1]-globales.Esc_p1[1]))
					if self.toolBox.currentIndex()==0 or self.toolBox.currentIndex()==1:
						imag_rect=cv2.rectangle(imag_rect, (globales.Esc_p1[0],globales.Esc_p1[1]), (globales.Esc_p2[0],globales.Esc_p2[1]), (164,73,163),-1)
					if self.toolBox.currentIndex()==2 or self.toolBox.currentIndex()==3:
						imag_rect=cv2.line(imag_rect, (globales.Esc_p1[0],globales.Esc_p1[1]), (globales.Esc_p2[0],globales.Esc_p2[1]), (0,255,0),1)

		image = QtGui.QImage(imag_rect, imag_rect.shape[1], imag_rect.shape[0], imag_rect.shape[1] * imag_rect.shape[2], QtGui.QImage.Format_RGB888)
 
        # Creamos un pixmap a partir de la imagen.
        # OpenCV entraga los pixeles de la imagen en formato BGR en lugar del tradicional RGB,
        # por lo tanto tenemos que usar el metodo rgbSwapped() para que nos entregue una imagen con
        # los bytes Rojo y Azul intercambiados, y asi poder mostrar la imagen de forma correcta.
		pixmap = QtGui.QPixmap()
		pixmap.convertFromImage(image.rgbSwapped())
 
        # Mostramos el QPixmap en la QLabel.
		self.label_7.setPixmap(pixmap)
###################################################################################
###################################################################################
	def closeEvent(self, evnt):
		globales.aux_vent_config=0
		self.captura.release()
		self.Ventana_Inicio=Ui_configWindow()
		self.Ventana_Inicio.show()
###################################################################################
###################################################################################
	def mostrar_fh(self):
		self.label_hora.setText(QtCore.QDateTime.currentDateTime().toString("ddd hh:mm"))
		self.label_fecha.setText(QtCore.QDateTime.currentDateTime().toString("dd/MMM/yy"))
###################################################################################
###################################################################################
###################################################################################



###################################################################################
###################################################################################
########################VENTANA DE CONTROL#########################################
###################################################################################
class Ui_controlWindow(QtWidgets.QMainWindow, Ui_controlWindow):
	def __init__(self, *args, **kwargs):

		self.captura= cv2.VideoCapture(globales.tarjeta_camara)
		self.captura.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
		self.captura.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self) 
		self.statusbar.showMessage("Designers: Luis Allauca - Gabriel Guerra")
		self.timer = QtCore.QTimer(self)
		self.timer.setInterval(10)
		self.timer.timeout.connect(self.Funciones_reloj)
		self.timer.start()

		#Inicializar variables dimensiones
		init_cuad_obstaculos()
		self.spinBox.setValue(70)
		globales.n_omni=self.comboBox.currentIndex()+1

		#self.Ventana_config=Ui_configWindow()
		self.datos_tab=QtWidgets.QTableWidgetItem('-')
		self.tableWidget_3.setItem(0,0,self.datos_tab)
		self.datos_tab=QtWidgets.QTableWidgetItem('-')
		self.tableWidget_3.setItem(0,1,self.datos_tab)
		self.datos_tab=QtWidgets.QTableWidgetItem('-')
		self.tableWidget_3.setItem(0,2,self.datos_tab)
		self.datos_tab=QtWidgets.QTableWidgetItem('-')
		self.tableWidget_3.setItem(0,3,self.datos_tab)
		self.datos_tab=QtWidgets.QTableWidgetItem('-')

		#NODERED
		self.boton_node=0
		self.pushButton_15.clicked.connect(self.control_node)

		#Inicializar modo COntrol
		self.pub_opc_omni()
		self.pub_set_vel()
		#cambio de modo de control
		self.tabWidget.currentChanged.connect(self.pub_opc_omni)

		#Bandera para enviar un dato a omni
		self.dato_send=0
		#Velocidad
		self.spinBox.editingFinished.connect(self.pub_set_vel)
		self.comboBox.currentIndexChanged.connect(self.pub_init_omni_manual)

		###################################################
		#################MANUAL########################
		###Variables de omni##
		if globales.st_omni1==0:
			self.comboBox.model().item(0).setEnabled(False)
			if globales.st_omni3==1:
				self.comboBox.setCurrentIndex(2)
			if globales.st_omni2==1:
				self.comboBox.setCurrentIndex(1)
		if globales.st_omni2==0:
			self.comboBox.model().item(1).setEnabled(False)
		if globales.st_omni3==0:
			self.comboBox.model().item(2).setEnabled(False)


		#Boton Adelante
		self.pushButton_32.pressed.connect(self.pub_adelante)
		self.pushButton_32.released.connect(self.pub_parar)
		#Boton Atras
		self.pushButton_36.pressed.connect(self.pub_atras)
		self.pushButton_36.released.connect(self.pub_parar)
		#Boton Izquierda
		self.pushButton_30.pressed.connect(self.pub_izq)
		self.pushButton_30.released.connect(self.pub_parar)
		#Boton Derecha
		self.pushButton_35.pressed.connect(self.pub_der)
		self.pushButton_35.released.connect(self.pub_parar)
		#Boton antihorario
		self.pushButton_9.pressed.connect(self.pub_anh)
		self.pushButton_9.released.connect(self.pub_parar)
		#Boton Horario
		self.pushButton_16.pressed.connect(self.pub_hor)
		self.pushButton_16.released.connect(self.pub_parar)
		#Boton diag Sup der
		self.pushButton_33.pressed.connect(self.pub_dsd)
		self.pushButton_33.released.connect(self.pub_parar)
		#Boton diag Inf der
		self.pushButton_37.pressed.connect(self.pub_did)
		self.pushButton_37.released.connect(self.pub_parar)
		#Boton diag Inf izq
		self.pushButton_31.pressed.connect(self.pub_dii)
		self.pushButton_31.released.connect(self.pub_parar)
		#Boton diag Sup izq
		self.pushButton_8.pressed.connect(self.pub_dsi)
		self.pushButton_8.released.connect(self.pub_parar)
		#Boton Griper
		self.bot_gripper1=1
		self.bot_gripper2=1
		self.bot_gripper3=1
		self.pushButton_34.pressed.connect(self.pub_gripper)
		self.pushButton_34.released.connect(self.pub_parar)
		###################################################
		#################AUTOMATICO########################
		###Variables de omni##
		if globales.st_omni1==0:
			self.comboBox_2.model().item(0).setEnabled(False)
			if globales.st_omni3==1:
				self.comboBox_2.setCurrentIndex(2)
			if globales.st_omni2==1:
				self.comboBox_2.setCurrentIndex(1)
		if globales.st_omni2==0:
			self.comboBox_2.model().item(1).setEnabled(False)
		if globales.st_omni3==0:
			self.comboBox_2.model().item(2).setEnabled(False)

		###Eleccion de tipo de automatico
		#Variables de cuadro de imagen
		#Definir dimension de grafica
		self.ptI=[self.label_2.x()+globales.capIz, self.label_2.y()+22+globales.capSu]
		self.ptI_img=[self.label_2.x(), self.label_2.y()+22]
		self.ptF=[self.label_2.x()+globales.capDe,self.label_2.y()+22+globales.capInf]
		#punto a punto
		self.radioButton.clicked.connect(self.init_p2p)
		#trayectoria obstaculos simulados
		self.radioButton_2.clicked.connect(self.init_tos)
		#trayectoria deteccion obstaculos
		self.radioButton_3.clicked.connect(self.init_tra)
		#Simular clasificador
		self.radioButton_4.clicked.connect(self.init_csi)
		#clasificador
		self.radioButton_5.clicked.connect(self.init_cla)
		#Ingreso manual de coordenada
		self.spinBox_2.editingFinished.connect(self.ch_destx)
		self.spinBox_3.editingFinished.connect(self.ch_desty)
		#Cargar Puntos
		self.pushButton_10.clicked.connect(self.carg_dest)
		#Borrar puntos
		self.pushButton_18.clicked.connect(self.borrar_dest)
		#Iniciar proceso
		self.pushButton_14.clicked.connect(self.start_ac)
		#Contador de datos
		self.cont_imp=0
		#Guardar datos
		self.pushButton_29.clicked.connect(self.guardar_datos)
		self.pushButton_28.clicked.connect(self.parar_aut)
		self.pushButton_19.clicked.connect(self.cargar_obst)
		self.pushButton_21.clicked.connect(self.detectar_obst)



###################################################################################
############################AUTOMATICO#############################################
###################################################################################

############################CARGAR OBSTACULOS######################################
###################################################################################
	def detectar_obst(self):
		self.groupBox_2.setEnabled(False)
		self.groupBox_4.setEnabled(False)
		globales.pt_obs_x=[]
		globales.pt_obs_y=[]
		globales.pts_tray_obs=[]
		globales.pts_aux_obs_det=[]
		ok, img = self.captura.read()
		print('leyendo obstaculos')
		if not ok:
			return
		
		detectar_obstaculos(img.copy())
		globales.obst_pant=True
		for i in range(len(globales.pts_aux_obs_det)):
			pts_aux=CalcularXYZ(globales.pts_aux_obs_det[i][0],globales.pts_aux_obs_det[i][1])
			globales.pt_obs_x.append(int(pts_aux[0]))
			globales.pt_obs_y.append(int(pts_aux[1][0]))
			globales.pts_tray_obs.append([int(pts_aux[0]),int(pts_aux[1][0])])
		self.pushButton_14.setEnabled(True)
		self.groupBox_5.setEnabled(True)
		self.pushButton_28.setEnabled(True)

		if self.radioButton_5.isChecked():
			self.detectar_obj()
			globales.obj_cla_dib=True

############################DETECTAR OBJETOS DE CLASIFICACION######################
	def detectar_obj(self):
		globales.obj_rojo_real=[]
		globales.obj_azul_real=[]
		globales.obj_celeste_real=[]
		
		globales.pts_objetos=[]
		globales.datos_clasificador_coger=[]
		globales.datos_clasificador_colocar=[]
		globales.datos_clasificador_obstaculos=[]

		ok, img = self.captura.read()
		print('leyendo OBJETOS')
		if not ok:
			return
		img=cv2.rectangle(img.copy(), (0,0), (globales.capIz,globales.capInf), (255,255,255),-1)
		img=cv2.rectangle(img.copy(), (0,globales.capInf),(720,480), (255,255,255),-1)
		img=cv2.rectangle(img.copy(), (0,0), (720,globales.capSu), (255,255,255),-1)
		img=cv2.rectangle(img.copy(), (globales.capDe-20,globales.capSu), (720,480), (255,255,255),-1)
		
		detectar_objetos(img.copy())



############################CARGAR OBSTACULOS######################################
###################################################################################
	def cargar_obst(self):
		self.groupBox_2.setEnabled(False)
		self.groupBox_4.setEnabled(False)
		globales.pt_obs_x=[]
		globales.pt_obs_y=[]
		globales.pts_tray_obs=[]
		for i in range(len(globales.pts_aux_obs)):
			pts_aux=CalcularXYZ(globales.pts_aux_obs[i][0],globales.pts_aux_obs[i][1])
			globales.pt_obs_x.append(int(pts_aux[0]))
			globales.pt_obs_y.append(int(pts_aux[1][0]))
			globales.pts_tray_obs.append([int(pts_aux[0]),int(pts_aux[1][0])])

		if self.radioButton_2.isChecked():
			self.pushButton_14.setEnabled(True)
			self.groupBox_5.setEnabled(True)
			self.pushButton_28.setEnabled(True)
		elif self.radioButton_4.isChecked():
			self.groupBox_3.setEnabled(True)
			self.pushButton_14.setEnabled(True)
			self.groupBox_5.setEnabled(True)
			globales.grid_objetos=True
			globales.grid_obs=False
			
		
		


############################GUARDAR DATOS##########################################
###################################################################################
	def parar_aut(self):
		globales.opc_omni_1=0
		globales.opc_omni_2=0
		globales.opc_omni_3=0
		globales.opc_auto=0
		globales.n_omni=1
		vros.publicar_opc()
		globales.n_omni=2
		vros.publicar_opc()
		globales.n_omni=3
		vros.publicar_opc()
		self.groupBox_5.setEnabled(False)
		#globales.pts_aux_obs=[]
		#globales.cuad_obs=[]
		if self.radioButton.isChecked():
			self.init_p2p()
		elif self.radioButton_2.isChecked():
			self.init_tos()
		elif self.radioButton_3.isChecked():
			self.init_tra()
		elif self.radioButton_4.isChecked():
			self.init_csi()
		elif self.radioButton_5.isChecked():
			self.init_cla()
		self.pushButton_29.setEnabled(True)

############################GUARDAR DATOS##########################################
###################################################################################
	def guardar_datos(self):
		if self.radioButton.isChecked():
			guardar_datos_exp1(1,self.comboBox_2.currentIndex())
		elif self.radioButton_2.isChecked():
			
			if self.radioButton_7.isChecked():
				globales.tray_alg=1
			else:
				globales.tray_alg=0
			guardar_datos_exp1(2,self.comboBox_2.currentIndex())
		elif self.radioButton_3.isChecked():
			
			if self.radioButton_7.isChecked():
				globales.tray_alg=1
			else:
				globales.tray_alg=0
			guardar_datos_exp1(3,self.comboBox_2.currentIndex())


############################FUNCION AUTOMATICO#####################################
###################################################################################
	def control_automatico(self):
		if globales.opc_auto !=0:
			if globales.opc_auto==1:
				if self.comboBox_2.currentIndex()==0:
					if globales.car1_st==0:
						globales.opc_omni_1=1
						globales.n_omni=1
						print([globales.aut_omni1_x,globales.aut_omni1_y,globales.dir_omni_x,globales.dir_omni_y,globales.pt_destx,globales.pt_desty])
						globales.opc1_pto=[globales.aut_omni1_x,globales.aut_omni1_y]
						globales.opc1_dest=[globales.pt_destx,globales.pt_desty]
						vros.publicar_pts()
						time.sleep(0.5)
						vros.publicar_opc()
						globales.car1_st=10
					elif globales.car1_st==1:
						globales.opc_omni_1=0
						vros.publicar_opc()
						globales.n_omni=1
						globales.opc_auto=0
						globales.car1_st=0
						self.init_p2p()
						globales.opc1_ptf=[globales.aut_omni1_x,globales.aut_omni1_y]
						self.pushButton_28.setEnabled(False)
						self.pushButton_29.setEnabled(True)
				elif self.comboBox_2.currentIndex()==1:
					if globales.car2_st==0:
						globales.opc_omni_2=1
						globales.n_omni=2
						print([globales.aut_omni2_x,globales.aut_omni2_y,globales.dir_omni_x,globales.dir_omni_y,globales.pt_destx,globales.pt_desty])
						globales.opc1_pto=[globales.aut_omni2_x,globales.aut_omni2_y]
						globales.opc1_dest=[globales.pt_destx,globales.pt_desty]
						vros.publicar_pts()
						time.sleep(0.5)
						vros.publicar_opc()
						globales.car2_st=10
					elif globales.car2_st==1:
						globales.opc_omni_2=0
						vros.publicar_opc()
						globales.n_omni=1
						globales.opc_auto=0
						globales.car2_st=0
						self.init_p2p()
						globales.opc1_ptf=[globales.aut_omni2_x,globales.aut_omni2_y]
						self.pushButton_28.setEnabled(False)
						self.pushButton_29.setEnabled(True)
				elif self.comboBox_2.currentIndex()==2:
					if globales.car3_st==0:
						globales.opc_omni_3=1
						globales.n_omni=3
						print([globales.aut_omni3_x,globales.aut_omni3_y,globales.dir_omni_x,globales.dir_omni_y,globales.pt_destx,globales.pt_desty])
						globales.opc1_pto=[globales.aut_omni3_x,globales.aut_omni3_y]
						globales.opc1_dest=[globales.pt_destx,globales.pt_desty]
						vros.publicar_pts()
						time.sleep(0.5)
						vros.publicar_opc()
						globales.car3_st=10
					elif globales.car3_st==1:
						print('fin')
						globales.opc_omni_3=0
						vros.publicar_opc()
						globales.n_omni=1
						globales.opc_auto=0
						globales.car3_st=0
						self.init_p2p()
						globales.opc1_ptf=[globales.aut_omni3_x,globales.aut_omni3_y]
						self.pushButton_28.setEnabled(False)
						self.pushButton_29.setEnabled(True)
			elif globales.opc_auto==2 or globales.opc_auto==3:
				if globales.cont_tray<len(globales.tray_omni_x):
					if self.comboBox_2.currentIndex()==0:
						if globales.car1_st==0:
							globales.opc_omni_1=1
							globales.n_omni=1
							self.dir_omni()
							
							globales.pt_destx=globales.tray_omni_x[globales.cont_tray]
							globales.pt_desty=globales.tray_omni_y[globales.cont_tray]
							globales.pts_tray_aux_omni.append([globales.aut_omni1_x,globales.aut_omni1_y])
							globales.pts_tray_aux.append([globales.pt_destx,globales.pt_desty])
							#print(globales.tray_omni_x)
							#print(globales.tray_omni_y)
							#print([globales.aut_omni1_x,globales.aut_omni1_y,globales.dir_omni_x,globales.dir_omni_y,globales.pt_destx,globales.pt_desty])

							vros.publicar_pts()
							time.sleep(0.5)
							vros.publicar_opc()
							globales.car1_st=10
						elif globales.car1_st==1:
							globales.opc_omni_1=0
							vros.publicar_opc()
							globales.cont_tray=globales.cont_tray+1
							globales.car1_st=0
					if self.comboBox_2.currentIndex()==1:
						if globales.car2_st==0:
							globales.opc_omni_2=1
							globales.n_omni=2
							self.dir_omni()
							
							globales.pt_destx=globales.tray_omni_x[globales.cont_tray]
							globales.pt_desty=globales.tray_omni_y[globales.cont_tray]
							globales.pts_tray_aux_omni.append([globales.aut_omni2_x,globales.aut_omni2_y])
							globales.pts_tray_aux.append([globales.pt_destx,globales.pt_desty])
							#print([globales.aut_omni2_x,globales.aut_omni2_y,globales.dir_omni_x,globales.dir_omni_y,globales.pt_destx,globales.pt_desty])
							vros.publicar_pts()
							time.sleep(0.5)
							vros.publicar_opc()
							globales.car2_st=10
						elif globales.car2_st==1:
							globales.opc_omni_2=0
							vros.publicar_opc()
							globales.cont_tray=globales.cont_tray+1
							globales.car2_st=0
					if self.comboBox_2.currentIndex()==2:
						if globales.car3_st==0:
							globales.opc_omni_3=1
							globales.n_omni=3
							self.dir_omni()
							
							globales.pt_destx=globales.tray_omni_x[globales.cont_tray]
							globales.pt_desty=globales.tray_omni_y[globales.cont_tray]
							globales.pts_tray_aux_omni.append([globales.aut_omni3_x,globales.aut_omni3_y])
							globales.pts_tray_aux.append([globales.pt_destx,globales.pt_desty])
							#print([globales.aut_omni3_x,globales.aut_omni3_y,globales.dir_omni_x,globales.dir_omni_y,globales.pt_destx,globales.pt_desty])
							vros.publicar_pts()
							time.sleep(0.5)
							vros.publicar_opc()
							globales.car3_st=10
						elif globales.car3_st==1:
							globales.opc_omni_3=0
							vros.publicar_opc()
							globales.cont_tray=globales.cont_tray+1
							globales.car3_st=0
							

							
				else:
					if self.comboBox_2.currentIndex()==0:
						globales.opc_omni_1=0
						vros.publicar_opc()
						globales.cont_tray=-1
						globales.car1_st=0
						#globales.opc_auto=0
						globales.n_omni=1
						
						
						globales.pts_tray_aux_omni.append([globales.aut_omni1_x,globales.aut_omni1_y])
						#globales.pts_aux_obs=[]
						#globales.cuad_obs=[]
					elif self.comboBox_2.currentIndex()==1:
						globales.opc_omni_2=0
						vros.publicar_opc()
						globales.cont_tray=-1
						globales.car2_st=0
						#globales.opc_auto=0
						globales.n_omni=1
						
						
						globales.pts_tray_aux_omni.append([globales.aut_omni2_x,globales.aut_omni2_y])
						#globales.pts_aux_obs=[]
						#globales.cuad_obs=[]
					elif self.comboBox_2.currentIndex()==2:
						globales.opc_omni_3=0
						vros.publicar_opc()
						globales.cont_tray=-1
						globales.car3_st=0
						#globales.opc_auto=0
						globales.n_omni=1
						
						
						globales.pts_tray_aux_omni.append([globales.aut_omni3_x,globales.aut_omni3_y])
						#globales.pts_aux_obs=[]
						#globales.cuad_obs=[]
					
					if globales.opc_auto==2:
						globales.opc_auto=0
						self.init_tos()
						self.pushButton_28.setEnabled(False)
						self.pushButton_29.setEnabled(True)

					elif globales.opc_auto==3:
						globales.opc_auto=0
						self.init_tra()
						self.pushButton_28.setEnabled(False)
						self.pushButton_29.setEnabled(True)
			elif globales.opc_auto==4 or globales.opc_auto==5:
				#print(globales.obj_rojo_real)
				#print(globales.obj_azul_real)
				#print(globales.obj_celeste_real)
				if globales.obj_rojo_real==[] and globales.obj_azul_real==[] and globales.obj_celeste_real==[]:
					if globales.st_clasificador!=0:

						if not globales.clasificando_obj:
							if globales.st_clasificador==1:
								globales.st_clasificador=0
								globales.obj_cla_dib=False
							elif globales.st_clasificador==2:
								print('entro a colocar')
								self.colocar_obj_cla()
							elif globales.st_clasificador==3:
								self.retornar_cla()
						else:
							self.Clasificador_function()


						
					else:
						
						if globales.opc_auto==4:
						
							self.init_csi()
							self.pushButton_28.setEnabled(False)
							self.pushButton_29.setEnabled(True)
							globales.opc_auto=0

						elif globales.opc_auto==5:
							
							self.init_cla()
							self.pushButton_28.setEnabled(False)
							self.pushButton_29.setEnabled(True)
							globales.opc_auto=0
				else:
					if not globales.clasificando_obj:
						if globales.st_clasificador==1:
							globales.aux_dir_omni=[]
							self.select_obj_cla()
						elif globales.st_clasificador==2:
							self.colocar_obj_cla()
						elif globales.st_clasificador==3:
							self.retornar_cla()

					else:
						self.Clasificador_function()

						
								
								
############################FUNCION DE CLASIFICACION###############################
###################################################################################
	def Clasificador_function(self):
		if globales.cont_tray<len(globales.tray_omni_x)-1:
			if globales.n_omni_cla==1:
				if globales.car1_st==0:
					globales.opc_omni_1=1
					globales.n_omni=1
					self.dir_omni()
							
					globales.pt_destx=globales.tray_omni_x[globales.cont_tray]
					globales.pt_desty=globales.tray_omni_y[globales.cont_tray]
					globales.pts_tray_aux_omni.append([globales.aut_omni1_x,globales.aut_omni1_y])
					globales.pts_tray_aux.append([globales.pt_destx,globales.pt_desty])
					vros.publicar_pts()
					time.sleep(0.5)
					vros.publicar_opc()
					globales.car1_st=10
				elif globales.car1_st==1:
					globales.opc_omni_1=0
					vros.publicar_opc()
					globales.cont_tray=globales.cont_tray+1
					globales.car1_st=0
			if globales.n_omni_cla==2:
				if globales.car2_st==0:
					globales.opc_omni_2=1
					globales.n_omni=2
					self.dir_omni()
									
					globales.pt_destx=globales.tray_omni_x[globales.cont_tray]
					globales.pt_desty=globales.tray_omni_y[globales.cont_tray]
					globales.pts_tray_aux_omni.append([globales.aut_omni2_x,globales.aut_omni2_y])
					globales.pts_tray_aux.append([globales.pt_destx,globales.pt_desty])
				#print([globales.aut_omni2_x,globales.aut_omni2_y,globales.dir_omni_x,globales.dir_omni_y,globales.pt_destx,globales.pt_desty])
					vros.publicar_pts()
					time.sleep(0.5)
					vros.publicar_opc()
					globales.car2_st=10
				elif globales.car2_st==1:
					globales.opc_omni_2=0
					vros.publicar_opc()
					globales.cont_tray=globales.cont_tray+1
					globales.car2_st=0
			if globales.n_omni_cla==3:
				if globales.car3_st==0:
					globales.opc_omni_3=1
					globales.n_omni=3
					self.dir_omni()
								
					globales.pt_destx=globales.tray_omni_x[globales.cont_tray]
					globales.pt_desty=globales.tray_omni_y[globales.cont_tray]
					globales.pts_tray_aux_omni.append([globales.aut_omni3_x,globales.aut_omni3_y])
					globales.pts_tray_aux.append([globales.pt_destx,globales.pt_desty])
					#print([globales.aut_omni3_x,globales.aut_omni3_y,globales.dir_omni_x,globales.dir_omni_y,globales.pt_destx,globales.pt_desty])
					vros.publicar_pts()
					time.sleep(0.5)
					vros.publicar_opc()
					globales.car3_st=10
				elif globales.car3_st==1:
					globales.opc_omni_3=0
					vros.publicar_opc()
					globales.cont_tray=globales.cont_tray+1
					globales.car3_st=0
									

									
		else:
			if globales.cont_tray<len(globales.tray_omni_x):
				if globales.st_clasificador==1:
					opc_aux_act=2
					#time.sleep(1)
				elif globales.st_clasificador==2:
					opc_aux_act=3
					#time.sleep(1)
				elif globales.st_clasificador==3:
					opc_aux_act=1

				if globales.n_omni_cla==1:
					if globales.car1_st==0:

						globales.opc_omni_1=opc_aux_act
						globales.n_omni=1
						self.dir_omni()
										
						globales.pt_destx=globales.tray_omni_x[globales.cont_tray]
						globales.pt_desty=globales.tray_omni_y[globales.cont_tray]
						globales.pts_tray_aux_omni.append([globales.aut_omni1_x,globales.aut_omni1_y])
						globales.pts_tray_aux.append([globales.pt_destx,globales.pt_desty])
						vros.publicar_pts()
						time.sleep(0.5)
						vros.publicar_opc()
						globales.car1_st=10
					elif globales.car1_st==1:
						globales.opc_omni_1=0
						vros.publicar_opc()
						globales.cont_tray=globales.cont_tray+1
						globales.car1_st=0
				if globales.n_omni_cla==2:
					if globales.car2_st==0:
						globales.opc_omni_2=opc_aux_act
						globales.n_omni=2
						self.dir_omni()
										
						globales.pt_destx=globales.tray_omni_x[globales.cont_tray]
						globales.pt_desty=globales.tray_omni_y[globales.cont_tray]
						globales.pts_tray_aux_omni.append([globales.aut_omni2_x,globales.aut_omni2_y])
						globales.pts_tray_aux.append([globales.pt_destx,globales.pt_desty])
						#print([globales.aut_omni2_x,globales.aut_omni2_y,globales.dir_omni_x,globales.dir_omni_y,globales.pt_destx,globales.pt_desty])
						vros.publicar_pts()
						time.sleep(0.5)
						vros.publicar_opc()
						globales.car2_st=10
					elif globales.car2_st==1:
						globales.opc_omni_2=0
						vros.publicar_opc()
						globales.cont_tray=globales.cont_tray+1
						globales.car2_st=0
				if globales.n_omni_cla==3:
					if globales.car3_st==0:
						globales.opc_omni_3=opc_aux_act
						globales.n_omni=3
						self.dir_omni()
										
						globales.pt_destx=globales.tray_omni_x[globales.cont_tray]
						globales.pt_desty=globales.tray_omni_y[globales.cont_tray]
						globales.pts_tray_aux_omni.append([globales.aut_omni3_x,globales.aut_omni3_y])
						globales.pts_tray_aux.append([globales.pt_destx,globales.pt_desty])
						#print([globales.aut_omni3_x,globales.aut_omni3_y,globales.dir_omni_x,globales.dir_omni_y,globales.pt_destx,globales.pt_desty])
						vros.publicar_pts()
						time.sleep(0.5)
						vros.publicar_opc()
						globales.car3_st=10
					elif globales.car3_st==1:
						globales.opc_omni_3=0
						vros.publicar_opc()
						globales.cont_tray=globales.cont_tray+1
						globales.car3_st=0
										
			else:

				if globales.n_omni_cla==1:
					globales.opc_omni_1=0
					vros.publicar_opc()
					globales.cont_tray=-1
					globales.car1_st=0
					#globales.opc_auto=0
					#globales.n_omni=1
									
									
					globales.pts_tray_aux_omni.append([globales.aut_omni1_x,globales.aut_omni1_y])
					#globales.pts_aux_obs=[]
					#globales.cuad_obs=[]
				elif globales.n_omni_cla==2:
					globales.opc_omni_2=0
					vros.publicar_opc()
					globales.cont_tray=-1
					globales.car2_st=0
					#globales.opc_auto=0
					#globales.n_omni=1
									
									
					globales.pts_tray_aux_omni.append([globales.aut_omni2_x,globales.aut_omni2_y])
					#globales.pts_aux_obs=[]
					#globales.cuad_obs=[]
				elif globales.n_omni_cla==3:
					globales.opc_omni_3=0
					vros.publicar_opc()
					globales.cont_tray=-1
					globales.car3_st=0
					#globales.opc_auto=0
					#globales.n_omni=1
					
									
					globales.pts_tray_aux_omni.append([globales.aut_omni3_x,globales.aut_omni3_y])
					#globales.pts_aux_obs=[]
					#globales.cuad_obs=[]
				if globales.st_clasificador==1:
					globales.datos_clasificador_coger.append([globales.pts_tray_aux_omni,globales.pts_tray_aux])
					globales.st_clasificador=2
					if globales.color_obj==1:
						if self.radioButton_5.isChecked():
							globales.point_obj_rojo.pop(globales.cont_obj_sim)
						else:
							globales.cuad_obj_rojos.pop(globales.cont_obj_sim)
							globales.obj_rojos.pop(globales.cont_obj_sim)
					elif globales.color_obj==2:
						if self.radioButton_5.isChecked():
							globales.point_obj_azul.pop(globales.cont_obj_sim)
						else:
							globales.cuad_obj_azul.pop(globales.cont_obj_sim)
							globales.obj_azul.pop(globales.cont_obj_sim)
					elif globales.color_obj==3:
						if self.radioButton_5.isChecked():
							globales.point_obj_celeste.pop(globales.cont_obj_sim)
						else:
							globales.cuad_obj_celeste.pop(globales.cont_obj_sim)
							globales.obj_celeste.pop(globales.cont_obj_sim)
					print('fin de atrapar')
					globales.clasificando_obj=False
				elif globales.st_clasificador==2:
					globales.datos_clasificador_colocar.append([globales.pts_tray_aux_omni,globales.pts_tray_aux])
					globales.st_clasificador=3
					print('fin de colocar')
					globales.clasificando_obj=False
				elif globales.st_clasificador==3:
					globales.datos_clasificador_obstaculos.append([globales.pt_obs_cla_x,globales.pt_obs_cla_y])
					globales.st_clasificador=1
					print('fin de retorno')
					globales.clasificando_obj=False
					
					

				

############################INICIAR ACCION AUTOMAT#################################
###################################################################################
	def start_ac(self):
		self.groupBox_2.setEnabled(False)
		self.groupBox_4.setEnabled(False)
		self.groupBox_3.setEnabled(False)
		self.comboBox_2.setEnabled(False)
		self.pushButton_14.setEnabled(False)
		self.pushButton_28.setEnabled(True)
		self.groupBox_5.setEnabled(False)

		if self.radioButton.isChecked():
			globales.opc_auto=1
			
		elif self.radioButton_2.isChecked():

			if self.comboBox_2.currentIndex()==0:
				ppxx=globales.aut_omni1_x
				ppyy=globales.aut_omni1_y
			elif self.comboBox_2.currentIndex()==1:
				ppxx=globales.aut_omni2_x
				ppyy=globales.aut_omni2_y
			elif self.comboBox_2.currentIndex()==2:
				ppxx=globales.aut_omni3_x
				ppyy=globales.aut_omni3_y
			if self.radioButton_6.isChecked():
				globales.tray_omni_x,globales.tray_omni_y=calcular_ruta_campos(ppxx,ppyy,globales.pt_destx,globales.pt_desty,globales.pt_obs_x,globales.pt_obs_y)
			elif self.radioButton_7.isChecked():
				globales.tray_omni_x,globales.tray_omni_y=calcular_ruta_AS(ppxx,ppyy,globales.pt_destx,globales.pt_desty,globales.pt_obs_x,globales.pt_obs_y)


			globales.pts_tray_aux_omni=[]
			globales.pts_tray_aux=[]
			globales.pts_tray_aux.append([ppxx,ppyy])
			#print([ppxx,ppyy])
			#print([globales.pt_destx,globales.pt_desty])
			#print(globales.tray_omni_x,globales.tray_omni_y)
			#print(globales.pt_obs_x,globales.pt_obs_y)
			#print([globales.aut_omni3_x,globales.aut_omni3_y,globales.dir_omni_x,globales.dir_omni_y,globales.pt_destx,globales.pt_desty])
			globales.cont_tray=0
			globales.opc_auto=2

		elif self.radioButton_3.isChecked():
			if self.comboBox_2.currentIndex()==0:
				ppxx=globales.aut_omni1_x
				ppyy=globales.aut_omni1_y
			elif self.comboBox_2.currentIndex()==1:
				ppxx=globales.aut_omni2_x
				ppyy=globales.aut_omni2_y
			elif self.comboBox_2.currentIndex()==2:
				ppxx=globales.aut_omni3_x
				ppyy=globales.aut_omni3_y
			if self.radioButton_6.isChecked():
				globales.tray_omni_x,globales.tray_omni_y=calcular_ruta_campos(ppxx,ppyy,globales.pt_destx,globales.pt_desty,globales.pt_obs_x,globales.pt_obs_y)
			elif self.radioButton_7.isChecked():
				globales.tray_omni_x,globales.tray_omni_y=calcular_ruta_AS(ppxx,ppyy,globales.pt_destx,globales.pt_desty,globales.pt_obs_x,globales.pt_obs_y)


			globales.pts_tray_aux_omni=[]
			globales.pts_tray_aux=[]
			globales.pts_tray_aux.append([ppxx,ppyy])
			globales.cont_tray=0
			globales.opc_auto=3

		elif self.radioButton_4.isChecked():
			globales.pts_objetos=[]
			globales.obj_rojo_real=[]
			globales.obj_azul_real=[]
			globales.obj_celeste_real=[]
			for i in range(len(globales.obj_rojos)):
				pts=CalcularXYZ(globales.obj_rojos[i][0],globales.obj_rojos[i][1])
				globales.obj_rojo_real.append([int(pts[0]),int(pts[1][0])])
			for i in range(len(globales.obj_azul)):
				pts=CalcularXYZ(globales.obj_azul[i][0],globales.obj_azul[i][1])
				globales.obj_azul_real.append([int(pts[0]),int(pts[1][0])])
			for i in range(len(globales.obj_celeste)):
				pts=CalcularXYZ(globales.obj_celeste[i][0],globales.obj_celeste[i][1])
				globales.obj_celeste_real.append([int(pts[0]),int(pts[1][0])])
			globales.pts_objetos=[]
			globales.datos_clasificador_coger=[]
			globales.datos_clasificador_colocar=[]
			globales.datos_clasificador_obstaculos=[]

			globales.st_clasificador=1
			globales.cont_tray=0
			globales.opc_auto=4
		elif self.radioButton_5.isChecked():
			globales.pts_objetos=[]
			globales.datos_clasificador_coger=[]
			globales.datos_clasificador_colocar=[]
			globales.datos_clasificador_obstaculos=[]

			globales.st_clasificador=1
			globales.cont_tray=0
			globales.opc_auto=5



############################REGRESAR A ORIGEN######################################
###################################################################################
	def retornar_cla(self):
		if globales.n_omni_cla==1:
			ppxx=globales.aut_omni1_x
			ppyy=globales.aut_omni1_y	
		elif globales.n_omni_cla==2:
			ppxx=globales.aut_omni2_x
			ppyy=globales.aut_omni2_y
		elif globales.n_omni_cla==3:
			ppxx=globales.aut_omni3_x
			ppyy=globales.aut_omni3_y
		
		globales.pt_destx=globales.pts_origin[0]
		globales.pt_desty=globales.pts_origin[1]
		print('------')
		print(globales.pt_destx,globales.pt_desty)
		print('------')
		const_obs_cla()
		print(globales.pt_obs_cla_x)
		print(globales.pt_obs_cla_y)
		
		if self.radioButton_6.isChecked():
			aux11=ppxx
			aux12=ppyy
			aux13=globales.pt_destx
			aux14=globales.pt_desty
			aux15=globales.pt_obs_cla_x
			aux16=globales.pt_obs_cla_y
			aux21=ppxx
			aux22=ppyy
			aux23=globales.pt_destx
			aux24=globales.pt_desty
			aux25=globales.pt_obs_cla_x
			aux26=globales.pt_obs_cla_y
			globales.tray_omni_x,globales.tray_omni_y=calcular_ruta_campos(aux11,aux12,aux13,aux14,aux15,aux16)
			if globales.tray_omni_x==[]:
				globales.tray_omni_x,globales.tray_omni_y=calcular_ruta_AS(aux21,aux22,aux23,aux24,aux25,aux26)
		elif self.radioButton_7.isChecked():
			globales.tray_omni_x,globales.tray_omni_y=calcular_ruta_AS(ppxx,ppyy,globales.pt_destx,globales.pt_desty,globales.pt_obs_cla_x,globales.pt_obs_cla_y)


		globales.pts_tray_aux_omni=[]
		globales.pts_tray_aux=[]
		globales.pts_tray_aux.append([ppxx,ppyy])
		globales.clasificando_obj=True
		globales.cont_tray=0

############################COLOCAR OBJETO#########################################
###################################################################################

	def colocar_obj_cla(self):
		if globales.n_omni_cla==1:
			ppxx=globales.aut_omni1_x
			ppyy=globales.aut_omni1_y
		elif globales.n_omni_cla==2:
			ppxx=globales.aut_omni2_x
			ppyy=globales.aut_omni2_y
		elif globales.n_omni_cla==3:
			ppxx=globales.aut_omni3_x
			ppyy=globales.aut_omni3_y
		#globales.pts_origin=[ppxx,ppyy]
		if globales.color_obj==1:
			pts=CalcularXYZ(globales.DepoRojoX[0],globales.DepoRojoY[0])
			globales.pt_destx=int(pts[0])
			globales.pt_desty=int(pts[1][0])
		elif globales.color_obj==2:
			pts=CalcularXYZ(globales.DepoAzulX[0],globales.DepoAzulY[0])
			globales.pt_destx=int(pts[0])
			globales.pt_desty=int(pts[1][0])
		elif globales.color_obj==3:
			pts=CalcularXYZ(globales.DepoCelX[0],globales.DepoCelY[0])
			globales.pt_destx=int(pts[0])
			globales.pt_desty=int(pts[1][0])
		const_obs_cla()
		print(globales.pt_obs_cla_x)
		print(globales.pt_obs_cla_y)
		
		if self.radioButton_6.isChecked():
			aux11=ppxx
			aux12=ppyy
			aux13=globales.pt_destx
			aux14=globales.pt_desty
			aux15=globales.pt_obs_cla_x
			aux16=globales.pt_obs_cla_y
			aux21=ppxx
			aux22=ppyy
			aux23=globales.pt_destx
			aux24=globales.pt_desty
			aux25=globales.pt_obs_cla_x
			aux26=globales.pt_obs_cla_y
			globales.tray_omni_x,globales.tray_omni_y=calcular_ruta_campos(aux11,aux12,aux13,aux14,aux15,aux16)
			if globales.tray_omni_x==[]:
				globales.tray_omni_x,globales.tray_omni_y=calcular_ruta_AS(aux21,aux22,aux23,aux24,aux25,aux26)
		elif self.radioButton_7.isChecked():
			globales.tray_omni_x,globales.tray_omni_y=calcular_ruta_AS(ppxx,ppyy,globales.pt_destx,globales.pt_desty,globales.pt_obs_cla_x,globales.pt_obs_cla_y)


		globales.pts_tray_aux_omni=[]
		globales.pts_tray_aux=[]
		globales.pts_tray_aux.append([ppxx,ppyy])
		globales.clasificando_obj=True
		globales.cont_tray=0

############################SELECCIONAR OBJETO#####################################
###################################################################################

	def select_obj_cla(self):
		globales.pts_origin=[]
		
		if globales.st_omni1==1:
			ppxx1=globales.aut_omni1_x
			ppyy1=globales.aut_omni1_y
		else:
			ppxx1=-100000
			ppyy1=-100000
		if globales.st_omni2==1:
			ppxx2=globales.aut_omni2_x
			ppyy2=globales.aut_omni2_y
		else:
			ppxx2=-100000
			ppyy2=-100000
		if globales.st_omni3==1:
			ppxx3=globales.aut_omni3_x
			ppyy3=globales.aut_omni3_y
		else:
			ppxx3=-100000
			ppyy3=-100000
		pts_omnis=[[ppxx1,ppyy1],[ppxx2,ppyy2],[ppxx3,ppyy3]]
		print('Objetos iniciales')
		print(globales.obj_rojo_real)
		print(globales.obj_azul_real)
		print(globales.obj_celeste_real)
		globales.pt_destx,globales.pt_desty, globales.color_obj, globales.n_omni_cla,globales.obj_rojo_real,globales.obj_azul_real,globales.obj_celeste_real, globales.cont_obj_sim=pln.ruta_corta_plan(pts_omnis, globales.obj_rojo_real, globales.obj_azul_real, globales.obj_celeste_real)
		print('Objetos despues de algoritmo')
		print(globales.obj_rojo_real)
		print(globales.obj_azul_real)
		print(globales.obj_celeste_real)
		print('-----------')
		if globales.n_omni_cla==1:
			ppxx=globales.aut_omni1_x
			ppyy=globales.aut_omni1_y

		elif globales.n_omni_cla==2:
			ppxx=globales.aut_omni2_x
			ppyy=globales.aut_omni2_y
		elif globales.n_omni_cla==3:
			ppxx=globales.aut_omni3_x
			ppyy=globales.aut_omni3_y
		globales.pts_objetos.append([globales.n_omni_cla,globales.color_obj,globales.pt_destx,globales.pt_desty])
		globales.pts_origin=[ppxx,ppyy]
		

		#Formacion de obstaculos
		
		const_obs_cla()
		print(globales.pt_obs_cla_x)
		print(globales.pt_obs_cla_y)

		"""print([ppxx,ppyy])
		print([globales.pt_destx,globales.pt_desty])
		print([globales.pt_obs_cla_x,globales.pt_obs_cla_y])"""

		if self.radioButton_6.isChecked():
			aux11=ppxx
			aux12=ppyy
			aux13=globales.pt_destx
			aux14=globales.pt_desty
			aux15=globales.pt_obs_cla_x
			aux16=globales.pt_obs_cla_y
			aux21=ppxx
			aux22=ppyy
			aux23=globales.pt_destx
			aux24=globales.pt_desty
			aux25=globales.pt_obs_cla_x
			aux26=globales.pt_obs_cla_y
			globales.tray_omni_x,globales.tray_omni_y=calcular_ruta_campos(aux11,aux12,aux13,aux14,aux15,aux16)
			if globales.tray_omni_x==[]:
				globales.tray_omni_x,globales.tray_omni_y=calcular_ruta_AS(aux21,aux22,aux23,aux24,aux25,aux26)
		elif self.radioButton_7.isChecked():
			globales.tray_omni_x,globales.tray_omni_y=calcular_ruta_AS(ppxx,ppyy,globales.pt_destx,globales.pt_desty,globales.pt_obs_cla_x,globales.pt_obs_cla_y)

		globales.pts_tray_aux_omni=[]
		globales.pts_tray_aux=[]
		globales.pts_tray_aux.append([ppxx,ppyy])
		globales.clasificando_obj=True
		globales.n_omni=globales.n_omni_cla
		globales.cont_tray=0
		
	

############################DETECTAR OMNI##########################################
###################################################################################
	def dir_omni(self):

		aux_dirr=[]
		n_omni_=7
		if globales.opc_auto==4 or globales.opc_auto==5:
			if globales.n_omni_cla==1:
				n_omni_=globales.st_omni1
			elif globales.n_omni_cla==2:
				n_omni_=globales.st_omni2
			elif globales.n_omni_cla==3:
				n_omni_=globales.st_omni3
		else:
			if self.comboBox_2.currentIndex()==0:
				n_omni_=globales.st_omni1
			elif self.comboBox_2.currentIndex()==1:
				n_omni_=globales.st_omni2
			elif self.comboBox_2.currentIndex()==2:
				n_omni_=globales.st_omni3
		if n_omni_==1:
		
			cont_dir=0
			while len(aux_dirr) != 2 and cont_dir<1000 :
				print('leyendo dir')
				print(globales.n_omni_cla)
				ok, img = self.captura.read()

		 
				if not ok:
					return
				imag_rect=img.copy()
				imag_rect=cv2.rectangle(imag_rect.copy(), (0,0), (globales.capIz,globales.capInf), (255,255,255),-1)
				imag_rect=cv2.rectangle(imag_rect.copy(), (0,globales.capInf),(720,480), (255,255,255),-1)
				imag_rect=cv2.rectangle(imag_rect.copy(), (0,0), (720,globales.capSu), (255,255,255),-1)
				imag_rect=cv2.rectangle(imag_rect.copy(), (globales.capDe,globales.capSu), (720,480), (255,255,255),-1)
				if globales.opc_auto==4 or globales.opc_auto==5:
					aux_dirr=detectar_dir_n_omni(imag_rect.copy(),globales.n_omni_cla-1)
				else:
					aux_dirr=detectar_dir_n_omni(imag_rect.copy(),self.comboBox_2.currentIndex())

			if cont_dir>=1000 and globales.aux_dir_omni!=[]:
				globales.dir_omni_x=globales.aux_dir_omni[0]
				globales.dir_omni_y=globales.aux_dir_omni[1]
			else:
				globales.dir_omni_x=aux_dirr[0]
				globales.dir_omni_y=aux_dirr[1]
				globales.aux_dir_omni=[aux_dirr[0],aux_dirr[1]]
			print(aux_dirr)

############################Borrar DATOS DE DEST.#################################
###################################################################################
	def borrar_dest(self):
		self.pushButton_29.setEnabled(False)
		globales.aux_ppx_pt_destx=-10000
		globales.aux_ppx_pt_desty=-10000
		globales.punto_mouse=[]
		globales.punto_mouse_rea=[]
		self.pushButton_18.setEnabled(False)
		self.pushButton_10.setEnabled(True)

		self.pushButton_14.setEnabled(True)
		self.spinBox_2.setEnabled(True)
		self.spinBox_3.setEnabled(True)
		self.groupBox_5.setEnabled(False)
		if self.radioButton_2.isChecked():
			self.groupBox_4.setEnabled(False)
			globales.grid_obs=False

############################GUARDAR DATOS DE DEST.#################################
###################################################################################
	def carg_dest(self):
		self.pushButton_29.setEnabled(False)

		globales.aux_dir_omni=[]
		aux_dirr=[]
		n_omni_=7
		if self.comboBox_2.currentIndex()==0:
			n_omni_=globales.st_omni1
		elif self.comboBox_2.currentIndex()==1:
			n_omni_=globales.st_omni2
		elif self.comboBox_2.currentIndex()==2:
			n_omni_=globales.st_omni3
		if n_omni_==1:

			globales.pt_destx=globales.aux_pt_destx
			globales.pt_desty=globales.aux_pt_desty
			globales.aux_ppx_pt_destx=-10000
			globales.aux_ppx_pt_desty=-10000
			globales.punto_mouse=[]
			globales.punto_mouse_rea=[]


			self.pushButton_18.setEnabled(True)
			self.pushButton_10.setEnabled(False)
			self.spinBox_2.setEnabled(False)
			self.spinBox_3.setEnabled(False)
			# Tomamos una captura desde la webcam.
			#cont_dir=0
			while len(aux_dirr) != 2:
				ok, img = self.captura.read()
				print('leyendo dir')
				#cont_dir=cont_dir+1
		 
				if not ok:
					return
				imag_rect=img.copy()
				imag_rect=cv2.rectangle(imag_rect.copy(), (0,0), (globales.capIz,globales.capInf), (255,255,255),-1)
				imag_rect=cv2.rectangle(imag_rect.copy(), (0,globales.capInf),(720,480), (255,255,255),-1)
				imag_rect=cv2.rectangle(imag_rect.copy(), (0,0), (720,globales.capSu), (255,255,255),-1)
				imag_rect=cv2.rectangle(imag_rect.copy(), (globales.capDe,globales.capSu), (720,480), (255,255,255),-1)

				aux_dirr=detectar_dir_n_omni(imag_rect.copy(),self.comboBox_2.currentIndex())

			globales.dir_omni_x=aux_dirr[0]
			globales.dir_omni_y=aux_dirr[1]
			globales.aux_dir_omni=[aux_dirr[0],aux_dirr[1]]
			print(aux_dirr)


			if self.radioButton.isChecked():
				globales.grid_obs=False
				self.pushButton_14.setEnabled(True)
				
			elif self.radioButton_2.isChecked():
				self.groupBox_4.setEnabled(True)
				self.pushButton_19.setEnabled(True)
				self.pushButton_21.setEnabled(False)
				globales.grid_obs=True

			elif self.radioButton_3.isChecked():
				self.groupBox_4.setEnabled(True)
				self.pushButton_19.setEnabled(False)
				self.pushButton_21.setEnabled(True)
				globales.grid_obs=False




############################INGRESO MANUAL X Y DEST.###############################
###################################################################################
	def ch_destx(self):
		globales.aux_ppx_pt_destx=globales.capIz
		globales.aux_ppx_pt_desty=globales.capSu
		globales.aux_pt_destx=self.spinBox_2.value()
		globales.aux_pt_desty=self.spinBox_3.value()
		globales.punto_mouse=[]
		globales.punto_mouse_rea=[]
	def ch_desty(self):
		globales.aux_ppx_pt_destx=globales.capIz
		globales.aux_ppx_pt_desty=globales.capSu
		globales.aux_pt_destx=self.spinBox_2.value()
		globales.aux_pt_desty=self.spinBox_3.value()
		globales.punto_mouse=[]
		globales.punto_mouse_rea=[]


############################EVENTO RELEASEON#######################################
###################################################################################

	def mouseReleaseEvent(self, event):
		if self.tabWidget.currentIndex()==1:
				if self.radioButton.isChecked() or self.radioButton_2.isChecked() or  self.radioButton_3.isChecked() or self.radioButton_4.isChecked():
					if self.groupBox_2.isEnabled() or self.groupBox_3.isEnabled() or self.groupBox_4.isEnabled():
						if event.x()>=self.ptI[0] and event.x()<= self.ptF[0] and event.y()>=self.ptI[1] and event.y() <= self.ptF[1]:
							if self.groupBox_2.isEnabled() and self.pushButton_10.isEnabled():
								globales.aux_ppx_pt_destx=event.x()-self.ptI_img[0]
								globales.aux_ppx_pt_desty=event.y()-self.ptI_img[1]
								pts_aux=CalcularXYZ(globales.aux_ppx_pt_destx,globales.aux_ppx_pt_desty)
								globales.aux_pt_destx=int(pts_aux[0])
								globales.aux_pt_desty=int(pts_aux[1][0])
								self.spinBox_2.setValue(int(pts_aux[0]))
								self.spinBox_3.setValue(int(pts_aux[1][0]))
								globales.punto_mouse=[]
								globales.punto_mouse_rea=[]


		

############################EVENTO MOV RATON########################################
###################################################################################
	def mouseMoveEvent(self, event):
		if self.tabWidget.currentIndex()==1:
			if self.radioButton.isChecked() or self.radioButton_2.isChecked() or  self.radioButton_3.isChecked() or self.radioButton_4.isChecked():
				if self.groupBox_2.isEnabled() or self.groupBox_3.isEnabled() or self.groupBox_4.isEnabled():
					
					if event.x()>=self.ptI[0] and event.x()<= self.ptF[0] and event.y()>=self.ptI[1] and event.y() <= self.ptF[1]:
						if self.groupBox_2.isEnabled() and self.pushButton_10.isEnabled():
							globales.punto_mouse=[event.x()-self.ptI_img[0],event.y()-self.ptI_img[1]]
							pts_aux=CalcularXYZ(globales.punto_mouse[0],globales.punto_mouse[1])
							globales.punto_mouse_real=[int(pts_aux[0]),int(pts_aux[1][0])]
							#print(globales.punto_mouse_real)
								
					else:
						globales.punto_mouse=[]
						globales.punto_mouse_rea=[]

########################EVENTO DE MOUSE CLICK######################################
###################################################################################
	def mousePressEvent(self, event):
		if self.tabWidget.currentIndex()==1:
			if self.radioButton.isChecked() or self.radioButton_2.isChecked() or  self.radioButton_3.isChecked() or self.radioButton_4.isChecked():
				if self.groupBox_2.isEnabled() or self.groupBox_3.isEnabled() or self.groupBox_4.isEnabled():
					if event.button() == QtCore.Qt.LeftButton:
						if event.x()>=self.ptI[0] and event.x()<= self.ptF[0] and event.y()>=self.ptI[1] and event.y() <= self.ptF[1]:
							if self.groupBox_2.isEnabled() and self.pushButton_10.isEnabled():
								globales.aux_ppx_pt_destx=event.x()-self.ptI_img[0]
								globales.aux_ppx_pt_desty=event.y()-self.ptI_img[1]
								pts_aux=CalcularXYZ(globales.aux_ppx_pt_destx,globales.aux_ppx_pt_desty)
								globales.aux_pt_destx=int(pts_aux[0])
								globales.aux_pt_desty=int(pts_aux[1][0])
								self.spinBox_2.setValue(int(pts_aux[0]))
								self.spinBox_3.setValue(int(pts_aux[1][0]))
								globales.punto_mouse=[]
								globales.punto_mouse_real=[]
							elif globales.grid_obs:
								aux_selec=Buscar_pt_cuadricula(event.x()-self.ptI_img[0],event.y()-self.ptI_img[1],globales.cuad_grid_obs)
								if not (aux_selec[2] in globales.cuad_obs):
									globales.cuad_obs.append(aux_selec[2])
									globales.pts_aux_obs.append([aux_selec[0],aux_selec[1]])				
								else:
									globales.cuad_obs.remove(aux_selec[2])
									globales.pts_aux_obs.remove([aux_selec[0],aux_selec[1]])
							elif globales.grid_objetos:
								aux_selec=Buscar_pt_cuadricula(event.x()-self.ptI_img[0],event.y()-self.ptI_img[1],globales.cuad_grid_obs)
								if not (aux_selec[2] in globales.cuad_obs):
									if self.radioButton_12.isChecked():
										if not aux_selec[2] in globales.cuad_obj_azul:
											if not aux_selec[2] in globales.cuad_obj_celeste:
												if not aux_selec[2] in globales.cuad_obj_rojos:
													globales.cuad_obj_rojos.append(aux_selec[2])
													globales.obj_rojos.append([aux_selec[0],aux_selec[1]])
												else:
													globales.cuad_obj_rojos.remove(aux_selec[2])
													globales.obj_rojos.remove([aux_selec[0],aux_selec[1]])

									elif self.radioButton_10.isChecked():
										if not aux_selec[2] in globales.cuad_obj_rojos:
											if not aux_selec[2] in globales.cuad_obj_celeste:
												if not aux_selec[2] in globales.cuad_obj_azul:
													globales.cuad_obj_azul.append(aux_selec[2])
													globales.obj_azul.append([aux_selec[0],aux_selec[1]])
												else:
													globales.cuad_obj_azul.remove(aux_selec[2])
													globales.obj_azul.remove([aux_selec[0],aux_selec[1]])

									elif self.radioButton_11.isChecked():
										if not aux_selec[2] in globales.cuad_obj_rojos:
											if not aux_selec[2] in globales.cuad_obj_azul:
												if not aux_selec[2] in globales.cuad_obj_celeste:
													globales.cuad_obj_celeste.append(aux_selec[2])
													globales.obj_celeste.append([aux_selec[0],aux_selec[1]])
												else:
													globales.cuad_obj_celeste.remove(aux_selec[2])
													globales.obj_celeste.remove([aux_selec[0],aux_selec[1]])
									



###################################################################################
##########################Inicializar sim clasificador#############################
	def init_cla(self):
		#SELECCION DE OMNI
		self.comboBox_2.setEnabled(False)
		#Grupo para ingresar punto
		self.groupBox_2.setEnabled(False)
		#Guardar datos
		self.pushButton_29.setEnabled(False)
		#Iniciar proceso
		self.pushButton_14.setEnabled(False)
		#Parar proceso
		self.pushButton_28.setEnabled(False)
		#Grupo para ingresar obstaculos
		self.groupBox_4.setEnabled(True)
		#Grupo para ingresar puntos de obstaculo
		self.pushButton_19.setEnabled(False)
		#Grupo para detectar obstaculos
		self.pushButton_21.setEnabled(True)
		#Grupo para ingresar objetos
		self.groupBox_3.setEnabled(False)
		self.groupBox_5.setEnabled(False)
		self.pushButton_21.setEnabled(True)
		globales.obst_pant=False
		globales.grid_obs=True
		globales.point_obj_rojo=[]
		globales.point_obj_azul=[]
		globales.point_obj_celeste=[]
		globales.obj_cla_dib=False
		globales.aux_dir_omni=[]


###################################################################################
##########################Inicializar sim clasificador#############################
	def init_csi(self):
		#SELECCION DE OMNI
		self.comboBox_2.setEnabled(False)
		#Grupo para ingresar punto
		self.groupBox_2.setEnabled(False)
		#Guardar datos
		self.pushButton_29.setEnabled(False)
		#Iniciar proceso
		self.pushButton_14.setEnabled(False)
		#Parar proceso
		self.pushButton_28.setEnabled(False)
		#Grupo para ingresar obstaculos
		self.groupBox_4.setEnabled(True)
		#Grupo para ingresar puntos de obstaculo
		self.pushButton_19.setEnabled(True)
		#Grupo para detectar obstaculos
		self.pushButton_21.setEnabled(True)
		#Grupo para ingresar objetos
		self.groupBox_3.setEnabled(False)
		self.groupBox_5.setEnabled(False)
		self.pushButton_21.setEnabled(False)
		globales.obst_pant=False
		globales.grid_obs=True
		globales.obj_cla_dib=False
		globales.aux_dir_omni=[]

###################################################################################
##########################Inicializar trayectoria##################################
	def init_tra(self):
		#SELECCION DE OMNI
		self.comboBox_2.setEnabled(True)
		#Grupo para ingresar punto
		self.groupBox_2.setEnabled(True)
		#ingreso manual de punto
		self.spinBox_2.setEnabled(True)
		self.spinBox_3.setEnabled(True)
		#Cargar puntos
		self.pushButton_10.setEnabled(True)
		#Guardar datos
		self.pushButton_29.setEnabled(False)
		#Iniciar proceso
		self.pushButton_14.setEnabled(False)
		#Parar proceso
		self.pushButton_28.setEnabled(False)
		#Borrar puntos
		self.pushButton_18.setEnabled(False)
		#Grupo para ingresar obstaculos
		self.groupBox_4.setEnabled(False)
		#Grupo para ingresar objetos
		self.groupBox_3.setEnabled(False)
		self.groupBox_5.setEnabled(False)
		globales.obst_pant=False
		globales.grid_obs=False
		globales.obj_cla_dib=False
		globales.aux_dir_omni=[]

###################################################################################
##########################Inicializar sim trayectoria##############################
	def init_tos(self):
		#SELECCION DE OMNI
		self.comboBox_2.setEnabled(True)
		#Grupo para ingresar punto
		self.groupBox_2.setEnabled(True)
		#ingreso manual de punto
		self.spinBox_2.setEnabled(True)
		self.spinBox_3.setEnabled(True)
		#Cargar puntos
		self.pushButton_10.setEnabled(True)
		#Guardar datos
		self.pushButton_29.setEnabled(False)
		#Iniciar proceso
		self.pushButton_14.setEnabled(False)
		#Parar proceso
		self.pushButton_28.setEnabled(False)
		#Borrar puntos
		self.pushButton_18.setEnabled(False)
		#Grupo para ingresar obstaculos
		self.groupBox_4.setEnabled(False)
		#Grupo para ingresar puntos de obstaculo
		self.pushButton_19.setEnabled(True)
		#Grupo para detectar obstaculos
		self.pushButton_21.setEnabled(False)
		#Grupo para ingresar objetos
		self.groupBox_3.setEnabled(False)
		self.groupBox_5.setEnabled(False)
		globales.obst_pant=False
		globales.grid_obs=False
		globales.obj_cla_dib=False
		globales.aux_dir_omni=[]

###################################################################################
##########################Inicializar p2p##########################################
	def init_p2p(self):
		#SELECCION DE OMNI
		self.comboBox_2.setEnabled(True)
		#Grupo para ingresar punto
		self.groupBox_2.setEnabled(True)
		#ingreso manual de punto
		self.spinBox_2.setEnabled(True)
		self.spinBox_3.setEnabled(True)
		#Cargar puntos
		self.pushButton_10.setEnabled(True)
		#Guardar datos
		self.pushButton_29.setEnabled(False)
		#Iniciar proceso
		self.pushButton_14.setEnabled(False)
		#Parar proceso
		self.pushButton_28.setEnabled(False)
		#Borrar puntos
		self.pushButton_18.setEnabled(False)
		#Grupo para ingresar obstaculos
		self.groupBox_4.setEnabled(False)
		#Grupo para ingresar objetos
		self.groupBox_3.setEnabled(False)
		self.groupBox_5.setEnabled(False)
		globales.obst_pant=False
		globales.grid_obs=False
		globales.obj_cla_dib=False
		globales.aux_dir_omni=[]

		

###################################################################################
###################################IOT#############################################
###################################################################################

###################################################################################
###################################################################################
	def control_node(self):
		aux_st_node=self.tabWidget.currentIndex()
		if self.boton_node==0 and aux_st_node==2:
			self.pushButton_15.setText('Desactivar')
			globales.node_st=1
			self.boton_node=1
		elif self.boton_node==1 and aux_st_node==2:
			self.pushButton_15.setText('Activar')
			globales.node_st=0
			self.boton_node=0
		else:
			self.pushButton_15.setText('Activar')
			globales.node_st=0
			self.boton_node=0

###################################################################################
###################################################################################
	def pub_gripper(self):
		comb=self.comboBox.currentIndex()
		if self.dato_send==0:
			if comb==0:
				if self.bot_gripper1==0:
					globales.car1_mov='+'
					self.bot_gripper1=1
				else:
					globales.car1_mov='-'
					self.bot_gripper1=0
				#print(globales.car1_mov)
				vros.publicarMovManual()
			elif comb==1:
				if self.bot_gripper2==0:
					globales.car2_mov='+'
					self.bot_gripper2=1
				else:
					globales.car2_mov='-'
					self.bot_gripper2=0
				#print(globales.car2_mov)
				vros.publicarMovManual()
			elif comb==2:
				if self.bot_gripper3==0:
					globales.car3_mov='+'
					self.bot_gripper3=1
				else:
					globales.car3_mov='-'
					self.bot_gripper3=0
				#print(globales.car2_mov)
				vros.publicarMovManual()
			self.dato_send=1
###################################################################################
###################################################################################	
	def pub_dsi(self):
		comb=self.comboBox.currentIndex()
		if self.dato_send==0:
			if comb==0:
				globales.car1_mov='J'
				#print(globales.car1_mov)
				vros.publicarMovManual()
			elif comb==1:
				globales.car2_mov='J'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			elif comb==2:
				globales.car3_mov='J'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			self.dato_send=1
###################################################################################
###################################################################################
	def pub_dii(self):
		comb=self.comboBox.currentIndex()
		if self.dato_send==0:
			if comb==0:
				globales.car1_mov='I'
				#print(globales.car1_mov)
				vros.publicarMovManual()
			elif comb==1:
				globales.car2_mov='I'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			elif comb==2:
				globales.car3_mov='I'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			self.dato_send=1
###################################################################################
###################################################################################
	def pub_did(self):
		comb=self.comboBox.currentIndex()
		if self.dato_send==0:
			if comb==0:
				globales.car1_mov='H'
				#print(globales.car1_mov)
				vros.publicarMovManual()
			elif comb==1:
				globales.car2_mov='H'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			elif comb==2:
				globales.car3_mov='H'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			self.dato_send=1
###################################################################################
###################################################################################
	def pub_dsd(self):
		comb=self.comboBox.currentIndex()
		if self.dato_send==0:
			if comb==0:
				globales.car1_mov='G'
				#print(globales.car1_mov)
				vros.publicarMovManual()
			elif comb==1:
				globales.car2_mov='G'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			elif comb==2:
				globales.car3_mov='G'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			self.dato_send=1
###################################################################################
###################################################################################
	def pub_hor(self):
		comb=self.comboBox.currentIndex()
		if self.dato_send==0:
			if comb==0:
				globales.car1_mov='F'
				#print(globales.car1_mov)
				vros.publicarMovManual()
			elif comb==1:
				globales.car2_mov='F'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			elif comb==2:
				globales.car3_mov='F'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			self.dato_send=1
###################################################################################
###################################################################################
	def pub_anh(self):
		comb=self.comboBox.currentIndex()
		if self.dato_send==0:
			if comb==0:
				globales.car1_mov='E'
				#print(globales.car1_mov)
				vros.publicarMovManual()
			elif comb==1:
				globales.car2_mov='E'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			elif comb==2:
				globales.car3_mov='E'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			self.dato_send=1
###################################################################################
###################################################################################
	def pub_der(self):
		comb=self.comboBox.currentIndex()
		if self.dato_send==0:
			if comb==0:
				globales.car1_mov='D'
				#print(globales.car1_mov)
				vros.publicarMovManual()
			elif comb==1:
				globales.car2_mov='D'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			elif comb==2:
				globales.car3_mov='D'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			self.dato_send=1
###################################################################################
###################################################################################
	def pub_izq(self):
		comb=self.comboBox.currentIndex()
		if self.dato_send==0:
			if comb==0:
				globales.car1_mov='C'
				#print(globales.car1_mov)
				vros.publicarMovManual()
			elif comb==1:
				globales.car2_mov='C'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			elif comb==2:
				globales.car3_mov='C'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			self.dato_send=1
###################################################################################
###################################################################################
	def pub_atras(self):
		comb=self.comboBox.currentIndex()
		if self.dato_send==0:
			if comb==0:
				globales.car1_mov='B'
				#print(globales.car1_mov)
				vros.publicarMovManual()
			elif comb==1:
				globales.car2_mov='B'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			elif comb==2:
				globales.car3_mov='B'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			self.dato_send=1
###################################################################################
###################################################################################
	def pub_init_omni_manual(self):
		globales.n_omni=self.comboBox.currentIndex()+1
		self.pub_set_vel()
###################################################################################
###################################################################################
	def pub_opc_omni(self):
		opc_mod=self.tabWidget.currentIndex()

		if opc_mod==0:
			self.control_node()
			globales.opc_omni_1=0
			globales.opc_omni_2=0
			globales.opc_omni_3=0
			globales.n_omni=1
			vros.publicar_opc()
			#print(globales.n_omni)
			self.pub_parar()
			globales.n_omni=2
			#print(globales.n_omni)
			vros.publicar_opc()
			self.pub_parar()
			globales.n_omni=3
			#print(globales.n_omni)
			vros.publicar_opc()
			self.pub_parar()
			globales.n_omni=self.comboBox.currentIndex()+1
		if opc_mod==2:
			globales.opc_omni_1=0
			globales.opc_omni_2=0
			globales.opc_omni_3=0
			globales.n_omni=1
			#print(globales.n_omni)
			vros.publicar_opc()
			self.pub_parar()
			globales.n_omni=2
			#print(globales.n_omni)
			vros.publicar_opc()
			self.pub_parar()
			globales.n_omni=3
			#print(globales.n_omni)
			vros.publicar_opc()
			self.pub_parar()
			globales.n_omni=globales.node_n_omni
		if opc_mod==1:
			self.control_node()
			#pass
###################################################################################
###################################################################################
	def pub_adelante(self):
		comb=self.comboBox.currentIndex()
		if self.dato_send==0:
			if comb==0:
				globales.car1_mov='A'
				#print(globales.car1_mov)
				vros.publicarMovManual()
			elif comb==1:
				globales.car2_mov='A'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			elif comb==2:
				globales.car3_mov='A'
				#print(globales.car2_mov)
				vros.publicarMovManual()
			self.dato_send=1
###################################################################################
###################################################################################
	def pub_set_vel(self):
		comb=self.comboBox.currentIndex()
		aux_vel=self.spinBox.value()
		if comb==0:
			globales.car1_set=aux_vel
			#print(globales.car1_set)
			vros.publicarVelManual()
		elif comb==1:
			globales.car2_set=aux_vel
			#print(globales.car2_set)
			vros.publicarVelManual()
		elif comb==2:
			globales.car3_set=aux_vel
			#print(globales.car2_set)
			vros.publicarVelManual()
###################################################################################
###################################################################################
	def pub_parar(self):
		comb=self.comboBox.currentIndex()
		if comb==0:
			globales.car1_mov='K'
			#print(globales.car1_mov)
			vros.publicarMovManual()
		elif comb==1:
			globales.car2_mov='K'
			#print(globales.car2_mov)
			vros.publicarMovManual()
		elif comb==2:
			globales.car3_mov='K'
			#print(globales.car2_mov)
			vros.publicarMovManual()
		self.dato_send=0
###################################################################################
###################################################################################
	def Funciones_reloj(self):
		self.mostrar_cam()
		self.mostrar_fh()
		self.mostrar_dat_omni()
		if globales.node_st==1:
			self.control_node_red()
		self.control_automatico()
###################################################################################
###################################################################################
	def control_node_red(self):
		vros.publicar_nodered()
###################################################################################
###################################################################################
	def mostrar_dat_omni(self):
		band=self.tabWidget.currentIndex()
		if band==0:
			aux_omni=self.comboBox.currentIndex()
			if aux_omni==0 and globales.st_omni1==1:
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car1_vel))
				self.tableWidget_3.setItem(0,2,dato_tab)
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car1_ang))
				self.tableWidget_3.setItem(0,3,dato_tab)
			else:
				if aux_omni==0:
					dato_tab=QtWidgets.QTableWidgetItem(str(0))
					self.tableWidget_3.setItem(0,2,dato_tab)
					dato_tab=QtWidgets.QTableWidgetItem(str('-'))
					self.tableWidget_3.setItem(0,3,dato_tab)

			if aux_omni==1 and globales.st_omni2==1:
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car2_vel))
				self.tableWidget_3.setItem(0,2,dato_tab)
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car2_ang))
				self.tableWidget_3.setItem(0,3,dato_tab)
			else:
				if aux_omni==1:
					dato_tab=QtWidgets.QTableWidgetItem(str(0))
					self.tableWidget_2.setItem(0,2,dato_tab)
					dato_tab=QtWidgets.QTableWidgetItem(str('-'))
					self.tableWidget_2.setItem(0,3,dato_tab)
			if aux_omni==2 and globales.st_omni3==1:
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car3_vel))
				self.tableWidget_3.setItem(0,2,dato_tab)
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car3_ang))
				self.tableWidget_3.setItem(0,3,dato_tab)
			else:
				if aux_omni==2:
					dato_tab=QtWidgets.QTableWidgetItem(str(0))
					self.tableWidget_2.setItem(0,2,dato_tab)
					dato_tab=QtWidgets.QTableWidgetItem(str('-'))
					self.tableWidget_2.setItem(0,3,dato_tab)
		elif band==1:
			if globales.st_omni1==1:
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car1_vel))
				self.tableWidget_2.setItem(0,2,dato_tab)
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car1_ang))
				self.tableWidget_2.setItem(0,3,dato_tab)
			else:
				dato_tab=QtWidgets.QTableWidgetItem(str(0))
				self.tableWidget_2.setItem(0,2,dato_tab)
				dato_tab=QtWidgets.QTableWidgetItem(str('-'))
				self.tableWidget_2.setItem(0,3,dato_tab)
			if globales.st_omni2==1:
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car2_vel))
				self.tableWidget_2.setItem(1,2,dato_tab)
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car2_ang))
				self.tableWidget_2.setItem(1,3,dato_tab)
			else:
				dato_tab=QtWidgets.QTableWidgetItem(str(0))
				self.tableWidget_2.setItem(1,2,dato_tab)
				dato_tab=QtWidgets.QTableWidgetItem(str('-'))
				self.tableWidget_2.setItem(1,3,dato_tab)
			if globales.st_omni3==1:
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car3_vel))
				self.tableWidget_2.setItem(2,2,dato_tab)
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car3_ang))
				self.tableWidget_2.setItem(2,3,dato_tab)
			else:
				dato_tab=QtWidgets.QTableWidgetItem(str(0))
				self.tableWidget_2.setItem(2,2,dato_tab)
				dato_tab=QtWidgets.QTableWidgetItem(str('-'))
				self.tableWidget_2.setItem(2,3,dato_tab)
		elif band==2:
			if globales.st_omni1==1:
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car1_vel))
				self.tableWidget.setItem(0,2,dato_tab)
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car1_ang))
				self.tableWidget.setItem(0,3,dato_tab)
			else:
				dato_tab=QtWidgets.QTableWidgetItem(str(0))
				self.tableWidget.setItem(0,2,dato_tab)
				dato_tab=QtWidgets.QTableWidgetItem(str('-'))
				self.tableWidget.setItem(0,3,dato_tab)
			if globales.st_omni2==1:
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car2_vel))
				self.tableWidget.setItem(1,2,dato_tab)
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car2_ang))
				self.tableWidget.setItem(1,3,dato_tab)
			else:
				dato_tab=QtWidgets.QTableWidgetItem(str(0))
				self.tableWidget.setItem(1,2,dato_tab)
				dato_tab=QtWidgets.QTableWidgetItem(str('-'))
				self.tableWidget.setItem(1,3,dato_tab)
			if globales.st_omni3==1:
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car3_vel))
				self.tableWidget.setItem(2,2,dato_tab)
				dato_tab=QtWidgets.QTableWidgetItem(str(globales.car3_ang))
				self.tableWidget.setItem(2,3,dato_tab)
			else:
				dato_tab=QtWidgets.QTableWidgetItem(str(0))
				self.tableWidget.setItem(2,2,dato_tab)
				dato_tab=QtWidgets.QTableWidgetItem(str('-'))
				self.tableWidget.setItem(2,3,dato_tab)
###################################################################################
###################################################################################
	def mostrar_fh(self):
		self.label_hora.setText(QtCore.QDateTime.currentDateTime().toString("ddd hh:mm"))
		self.label_fecha.setText(QtCore.QDateTime.currentDateTime().toString("dd/MMM/yy"))
###################################################################################
###################################################################################
	#Mostrar imagen
	def mostrar_cam(self):

		
		pos1x=0
		pos1y=0
		pos2x=0
		pos2y=0
		pos3x=0
		pos3y=0
		
		# Tomamos una captura desde la webcam.
		ok, img = self.captura.read()

 
		if not ok:
			return
		band=self.tabWidget.currentIndex()
		imag_rect=img.copy()
		imag_rect=cv2.rectangle(imag_rect.copy(), (0,0), (globales.capIz,globales.capInf), (255,255,255),-1)
		imag_rect=cv2.rectangle(imag_rect.copy(), (0,globales.capInf),(720,480), (255,255,255),-1)
		imag_rect=cv2.rectangle(imag_rect.copy(), (0,0), (720,globales.capSu), (255,255,255),-1)
		imag_rect=cv2.rectangle(imag_rect.copy(), (globales.capDe,globales.capSu), (720,480), (255,255,255),-1)

		if band==0:
			imag_rect,pos1x,pos1y=detec_pos_omni_one(self.comboBox.currentIndex(),imag_rect.copy())
			if pos1x==-10000 and pos1y==-10000:
				self.datos_tab=QtWidgets.QTableWidgetItem('No Encontrado')
				self.tableWidget_3.setItem(0,0,self.datos_tab)
				self.datos_tab=QtWidgets.QTableWidgetItem('No Encontrado')
				self.tableWidget_3.setItem(0,1,self.datos_tab)
			elif pos1x==-20000 and pos1y==-20000:
				self.datos_tab=QtWidgets.QTableWidgetItem('Varios Encotrados')
				self.tableWidget_3.setItem(0,0,self.datos_tab)
				self.datos_tab=QtWidgets.QTableWidgetItem('Varios Encotrados')
				self.tableWidget_3.setItem(0,1,self.datos_tab)
			elif pos1x==-30000 and pos1y==-30000:
				self.datos_tab=QtWidgets.QTableWidgetItem('Fuera de rango')
				self.tableWidget_3.setItem(0,0,self.datos_tab)
				self.datos_tab=QtWidgets.QTableWidgetItem('Fuera de rango')
				self.tableWidget_3.setItem(0,1,self.datos_tab)
			elif pos1x==-40000 and pos1y==-40000:
				self.datos_tab=QtWidgets.QTableWidgetItem('Desactivado')
				self.tableWidget_3.setItem(0,0,self.datos_tab)
				self.datos_tab=QtWidgets.QTableWidgetItem('Desactivado')
				self.tableWidget_3.setItem(0,1,self.datos_tab)
			else:
				self.datos_tab=QtWidgets.QTableWidgetItem(str(pos1x))
				self.tableWidget_3.setItem(0,0,self.datos_tab)
				self.datos_tab=QtWidgets.QTableWidgetItem(str(pos1y))
				self.tableWidget_3.setItem(0,1,self.datos_tab)
		elif band==2:
			imag_rect,pos1x,pos1y,pos2x,pos2y,pos3x,pos3y=detec_pos_omni_iot(imag_rect.copy())
			if pos1x==0 and pos1y==0:
				self.datos_tab=QtWidgets.QTableWidgetItem('No Encontrado')
				self.tableWidget.setItem(0,0,self.datos_tab)
				self.datos_tab=QtWidgets.QTableWidgetItem('No Encontrado')
				self.tableWidget.setItem(0,1,self.datos_tab)
				if globales.node_st==1:
					vros.pos_net.data[1]=0
					vros.pos_net.data[2]=0
			else:
				self.datos_tab=QtWidgets.QTableWidgetItem(str(pos1x))
				self.tableWidget.setItem(0,0,self.datos_tab)
				self.datos_tab=QtWidgets.QTableWidgetItem(str(pos1y))
				self.tableWidget.setItem(0,1,self.datos_tab)
				if globales.node_st==1:
					vros.pos_net.data[1]=pos1x
					vros.pos_net.data[2]=pos1y

			if pos2x==0 and pos2y==0:
				self.datos_tab=QtWidgets.QTableWidgetItem('No Encontrado')
				self.tableWidget.setItem(1,0,self.datos_tab)
				self.datos_tab=QtWidgets.QTableWidgetItem('No Encontrado')
				self.tableWidget.setItem(1,1,self.datos_tab)
				if globales.node_st==1:
					vros.pos_net.data[2]=0
					vros.pos_net.data[3]=0
			else:
				self.datos_tab=QtWidgets.QTableWidgetItem(str(pos2x))
				self.tableWidget.setItem(1,0,self.datos_tab)
				self.datos_tab=QtWidgets.QTableWidgetItem(str(pos2y))
				self.tableWidget.setItem(1,1,self.datos_tab)
				if globales.node_st==1:
					vros.pos_net.data[2]=pos2x
					vros.pos_net.data[3]=pos2y


			if pos3x==0 and pos3y==0:
				self.datos_tab=QtWidgets.QTableWidgetItem('No Encontrado')
				self.tableWidget.setItem(2,0,self.datos_tab)
				self.datos_tab=QtWidgets.QTableWidgetItem('No Encontrado')
				self.tableWidget.setItem(2,1,self.datos_tab)
				if globales.node_st==1:
					vros.pos_net.data[4]=0
					vros.pos_net.data[5]=0
			else:
				self.datos_tab=QtWidgets.QTableWidgetItem(str(pos3x))
				self.tableWidget.setItem(2,0,self.datos_tab)
				self.datos_tab=QtWidgets.QTableWidgetItem(str(pos3y))
				self.tableWidget.setItem(2,1,self.datos_tab)
				if globales.node_st==1:
					vros.pos_net.data[4]=pos3x
					vros.pos_net.data[5]=pos3y
			if globales.node_st==1:
				ret, jpeg = cv2.imencode('.jpg', imag_rect.copy())
				jpg_as_text = base64.b64encode(jpeg)
				aux_cam=str(jpg_as_text)
				aux_cam="data:image/jpeg;base64,"+aux_cam[2:len(aux_cam)-1]
				globales.node_cam=aux_cam

		elif band==1:
			imag_rect,pos1x,pos1y,pos2x,pos2y,pos3x,pos3y=detec_pos_omni_auto(imag_rect.copy())
			if pos1x==0 and pos1y==0:
				if globales.st_omni1==1:
					self.datos_tab=QtWidgets.QTableWidgetItem('No Encontrado')
					self.tableWidget_2.setItem(0,0,self.datos_tab)
					self.datos_tab=QtWidgets.QTableWidgetItem('No Encontrado')
					self.tableWidget_2.setItem(0,1,self.datos_tab)
				else:
					self.datos_tab=QtWidgets.QTableWidgetItem(str('INACTIVO'))
					self.tableWidget_2.setItem(0,0,self.datos_tab)
					self.datos_tab=QtWidgets.QTableWidgetItem(str('INACTIVO'))
					self.tableWidget_2.setItem(0,1,self.datos_tab)
					globales.aut_omni1_x=-10000
					globales.aut_omni1_y=-10000

			else:
				if globales.st_omni1==1:
					self.datos_tab=QtWidgets.QTableWidgetItem(str(pos1x))
					self.tableWidget_2.setItem(0,0,self.datos_tab)
					self.datos_tab=QtWidgets.QTableWidgetItem(str(pos1y))
					self.tableWidget_2.setItem(0,1,self.datos_tab)
				
					globales.aut_omni1_x=int(pos1x)
					globales.aut_omni1_y=int(pos1y)
				else:
					self.datos_tab=QtWidgets.QTableWidgetItem(str('INACTIVO'))
					self.tableWidget_2.setItem(0,0,self.datos_tab)
					self.datos_tab=QtWidgets.QTableWidgetItem(str('INACTIVO'))
					self.tableWidget_2.setItem(0,1,self.datos_tab)
				
					globales.aut_omni1_x=-10000
					globales.aut_omni1_y=-10000
					


			if pos2x==0 and pos2y==0:
				if globales.st_omni2==1:
					self.datos_tab=QtWidgets.QTableWidgetItem('No Encontrado')
					self.tableWidget_2.setItem(1,0,self.datos_tab)
					self.datos_tab=QtWidgets.QTableWidgetItem('No Encontrado')
					self.tableWidget_2.setItem(1,1,self.datos_tab)
				else:
					self.datos_tab=QtWidgets.QTableWidgetItem('NINACTIVO')
					self.tableWidget_2.setItem(1,0,self.datos_tab)
					self.datos_tab=QtWidgets.QTableWidgetItem('NINACTIVO')
					self.tableWidget_2.setItem(1,1,self.datos_tab)
					globales.aut_omni2_x=-10000
					globales.aut_omni2_y=-10000

			else:
				if globales.st_omni2==1:
					self.datos_tab=QtWidgets.QTableWidgetItem(str(pos2x))
					self.tableWidget_2.setItem(1,0,self.datos_tab)
					self.datos_tab=QtWidgets.QTableWidgetItem(str(pos2y))
					self.tableWidget_2.setItem(1,1,self.datos_tab)

					globales.aut_omni2_x=int(pos2x)
					globales.aut_omni2_y=int(pos2y)
				else:
					self.datos_tab=QtWidgets.QTableWidgetItem('INACTIVO')
					self.tableWidget_2.setItem(1,0,self.datos_tab)
					self.datos_tab=QtWidgets.QTableWidgetItem('INACTIVO')
					self.tableWidget_2.setItem(1,1,self.datos_tab)

					globales.aut_omni2_x=-10000
					globales.aut_omni2_y=-10000



			if pos3x==0 and pos3y==0:
				if globales.st_omni3==1:
					self.datos_tab=QtWidgets.QTableWidgetItem('No Encontrado')
					self.tableWidget_2.setItem(2,0,self.datos_tab)
					self.datos_tab=QtWidgets.QTableWidgetItem('No Encontrado')
					self.tableWidget_2.setItem(2,1,self.datos_tab)
				else:
					self.datos_tab=QtWidgets.QTableWidgetItem('INACTIVO')
					self.tableWidget_2.setItem(2,0,self.datos_tab)
					self.datos_tab=QtWidgets.QTableWidgetItem('INACTIVO')
					self.tableWidget_2.setItem(2,1,self.datos_tab)
					globales.aut_omni3_x=-10000
					globales.aut_omni3_y=-10000

			else:
				if globales.st_omni3==1:
					self.datos_tab=QtWidgets.QTableWidgetItem(str(pos3x))
					self.tableWidget_2.setItem(2,0,self.datos_tab)
					self.datos_tab=QtWidgets.QTableWidgetItem(str(pos3y))
					self.tableWidget_2.setItem(2,1,self.datos_tab)
					globales.aut_omni3_x=int(pos3x)
					globales.aut_omni3_y=int(pos3y)
				else:
					self.datos_tab=QtWidgets.QTableWidgetItem('INACTIVO')
					self.tableWidget_2.setItem(2,0,self.datos_tab)
					self.datos_tab=QtWidgets.QTableWidgetItem('INACTIVO')
					self.tableWidget_2.setItem(2,1,self.datos_tab)

					globales.aut_omni3_x=-10000
					globales.aut_omni3_y=-10000

			if globales.mov_enc==0:
				if self.radioButton.isChecked() or self.radioButton_2.isChecked() or  self.radioButton_3.isChecked() or self.radioButton_4.isChecked():
					if self.groupBox_2.isEnabled() or self.groupBox_3.isEnabled() or self.groupBox_4.isEnabled():
						if self.groupBox_2.isEnabled() and self.pushButton_10.isEnabled():
							imag_rect=cv2.circle(imag_rect.copy(), (globales.aux_ppx_pt_destx,globales.aux_ppx_pt_desty), 8, (0,0,0), -1)
							font = cv2.FONT_HERSHEY_SIMPLEX
							imag_rect=cv2.putText(imag_rect.copy(), '{},{}'.format(globales.aux_pt_destx,globales.aux_pt_desty),(int(globales.aux_ppx_pt_destx-100),int(globales.aux_ppx_pt_desty-10)), font, 0.55,(0,0,0),1,cv2.LINE_AA)

							if len(globales.punto_mouse)==2:
								mag_rect=cv2.circle(imag_rect.copy(), (int(globales.punto_mouse[0]),int(globales.punto_mouse[1])), 2, (0,0,255), -1)
								font = cv2.FONT_HERSHEY_SIMPLEX
								imag_rect=cv2.putText(imag_rect.copy(), '{},{}'.format(globales.punto_mouse_real[0],globales.punto_mouse_real[1]),(int(globales.punto_mouse[0]-100),int(globales.punto_mouse[1]-10)), font, 0.55,(0,0,255),1,cv2.LINE_AA)
						elif globales.grid_obs:
							imag_rect=grid_obstaculos(imag_rect.copy())
						elif globales.grid_objetos:
							imag_rect=grid_obstaculos(imag_rect.copy())
							imag_rect=grid_objetos(imag_rect.copy())
			if globales.opc_auto==2:
				imag_rect=grid_obstaculos(imag_rect.copy())
			if globales.opc_auto==4:
				imag_rect=grid_obstaculos(imag_rect.copy())
				imag_rect=grid_objetos(imag_rect.copy())

			if globales.obst_pant:
				imag_rect=pant_obstaculos(imag_rect.copy())
			if globales.obj_cla_dib:
				imag_rect=dibjar_objetos_detectados(imag_rect.copy())


	################################################################################################################	


		image = QtGui.QImage(imag_rect, imag_rect.shape[1], imag_rect.shape[0], imag_rect.shape[1] * imag_rect.shape[2], QtGui.QImage.Format_RGB888)
 
        # Creamos un pixmap a partir de la imagen.
        # OpenCV entraga los pixeles de la imagen en formato BGR en lugar del tradicional RGB,
        # por lo tanto tenemos que usar el metodo rgbSwapped() para que nos entregue una imagen con
        # los bytes Rojo y Azul intercambiados, y asi poder mostrar la imagen de forma correcta.
		pixmap = QtGui.QPixmap()
		pixmap.convertFromImage(image.rgbSwapped())
 
        # Mostramos el QPixmap en la QLabel.
		self.label_2.setPixmap(pixmap)
###################################################################################
###################################################################################
	#Deteccion boton cerrar
	def closeEvent(self, evnt):
		globales.aux_vent_config=0
		self.captura.release()
		self.Ventana_Inicio=Ui_Inicio()
		self.Ventana_Inicio.show()
		self.close()

###################################################################################
###################################################################################
###################################################################################

		