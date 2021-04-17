#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import cv2
import numpy as np

#DIRECCION DE SCRIP
dir_work=''
dir_work_aux=''

###Globales para control
##eleccion de camara
tarjeta_camara=0
##estado de omnidireccionales
st_omni1=0
st_omni2=0
st_omni3=0

##Recorte de video
#limite izquierda video
capIz=0
#limite derecha video
capDe=720
#limite superior video
capSu=0
#limite inferior video
capInf=480

#Numero de divisiones horizontal
divH=1

#Numero de divisiones vertical
divV=1


##Puntos de depositos
#Rojo
DepoRojoX=[]
DepoRojoY=[]
#Azul
DepoAzulX=[]
DepoAzulY=[]
#Celeste
DepoCelX=[]
DepoCelY=[]

##Equivalencia de pixeles y mm
#Pixeles
EscPix=0
#mm
EscMM=0

##Dimensiones de deteccion OMNIS
#Omni1
omni1_Area_Cent=0
omni1_Area_Sec=0
omni1_Sep_Area=0
omni1_Dist_Act=0
#Omni2
omni2_Area_Cent=0
omni2_Area_Sec=0
omni2_Sep_Area=0
omni2_Dist_Act=0
#Omni3
omni3_Area_Cent=0
omni3_Area_Sec=0
omni3_Sep_Area=0
omni3_Dist_Act=0





###globales auxiliares para funcionamiento

##Interaccion entre ventanas
#Seleccion de video
aux_tarjeta=0
#Abrir ventanas auxiliares sin regresar
aux_vent_config=0



##Cuadricula de puntos
cuadricula=[]
cuadricula_rojo=[]
cuadricula_azul=[]
cuadricula_celeste=[]

###Globales restaurar configAvanzado
#Dimenisones de entorno y grid
limIz=0
limDe=0
limSup=0
limInf=0
Grid_mm=0
Grid_px=0

#Escala restaurar
rest_px=0
rest_mm=0

##Puntos en imagen configuraciones avanzadas
Esc_p1=[]
Esc_p2=[]



##Globales auxiliares depositos
Drojo=[]
Dazul=[]
Dceleste=[]


#inicio de gafico de linea
glineI=False
glineT=False
glineTT=False

#areas y sepracion omnis
aG=[0,0,0]
aS=[0,0,0]
dA=[0,0,0]
dAc=[0,0,0]

#variables de camara
verdeBajo = np.array([40, 70, 15], np.uint8)
verdeAlto = np.array([70, 255, 255], np.uint8)
rojoBajo1 = np.array([0, 40, 0], np.uint8)
rojoAlto1 = np.array([9, 255, 150], np.uint8)
rojoBajo2 = np.array([175, 40, 0], np.uint8)
rojoAlto2 = np.array([179, 255, 150], np.uint8)
#rojoBajo1 = np.array([0, 70, 30], np.uint8)
#rojoAlto1 = np.array([9, 255, 255], np.uint8)
#rojoBajo2 = np.array([175, 90, 10], np.uint8)
#rojoAlto2 = np.array([179, 255, 255], np.uint8)
azulBajo = np.array([100, 80, 0], np.uint8)
azulAlto = np.array([125, 255, 255], np.uint8)
azulBajo1 = np.array([105, 100, 0], np.uint8)
azulAlto1 = np.array([125, 255, 255], np.uint8)
#azulBajo = np.array([100, 110, 0], np.uint8)
#azulAlto = np.array([125, 255, 255], np.uint8)
celesteBajo = np.array([75, 50, 0], np.uint8)
celesteAlto = np.array([100, 200, 255], np.uint8)

#Obstaculos
obstaculoBajo = np.array([15, 70, 0], np.uint8)
obstaculoAlto = np.array([25, 255, 255], np.uint8)
area_objeto=[300,1000]

#OBJETOS clasificar
area_obj_cla=[50,150]

#Variables de camara
pt_max_x=2920
pt_max_y=1867
mtx=np.float64([[490.20949553,0,306.49475765],[0,579.08833664,285.74153175],[0,0,1]])
dist=np.array([[-0.3358916, 0.2173247, -0.00666694, 0.00756815, -0.12965549]])
patron = np.float32([[27, 1790,0], [2835,1867,0], [0,0,0], [2920,99,0]])
centros_ordenados = np.float32([[105,65] , [640,65], [105,455], [640,455]])
retval, rvec, tvec = cv2.solvePnP(objectPoints = patron, imagePoints = centros_ordenados, cameraMatrix = mtx, distCoeffs = dist)


###POSICIONES OMNI
##OMNI1
#POSICION
omni1_xy=[0,0]
omni2_xy=[0,0]
omni3_xy=[0,0]

###VARIABLES DE ROS
#Seleccion de omni manual
n_omni=1
#En funcion nodered
node_st=0
##PUBLICADORES A OMNI
car1_mov='K'
car2_mov='K'
car3_mov='K'

car1_set=0
car2_set=0
car3_set=0

opc_omni_1=0
opc_omni_2=0
opc_omni_3=0

car1_pts=[0,0,0,0,0,0]
car2_pts=[0,0,0,0,0,0]
car3_pts=[0,0,0,0,0,0]

##SUSCRIPTORES DE OMNI
car1_ang=0
car2_ang=0
car3_ang=0
car1_vel=0
car2_vel=0
car3_vel=0
car1_st=0
car2_st=0
car3_st=0

##PUBLICADORES A NODERED
node_rpms=[0,0,0]
node_pos=[0,0,0,0,0,0]
node_cam=''

##Suscriptores DE NODERED
node_mov='K'
node_set=0
node_n_omni=1

##VARIABLES ENTORNO AUTOMATICO
#POSICION DE OMNI
aut_omni1_x=-10000
aut_omni1_y=-10000
aut_omni2_x=-10000
aut_omni2_y=-10000
aut_omni3_x=-10000
aut_omni3_y=-10000
#GRID DE DIVISION
grid_tray=150
ratio_robot=300
cuad_grid_obs=[]
cuad_obs=[]
#Punto de destino
pt_destx=-10000
pt_desty=-10000
aux_pt_destx=-10000
aux_pt_desty=-10000
aux_ppx_pt_destx=-10000
aux_ppx_pt_desty=-10000

#BANDERA PTS
pts_act=0
#seguimiento de punto
punto_mouse_act=0
punto_mouse=[]
punto_mouse_real=[]

#ACTIVACION DE MOVIMIENTO
mov_enc=0


#PUNTOS DE DIRECCION
dir_omni_x=0
dir_omni_y=0


#INICIIO DE PROCESO OPCION 
#1-->P2P
#2-->TSIM
#3-->TOBJ
#4-->CSIM
#5-->CLASI
#0-->INACTIVO
opc_auto=0

#DATOS PARA GUARDAR
opc1_pto=[]
opc1_ptf=[]
opc1_dest=[]

#VER GRID DE OBSTACULOS
grid_obs=False
#PuntosoBSTACULOS
pts_aux_obs=[]
pt_obs_x=[]
pt_obs_y=[]

#Puntos Trayectoria
tray_omni_x=[]
tray_omni_y=[]

#Contador_tray
cont_tray=0

#Auxiliar_Datos tray
pts_tray_aux_omni=[]
pts_tray_aux=[]
pts_tray_obs=[]

#Guardar datos dep de algoritmo tray
tray_alg=0
#Puntos de obstaculos auxiliares detectados
pts_aux_obs_det=[]
#Mostrar obstaculos en pantalla
obst_pant=False

#OBJETOS GRID
grid_objetos=False
#OBJETOS A CLASIFICAR
#ROJOS
cuad_obj_rojos=[]
obj_rojos=[]
#obj_rojos_aux=[]
#AZUL
cuad_obj_azul=[]
obj_azul=[]
#obj_azul_aux=[]
#CELESTE
cuad_obj_celeste=[]
obj_celeste=[]
#obj_celeste_aux=[]

#OMNI EN CLASIFICACION
n_omni_cla=0
pts_origin=[]
pts_objetos=[]

#ESTADO DE CLASIFICACION
clasificando_obj=False
#Estado de ruta 1 coger 2 llevar 3 regresar
st_clasificador=0
#Color de objeto
color_obj=0
#Objetos de clasificador
pt_obs_cla_x=[]
pt_obs_cla_y=[]
#Puntos de grid de auto
pts_px_omni_1=[-10000,-10000]
pts_px_omni_2=[-10000,-10000]
pts_px_omni_3=[-10000,-10000]
cuad_clasificador_obj=[]
datos_clasificador_coger=[]
datos_clasificador_colocar=[]
datos_clasificador_obstaculos=[]
#objetos con coordenada real
obj_rojo_real=[]
obj_azul_real=[]
obj_celeste_real=[]
#INDICE DE OBJETO SIMULACION
cont_obj_sim=100
#PUNTOS DE CLASIFICACION
point_obj_rojo=[]
point_obj_azul=[]
point_obj_celeste=[]
obj_cla_dib=False
#Detectar objectos desactivado
desact_dect_obj=True

