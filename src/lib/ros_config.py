#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import Int16
from std_msgs.msg import Float32
from std_msgs.msg import Char
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int8
from std_msgs.msg import String
from config import globales

#Librery numpy
import numpy as np
import cv2
#from cv_bridge import CvBridge, CvBridgeError

import sys
#global num_omni.data
num_omni=Int8()
num_omni.data=0


_opc_omni=Int8()
_opc_omni.data=0


_mov_omni=Char()
_mov_omni.data=ord('K')

_setpoint_omni=Float32MultiArray()
_setpoint_omni.data=[0,0,0,0]


###PUBLISH FUNCTIONS
##ENVIROMENT CAMERA BROKER-NODERED
cam1=String()
cam1.data=" "

#OMNI POSITION - BROKER-NODERED 
pos_net=Float32MultiArray()
pos_net.data=[0,0,0,0,0,0]

#VELOCITY OF OMNIS LECTOR-NODERED
rpm_net=Float32MultiArray()
rpm_net.data=[0,0,0]

#PUNTOS DE MOVILIZACION
#Puntos para direccionar
pts1=Float32MultiArray()
pts1.data=[0,0,0,0,0,0]
pts2=Float32MultiArray()
pts2.data=[0,0,0,0,0,0]
pts3=Float32MultiArray()
pts3.data=[0,0,0,0,0,0]
pts4=Float32MultiArray()
pts4.data=[0,0,0,0,0,0]
pts5=Float32MultiArray()
pts5.data=[0,0,0,0,0,0]




###################################################################################
###################################################################################
##########################FUNCINES DE SUSCRIPCION##################################
###################################################################################
##########################DE NODERED###############################################
###################################################################################
def Omni_opc(data):
	if globales.node_st==1:
		if globales.node_n_omni!=data.data:
			_mov_omni.data=ord('K')
			pubM1.publish(_mov_omni)
			pubM2.publish(_mov_omni)
			pubM3.publish(_mov_omni)
			globales.node_n_omni=data.data
###################################################################################
def Movimiento_omni(data):
	#globales.node_mov=data.datade_mov=data.data
	if globales.node_st==1:
		if globales.node_n_omni==1:
			pubM1.publish(data)
		elif globales.node_n_omni==2:
			pubM2.publish(data)
		elif globales.node_n_omni==3:
			pubM3.publish(data)
###################################################################################
def Omni_rpm(data):
	#globales.node_set=data.data
	
		
	if globales.node_st==1:
		_setpoint_omni.data=[data.data,data.data,data.data,data.data]
		if globales.node_n_omni==1:
			pubS1.publish(_setpoint_omni)
		elif globales.node_n_omni==2:
			pubS2.publish(_setpoint_omni)
		elif globales.node_n_omni==3:
			pubS3.publish(_setpoint_omni)
###################################################################################
def Gripper_net(data):
	#globales.node_mov=data.data
	if globales.node_st==1:
		if globales.node_n_omni==1:
			pubM1.publish(data)
		elif globales.node_n_omni==2:
			pubM2.publish(data)
		elif globales.node_n_omni==3:
			pubM3.publish(data)
###################################################################################
###################################################################################

###################################################################################
###################################################################################
#######################DE 0MNI#####################################################
###################################################################################
def VelOmni1(data):
	globales.car1_vel=int(sum(data.data)/len(data.data))
	if globales.node_st==1:
		rpm_net.data[0]=globales.car1_vel
###################################################################################
def VelOmni2(data):
	globales.car2_vel=int(sum(data.data)/len(data.data))
	if globales.node_st==1:
		rpm_net.data[1]=globales.car2_vel
###################################################################################
def VelOmni3(data):
	globales.car3_vel=int(sum(data.data)/len(data.data))
	if globales.node_st==1:
		rpm_net.data[2]=globales.car3_vel
###################################################################################
def AngOmni1(data):
	globales.car1_ang=data.data[3]
###################################################################################
def AngOmni2(data):
	globales.car2_ang=data.data[3]
###################################################################################
def AngOmni3(data):
	globales.car3_ang=int(data.data[3])
###################################################################################
def StateOmni1(data):
	globales.car1_st=data.data
###################################################################################
def StateOmni2(data):
	globales.car2_st=data.data
###################################################################################
def StateOmni3(data):
	globales.car3_st=data.data
###################################################################################
###################################################################################








###################################################################################
###################################################################################
#########################PUBLICADORES##############################################
###################################################################################
#########################PARA OMNI#################################################
###################################################################################
pubS1 = rospy.Publisher('rasp_control/rasp1/setpoint', Float32MultiArray, queue_size=2)
pubM1 = rospy.Publisher('rasp_control/rasp1/movimiento', Char, queue_size=2)
pubOpc1 = rospy.Publisher('rasp_control/rasp1/opc', Int8, queue_size=2)

pubS2 = rospy.Publisher('rasp_control/rasp2/setpoint', Float32MultiArray, queue_size=2)
pubM2 = rospy.Publisher('rasp_control/rasp2/movimiento', Char, queue_size=2)
pubOpc2 = rospy.Publisher('rasp_control/rasp2/opc', Int8, queue_size=2)

pubS3 = rospy.Publisher('rasp_control/rasp3/setpoint', Float32MultiArray, queue_size=2)
pubM3 = rospy.Publisher('rasp_control/rasp3/movimiento', Char, queue_size=2)
pubOpc3 = rospy.Publisher('rasp_control/rasp3/opc', Int8, queue_size=2)

###################################################################################
############################NODERED PUBLISHER######################################
###################################################################################
pub_img = rospy.Publisher('node_red/cam', String, queue_size=1)
pub_rpm = rospy.Publisher('node_red/rpm', Float32MultiArray, queue_size=1)
pub_pos = rospy.Publisher('node_red/pos', Float32MultiArray, queue_size=1)
###################################################################################
###################################################################################
###################################################################################

###################################################################################
######################Puntos para movilizarse######################################
###################################################################################
pub1_pts = rospy.Publisher('/rasp_control/rasp1/puntos', Float32MultiArray, queue_size=2)
pub2_pts = rospy.Publisher('/rasp_control/rasp2/puntos', Float32MultiArray, queue_size=2)
pub3_pts = rospy.Publisher('/rasp_control/rasp3/puntos', Float32MultiArray, queue_size=2)
pub4_pts = rospy.Publisher('/rasp_control/rasp4/puntos', Float32MultiArray, queue_size=2)
pub5_pts = rospy.Publisher('/rasp_control/rasp5/puntos', Float32MultiArray, queue_size=2)
###################################################################################
###################################################################################
###################################################################################


###################################################################################
###################################################################################
#############################SUSCRIPTORES##########################################
###################################################################################
###################################################################################
##########################SUBSCRIPTORES OMNI-ESP32#################################
###################################################################################
###############Direccion#################
rospy.Subscriber('rasp_control/omni1/mpu', Float32MultiArray, AngOmni1)
rospy.Subscriber('rasp_control/omni2/mpu', Float32MultiArray, AngOmni2)
rospy.Subscriber('rasp_control/omni3/mpu', Float32MultiArray, AngOmni3)
###############Velocidad#################
rospy.Subscriber('rasp_control/omni1/rpm', Float32MultiArray, VelOmni1)
rospy.Subscriber('rasp_control/omni2/rpm', Float32MultiArray, VelOmni2)
rospy.Subscriber('rasp_control/omni3/rpm', Float32MultiArray, VelOmni3)
###############Estado automatico#########
rospy.Subscriber('rasp_control/rasp1/estado', Int8, StateOmni1)
rospy.Subscriber('rasp_control/rasp2/estado', Int8, StateOmni2)
rospy.Subscriber('rasp_control/rasp3/estado', Int8, StateOmni3)
###################################################################################
###################################################################################
###########################SUSCRIPTORES NODERED####################################
###################################################################################
rospy.Subscriber('node_red/rasp/omni_opc', Int8, Omni_opc)
rospy.Subscriber('node_red/rasp/movimiento', Char, Movimiento_omni)
rospy.Subscriber('node_red/rasp/rpm', Int8, Omni_rpm)
rospy.Subscriber('node_red/rasp/gripper', Char, Gripper_net)
###################################################################################
###################################################################################



###################################################################################
###########################INICIALIZAR NODO########################################
###################################################################################
rospy.init_node('Broker_control_omni', anonymous=True)
rospy.loginfo('Broker_cntrol')
rate = rospy.Rate(10) # 10hz
###################################################################################

###################################################################################
###################################################################################
##########################FUNCIONES DE PUBLICACION#################################
###################################################################################
###################################################################################
##########################PARA OMNI################################################
###################################################################################
def publicarMovManual():
	global num_omni
	global _setpoint_omni
	global _mov_omni
	if globales.n_omni==1:
		#_setpoint_omni.data=[globales.car1_set,globales.car1_set,globales.car1_set,globales.car1_set]
		_mov_omni.data=ord(globales.car1_mov)
		#pubS1.publish(_setpoint_omni)
		pubM1.publish(_mov_omni)
	elif globales.n_omni==2:
		#_setpoint_omni.data=[globales.car2_set,globales.car2_set,globales.car2_set,globales.car2_set]
		_mov_omni.data=ord(globales.car2_mov)
		#pubS2.publish(_setpoint_omni)
		pubM2.publish(_mov_omni)
	elif globales.n_omni==3:
		#_setpoint_omni.data=[globales.car3_set,globales.car3_set,globales.car3_set,globales.car3_set]
		_mov_omni.data=ord(globales.car3_mov)
		#pubS3.publish(_setpoint_omni)
		pubM3.publish(_mov_omni)

	rate.sleep()
###################################################################################
###################################################################################
def publicarVelManual():
	global num_omni
	global _setpoint_omni
	global _mov_omni
	if globales.n_omni==1:
		_setpoint_omni.data=[globales.car1_set,globales.car1_set,globales.car1_set,globales.car1_set]
		pubS1.publish(_setpoint_omni)
	elif globales.n_omni==2:
		_setpoint_omni.data=[globales.car2_set,globales.car2_set,globales.car2_set,globales.car2_set]
		pubS2.publish(_setpoint_omni)
	elif globales.n_omni==3:
		_setpoint_omni.data=[globales.car3_set,globales.car3_set,globales.car3_set,globales.car3_set]
		pubS3.publish(_setpoint_omni)

	rate.sleep()
###################################################################################
###################################################################################
def publicar_opc():
	global num_omni
	global _opc_omni

	if globales.n_omni==1:
		_opc_omni.data=globales.opc_omni_1
		pubOpc1.publish(_opc_omni)

	elif globales.n_omni==2:
		_opc_omni.data=globales.opc_omni_2
		pubOpc2.publish(_opc_omni)

	elif globales.n_omni==3:
		_opc_omni.data=globales.opc_omni_3
		pubOpc3.publish(_opc_omni)

	rate.sleep()
###################################################################################
###################################################################################
######################PARA NODERED#################################################
###################################################################################

def publicar_nodered():
	global rpm_net
	global pos_net
	global cam1
	pos_net.data=globales.node_pos
	rpm_net.data=globales.node_rpms
	cam1.data=globales.node_cam
	pub_pos.publish(pos_net)
	pub_rpm.publish(rpm_net)
	pub_img.publish(cam1)
	rate.sleep()
###################################################################################
###################################################################################
###################################################################################
######################PARA AUTOMATICO##############################################
###################################################################################

def publicar_pts():
	global pts1
	if globales.n_omni==1:
		pts1.data=[globales.aut_omni1_x,globales.aut_omni1_y,globales.dir_omni_x,globales.dir_omni_y,globales.pt_destx,globales.pt_desty]
		pub1_pts.publish(pts1)
		print(pts1.data)

	elif globales.n_omni==2:
		pts2.data=[globales.aut_omni2_x,globales.aut_omni2_y,globales.dir_omni_x,globales.dir_omni_y,globales.pt_destx,globales.pt_desty]
		pub2_pts.publish(pts2)
		print(pts2.data)

	elif globales.n_omni==3:
		pts3.data=[globales.aut_omni3_x,globales.aut_omni3_y,globales.dir_omni_x,globales.dir_omni_y,globales.pt_destx,globales.pt_desty]
		pub3_pts.publish(pts3)
		print(pts3.data)
		#print(pts3)

	rate.sleep()
###################################################################################
###################################################################################