#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
from config import globales
import shlex, subprocess
import re
import csv
import os
import cv2
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


#dir_work="/home/lja/catkin_ws/src/broker_control/src/vars/config_var.csv"

def recuperar_variable_total():
	globales.dir_work=globales.dir_work+"/vars/config_var.csv"
	f = open(globales.dir_work, 'r')

	with f:

		reader = csv.DictReader(f)
    
		for row in reader:
			globales.tarjeta_camara=int(row['camara'])
			
			globales.st_omni1=int(row['st_omni1'])
			globales.st_omni2=int(row['st_omni2'])
			globales.st_omni3=int(row['st_omni3'])
			
			globales.capIz=int(row['limIzq'])
			globales.capDe=int(row['limDer'])
			globales.capSu=int(row['limSup'])
			globales.capInf=int(row['limInf'])
			globales.divH=int(row['DivH'])
			globales.divV=int(row['DivV'])

			
			globales.DepoRojoX=trans_load_vec(row['DepoRojox'])
			globales.DepoRojoY=trans_load_vec(row['DepoRojoy'])
			globales.DepoAzulX=trans_load_vec(row['DepoAzulx'])
			globales.DepoAzulY=trans_load_vec(row['DepoAzuly'])
			globales.DepoCelX=trans_load_vec(row['DepoCelx'])
			globales.DepoCelY=trans_load_vec(row['DepoCely'])

			globales.EscPix=float(row['EPix'])
			globales.EscMM=float(row['Emm'])

			globales.omni1_Area_Cent=float(row['o1_AC'])
			globales.omni1_Area_Sec=float(row['o1_AS'])
			globales.omni1_Sep_Area=float(row['o1_SA'])
			globales.omni1_Dist_Act=float(row['o1_DA'])

			globales.omni2_Area_Cent=float(row['o2_AC'])
			globales.omni2_Area_Sec=float(row['o2_AS'])
			globales.omni2_Sep_Area=float(row['o2_SA'])
			globales.omni2_Dist_Act=float(row['o2_DA'])

			globales.omni3_Area_Cent=float(row['o3_AC'])
			globales.omni3_Area_Sec=float(row['o3_AS'])
			globales.omni3_Sep_Area=float(row['o3_SA'])
			globales.omni3_Dist_Act=float(row['o3_DA'])



def guardar_variable_total():

	aux_pRx=trans_save_vec(globales.DepoRojoX)
	aux_pRy=trans_save_vec(globales.DepoRojoY)
	aux_pAx=trans_save_vec(globales.DepoAzulX)
	aux_pAy=trans_save_vec(globales.DepoAzulY)
	aux_pCx=trans_save_vec(globales.DepoCelX)
	aux_pCy=trans_save_vec(globales.DepoCelY)

	f = open(globales.dir_work, 'w')

	with f:

		fnames = ['camara', 'st_omni1','st_omni2','st_omni3','limIzq','limDer','limSup','limInf','DivH','DivV','DepoRojox','DepoRojoy','DepoAzulx','DepoAzuly','DepoCelx','DepoCely','EPix','Emm','o1_AC','o1_AS','o1_SA','o1_DA','o2_AC','o2_AS','o2_SA','o2_DA','o3_AC','o3_AS','o3_SA','o3_DA']
		writer = csv.DictWriter(f, fieldnames=fnames)  
    
		#print(globales.tarjeta_camara)
		writer.writeheader()
		writer.writerow({'camara' : str(globales.tarjeta_camara), 'st_omni1': str(globales.st_omni1),'st_omni2': str(globales.st_omni2), 'st_omni3': str(globales.st_omni3),'limIzq':str(globales.capIz),'limDer':str(globales.capDe),'limSup':str(globales.capSu),'limInf':str(globales.capInf),'DivH':str(globales.divH),'DivV':str(globales.divV),'DepoRojox':aux_pRx,'DepoRojoy':aux_pRy,'DepoAzulx':aux_pAx,'DepoAzuly':aux_pAy,'DepoCelx':aux_pCx,'DepoCely':aux_pCy,'EPix':str(globales.EscPix),'Emm':str(globales.EscMM),'o1_AC':str(globales.omni1_Area_Cent),'o1_AS':str(globales.omni1_Area_Sec),'o1_SA':str(globales.omni1_Sep_Area),'o1_DA':str(globales.omni1_Dist_Act),'o2_AC':str(globales.omni2_Area_Cent),'o2_AS':str(globales.omni2_Area_Sec),'o2_SA':str(globales.omni2_Sep_Area),'o2_DA':str(globales.omni2_Dist_Act),'o3_AC':str(globales.omni3_Area_Cent),'o3_AS':str(globales.omni3_Area_Sec),'o3_SA':str(globales.omni3_Sep_Area),'o3_DA':str(globales.omni3_Dist_Act)})


def trans_load_vec(aux_):
	aux1=aux_
	aux2=aux1.split(sep='+')
	aux3=[]
	if aux2[0]!='':
		for i in range(len(aux2)):
			aux3.append(int(aux2[i]))
	return aux3


def trans_save_vec(aux1):
	aux_=str(aux1)
	aux_=aux_[1:len(aux_)-1]
	aux_=aux_.split(sep=', ')
	aux_='+'.join(aux_)
	return aux_

def detec_cam():
	try:
		videos=[]
		args = 'ls /dev/video*'
		a1=subprocess.run(args,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		msgs=a1.stdout.decode('utf-8')
		if a1.returncode==0:
			#print('returncode:', a1.returncode)
			aux=0
			for c in range(len(msgs)):
				if msgs[c].isspace():
					videos.append(msgs[aux:c])
					aux=c+1
		else:
			videos.append("No hay cámaras disponibles")


		#print(videos)
	except Exception as e:
		videos.append('error de lectura:')
		videos.append(e)

	return videos

def form_cuadricula(img,cuadricula):
	for i in range(len(cuadricula)):
		imag1 = cv2.rectangle(img,(cuadricula[i][0][0],cuadricula[i][0][1]),(cuadricula[i][1][0],cuadricula[i][1][1]),(0,255,0),1)

	return imag1

def form_cuad_dep(img,cuadricula,indice,color_p):
	for i in range(len(indice)):
		if color_p==0:
			img = cv2.rectangle(img,(cuadricula[indice[i]][0][0],cuadricula[indice[i]][0][1]),(cuadricula[indice[i]][1][0],cuadricula[indice[i]][1][1]),(0,0,255),-1)
		if color_p==1:
			img = cv2.rectangle(img,(cuadricula[indice[i]][0][0],cuadricula[indice[i]][0][1]),(cuadricula[indice[i]][1][0],cuadricula[indice[i]][1][1]),(255,0,0),-1)
		if color_p==2:
			img = cv2.rectangle(img,(cuadricula[indice[i]][0][0],cuadricula[indice[i]][0][1]),(cuadricula[indice[i]][1][0],cuadricula[indice[i]][1][1]),(242, 183, 12),-1)

	return img

def Buscar_pt_cuadricula(px,py,cuadricula):
	aux_pts=[0,0,0]
	band=0

	for i in range(len(cuadricula)):

		if px>=cuadricula[i][0][0] and px<=cuadricula[i][1][0] and py >=cuadricula[i][0][1] and py <= cuadricula[i][1][1]:
			aux_pts[0]=int((cuadricula[i][1][0]-cuadricula[i][0][0])/2+cuadricula[i][0][0])
			aux_pts[1]=int((cuadricula[i][1][1]-cuadricula[i][0][1])/2+cuadricula[i][0][1])
			aux_pts[2]=i
			band=1
			return aux_pts
	if band==0:
		return []

def Init_cuad():
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
			elif limDx>globales.capDe and limDy<= globales.capInf:
				aux_cuadricula.append(([limIx,limIy],[globales.capDe,limDy]))
			elif limDx<=globales.capDe and limDy>globales.capInf:
				aux_cuadricula.append(([limIx,limIy],[limDx,globales.capInf]))
			else:
				aux_cuadricula.append(([limIx,limIy],[globales.capDe,globales.capInf]))

			globales.cuadricula=aux_cuadricula

def init_dep():
	aux_selec=[]
	globales.cuadricula_rojo=[]
	globales.Drojo=[]
	globales.cuadricula_azul=[]
	globales.Dazul=[]
	globales.cuadricula_celeste=[]
	globales.Dceleste=[]

	if globales.DepoRojoX!=[] and globales.DepoRojoY!=[]:
		for i in range(len(globales.DepoRojoX)):
			aux_selec=Buscar_pt_cuadricula(globales.DepoRojoX[i],globales.DepoRojoY[i],globales.cuadricula)
			globales.cuadricula_rojo.append(aux_selec[2])
			globales.Drojo.append(aux_selec[0:1])

	if globales.DepoAzulX!=[] and globales.DepoAzulY!=[]:
		for i in range(len(globales.DepoAzulX)):
			aux_selec=Buscar_pt_cuadricula(globales.DepoAzulX[i],globales.DepoAzulY[i],globales.cuadricula)
			globales.cuadricula_azul.append(aux_selec[2])
			globales.Dazul.append(aux_selec[0:1])

	if globales.DepoCelY!=[] and globales.DepoCelY!=[]:
		for i in range(len(globales.DepoCelX)):
			aux_selec=Buscar_pt_cuadricula(globales.DepoCelX[i],globales.DepoCelY[i],globales.cuadricula)
			globales.cuadricula_celeste.append(aux_selec[2])
			globales.Dceleste.append(aux_selec[0:1])

def detec_pos_omni_one(n,img):
	img1=img.copy()
	frame = cv2.cvtColor(img1.copy(), cv2.COLOR_BGR2HSV)
	deteccion=0
	
	if n==0:
		if globales.st_omni1==1:
			mask = cv2.inRange(frame, globales.azulBajo, globales.azulAlto)
			

			_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			if len(contornos)>0:
				for c in contornos:
					nuevoContorno = cv2.convexHull(c)
					rect = cv2.minAreaRect(nuevoContorno)
					box = cv2.boxPoints(rect)
					box = np.int0(box)
					area = cv2.contourArea(box)
					if area > globales.omni1_Area_Cent-500 and area < globales.omni1_Area_Cent+200:
						deteccion+=1
						M = cv2.moments(nuevoContorno)
						if (M["m00"]==0): M["m00"]=1
						x = int(M["m10"]/M["m00"])
						y = int(M['m01']/M['m00'])
						img1=cv2.circle(img1.copy(), (x,y), 4, (0,255,0), -1)
						#font = cv2.FONT_HERSHEY_SIMPLEX
						pts=CalcularXYZ(x,y)
						#print(int(pts[0]),int(pts[1][0]))
						#cv2.putText(img1, '{},{}'.format(int(pts[0]),int(pts[1][0])),(int(x-100),int(y)), font, 0.75,(0,255,0),1,cv2.LINE_AA)

						#cv2.drawContours(img1,[box],0,(0,0,255),2)
				if deteccion==1:
					deteccion=0
					return img1,int(pts[0]),int(pts[1][0])
				elif deteccion>1:
					deteccion=0
					return img1,-20000,-20000
				else:
					deteccion=0
					return img1,-30000,-30000

			else:
				deteccion=0
				return img1,-10000,-10000
		else:
			deteccion=0
			return img1,-40000,-40000
	elif n==1:
		if globales.st_omni2==1:
			mask = cv2.inRange(frame, globales.verdeBajo, globales.verdeAlto)
			_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

			if len(contornos)>0:
				for c in contornos:
					nuevoContorno = cv2.convexHull(c)
					
					rect = cv2.minAreaRect(nuevoContorno)
					box = cv2.boxPoints(rect)
					box = np.int0(box)
					#cv2.drawContours(img1,[box],0,(0,0,255),2)
					area = cv2.contourArea(box)
					if area > globales.omni2_Area_Cent-100 and area < globales.omni2_Area_Cent+450:
						deteccion+=1
						M = cv2.moments(nuevoContorno)
						if (M["m00"]==0): M["m00"]=1
						x = int(M["m10"]/M["m00"])
						y = int(M['m01']/M['m00'])
						img1=cv2.circle(img1.copy(), (x,y), 4, (0,255,0), -1)
						#font = cv2.FONT_HERSHEY_SIMPLEX
						pts=CalcularXYZ(x,y)
						#print(int(pts[0]),int(pts[1][0]))
						#cv2.putText(img1, '{},{}'.format(int(pts[0]),int(pts[1][0])),(int(x-100),int(y)), font, 0.75,(0,255,0),1,cv2.LINE_AA)

						#cv2.drawContours(img1,[box],0,(0,0,255),2)
				if deteccion==1:
					deteccion=0
					return img1,int(pts[0]),int(pts[1][0])
				elif deteccion>1:
					deteccion=0
					return img1,-20000,-20000
				else:
					deteccion=0
					return img1,-30000,-30000

			else:
				deteccion=0
				return img1,-10000,-10000
		else:
			deteccion=0
			return img1,-40000,-40000
	elif n==2:
		if globales.st_omni3==1:
			mask1 = cv2.inRange(frame, globales.rojoBajo1, globales.rojoAlto1)
			mask2 = cv2.inRange(frame, globales.rojoBajo2, globales.rojoAlto2)
			mask = cv2.add(mask1, mask2)
			_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			if len(contornos)>0:
				for c in contornos:
					nuevoContorno = cv2.convexHull(c)
					rect = cv2.minAreaRect(nuevoContorno)
					box = cv2.boxPoints(rect)
					box = np.int0(box)
					area = cv2.contourArea(box)

					if area > globales.omni3_Area_Cent-500 and area < globales.omni3_Area_Cent+100:
						#print(globales.omni3_Area_Sec)
						deteccion+=1
						M = cv2.moments(nuevoContorno)
						if (M["m00"]==0): M["m00"]=1
						x = int(M["m10"]/M["m00"])
						y = int(M['m01']/M['m00'])
						img1=cv2.circle(img1.copy(), (x,y), 4, (0,255,0), -1)
						#font = cv2.FONT_HERSHEY_SIMPLEX
						pts=CalcularXYZ(x,y)
						#print(int(pts[0]),int(pts[1][0]))
						#cv2.putText(img1, '{},{}'.format(int(pts[0]),int(pts[1][0])),(int(x-100),int(y)), font, 0.75,(0,255,0),1,cv2.LINE_AA)
						#cv2.drawContours(img1,[box],0,(0,0,255),2)
						#cv2.drawContours(img1,[box],0,(0,0,255),2)
				if deteccion==1:
					deteccion=0
					return img1,int(pts[0]),int(pts[1][0])
				elif deteccion>1:
					deteccion=0
					return img1,-20000,-20000
				else:
					deteccion=0
					return img1,-30000,-30000

			else:
				deteccion=0
				return img1,-10000,-10000
		else:
			deteccion=0
			return img1,-40000,-40000


def CalcularXYZ(u,v):#, s):
    # Generamos el vector m
	uv = np.array([[u,v,1]], dtype=np.float).T
    # Obtenemos R a partir de rvec
	R, _ = cv2.Rodrigues(globales.rvec)
	Inv_R = np.linalg.inv(R)
    # Parte izquierda m*A^(-1)*R^(-1)
	Izda = Inv_R.dot(np.linalg.inv(globales.mtx).dot(uv))
    # Parte derecha
	Drch = Inv_R.dot(globales.tvec)
    # Calculamos S porque sabemos Z = 0
	s = 0 + Drch[2][0]/Izda[2][0]
	XYZ = Inv_R.dot( s * np.linalg.inv(globales.mtx).dot(uv) - globales.tvec)
	aux_x=XYZ[0]
	XYZ[0]=aux_x+(-107.5+0.3075*aux_x-0.0002876*aux_x*aux_x+aux_x*aux_x*aux_x*0.0000000834)
	return XYZ


###CALCULAR PUNTOS IOT
def detec_pos_omni_iot(img):
	img1=img.copy()
	img2=img.copy()
	om1x=0
	om1y=0
	om2x=0
	om2y=0
	om3x=0
	om3y=0
	frame = cv2.cvtColor(img1.copy(), cv2.COLOR_BGR2HSV)
	deteccion=0
	if globales.st_omni1==1:
		mask = cv2.inRange(frame.copy(), globales.azulBajo, globales.azulAlto)
		_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		if len(contornos)>0:
			for c in contornos:
				nuevoContorno = cv2.convexHull(c)
				rect = cv2.minAreaRect(nuevoContorno)
				box = cv2.boxPoints(rect)
				box = np.int0(box)
				area = cv2.contourArea(box)
				if area > globales.omni1_Area_Cent-500 and area < globales.omni1_Area_Cent+200:
					deteccion+=1
					M = cv2.moments(nuevoContorno)
					if (M["m00"]==0): M["m00"]=1
					x = int(M["m10"]/M["m00"])
					y = int(M['m01']/M['m00'])
					img2=cv2.circle(img2.copy(), (x,y), 4, (0,255,0), -1)
					#font = cv2.FONT_HERSHEY_SIMPLEX
					pts=CalcularXYZ(x,y)
					#print(int(pts[0]),int(pts[1][0]))
					#img2=cv2.putText(img2.copy(), '{},{}'.format(int(pts[0]),int(pts[1][0])),(int(x-100),int(y)), font, 0.75,(0,255,0),1,cv2.LINE_AA)

					#img2=cv2.drawContours(img2.copy(),[box],0,(0,0,255),2)
			if deteccion==1:
				deteccion=0
				om1x=int(pts[0])
				om1y=int(pts[1][0])
			elif deteccion>1:
				deteccion=0
				om1x=0
				om1y=0
			else:
				deteccion=0
				om1x=0
				om1y=0

		else:
			deteccion=0
			om1x=0
			om1y=0
	else:
		deteccion=0
		om1x=0
		om1y=0

	if globales.st_omni2==1:
		mask = cv2.inRange(frame.copy(), globales.verdeBajo, globales.verdeAlto)
		_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		if len(contornos)>0:
			for c in contornos:
				nuevoContorno = cv2.convexHull(c)
				rect = cv2.minAreaRect(nuevoContorno)
				box = cv2.boxPoints(rect)
				box = np.int0(box)
				area = cv2.contourArea(box)
				if area > globales.omni2_Area_Cent-600 and area < globales.omni2_Area_Cent+300:
					deteccion+=1
					M = cv2.moments(nuevoContorno)
					if (M["m00"]==0): M["m00"]=1
					x = int(M["m10"]/M["m00"])
					y = int(M['m01']/M['m00'])
					img2=cv2.circle(img2.copy(), (x,y), 4, (0,255,0), -1)
					#font = cv2.FONT_HERSHEY_SIMPLEX
					pts=CalcularXYZ(x,y)
					#print(int(pts[0]),int(pts[1][0]))
					#img2=cv2.putText(img2.copy(), '{},{}'.format(int(pts[0]),int(pts[1][0])),(int(x-100),int(y)), font, 0.75,(0,255,0),1,cv2.LINE_AA)

					#img2-cv2.drawContours(img2.copy(),[box],0,(0,0,255),2)
			if deteccion==1:
				deteccion=0
				om2x=int(pts[0])
				om2y=int(pts[1][0])
			elif deteccion>1:
				deteccion=0
				om2x=0
				om2y=0
			else:
				deteccion=0
				om2x=0
				om2y=0

		else:
			deteccion=0
			om2x=0
			om2y=0
	else:
		deteccion=0
		om2x=0
		om2y=0


	if globales.st_omni3==1:
		mask1 = cv2.inRange(frame.copy(), globales.rojoBajo1, globales.rojoAlto1)
		mask2 = cv2.inRange(frame.copy(), globales.rojoBajo2, globales.rojoAlto2)
		mask = cv2.add(mask1, mask2)
		_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		if len(contornos)>0:
			for c in contornos:
				nuevoContorno = cv2.convexHull(c)
				rect = cv2.minAreaRect(nuevoContorno)
				box = cv2.boxPoints(rect)
				box = np.int0(box)
				area = cv2.contourArea(box)
				if area > globales.omni3_Area_Cent-500 and area < globales.omni3_Area_Cent+100:
					deteccion+=1
					M = cv2.moments(nuevoContorno)
					if (M["m00"]==0): M["m00"]=1
					x = int(M["m10"]/M["m00"])
					y = int(M['m01']/M['m00'])
					img2=cv2.circle(img2.copy(), (x,y), 4, (0,255,0), -1)
					#font = cv2.FONT_HERSHEY_SIMPLEX
					pts=CalcularXYZ(x,y)
					#print(int(pts[0]),int(pts[1][0]))
					#img2=cv2.putText(img2.copy(), '{},{}'.format(int(pts[0]),int(pts[1][0])),(int(x-100),int(y)), font, 0.75,(0,255,0),1,cv2.LINE_AA)

					#img2=cv2.drawContours(img2.copy(),[box],0,(0,0,255),2)
			if deteccion==1:
				deteccion=0
				om3x=int(pts[0])
				om3y=int(pts[1][0])
			elif deteccion>1:
				deteccion=0
				om3x=0
				om3y=0
			else:
				deteccion=0
				om3x=0
				om3y=0

		else:
			deteccion=0
			om3x=0
			om3y=0
	else:
		deteccion=0
		om3x=0
		om3y=0

	return img2,om1x,om1y,om2x,om2y,om3x,om3y


###CALCULAR PUNTOS OMNI EN AUTO
def detec_pos_omni_auto(img):
	img1=img.copy()
	img2=img.copy()
	om1x=0
	om1y=0
	om2x=0
	om2y=0
	om3x=0
	om3y=0
	frame = cv2.cvtColor(img1.copy(), cv2.COLOR_BGR2HSV)
	deteccion=0
	if globales.st_omni1==1:
		mask = cv2.inRange(frame.copy(), globales.azulBajo, globales.azulAlto)
		_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		if len(contornos)>0:
			for c in contornos:
				nuevoContorno = cv2.convexHull(c)
				rect = cv2.minAreaRect(nuevoContorno)
				box = cv2.boxPoints(rect)
				box = np.int0(box)
				area = cv2.contourArea(box)
				if area > globales.omni1_Area_Cent-500 and area < globales.omni1_Area_Cent+200:
					deteccion+=1
					M = cv2.moments(nuevoContorno)
					if (M["m00"]==0): M["m00"]=1
					x = int(M["m10"]/M["m00"])
					y = int(M['m01']/M['m00'])
					img2=cv2.circle(img2.copy(), (x,y), 4, (0,255,0), -1)
					#font = cv2.FONT_HERSHEY_SIMPLEX
					
					pts=CalcularXYZ(x,y)
					#print(int(pts[0]),int(pts[1][0]))
					#img2=cv2.putText(img2.copy(), '{},{}'.format(int(pts[0]),int(pts[1][0])),(int(x-100),int(y)), font, 0.75,(0,255,0),1,cv2.LINE_AA)

					#img2=cv2.drawContours(img2.copy(),[box],0,(0,0,255),2)
			if deteccion==1:
				deteccion=0
				globales.pts_px_omni_1=[x,y]
				om1x=int(pts[0])
				om1y=int(pts[1][0])
			elif deteccion>1:
				deteccion=0
				om1x=0
				om1y=0
			else:
				deteccion=0
				om1x=0
				om1y=0

		else:
			deteccion=0
			om1x=0
			om1y=0
	else:
		deteccion=0
		om1x=0
		om1y=0

	if globales.st_omni2==1:
		mask = cv2.inRange(frame.copy(), globales.verdeBajo, globales.verdeAlto)
		_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		if len(contornos)>0:
			for c in contornos:
				nuevoContorno = cv2.convexHull(c)
				rect = cv2.minAreaRect(nuevoContorno)
				box = cv2.boxPoints(rect)
				box = np.int0(box)
				area = cv2.contourArea(box)
				if area > globales.omni2_Area_Cent-300 and area < globales.omni2_Area_Cent+350:
					deteccion+=1
					M = cv2.moments(nuevoContorno)
					if (M["m00"]==0): M["m00"]=1
					x = int(M["m10"]/M["m00"])
					y = int(M['m01']/M['m00'])
					img2=cv2.circle(img2.copy(), (x,y), 4, (0,255,0), -1)
					#font = cv2.FONT_HERSHEY_SIMPLEX
					pts=CalcularXYZ(x,y)
					#print(int(pts[0]),int(pts[1][0]))
					#img2=cv2.putText(img2.copy(), '{},{}'.format(int(pts[0]),int(pts[1][0])),(int(x-100),int(y)), font, 0.75,(0,255,0),1,cv2.LINE_AA)

					#img2-cv2.drawContours(img2.copy(),[box],0,(0,0,255),2)
			if deteccion==1:
				deteccion=0
				globales.pts_px_omni_2=[x,y]
				om2x=int(pts[0])
				om2y=int(pts[1][0])
			elif deteccion>1:
				deteccion=0
				om2x=0
				om2y=0
			else:
				deteccion=0
				om2x=0
				om2y=0

		else:
			deteccion=0
			om2x=0
			om2y=0
	else:
		deteccion=0
		om2x=0
		om2y=0


	if globales.st_omni3==1:
		mask1 = cv2.inRange(frame.copy(), globales.rojoBajo1, globales.rojoAlto1)
		mask2 = cv2.inRange(frame.copy(), globales.rojoBajo2, globales.rojoAlto2)
		mask = cv2.add(mask1, mask2)
		_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		if len(contornos)>0:
			for c in contornos:
				nuevoContorno = cv2.convexHull(c)
				rect = cv2.minAreaRect(nuevoContorno)
				box = cv2.boxPoints(rect)
				box = np.int0(box)
				area = cv2.contourArea(box)
				if area > globales.omni3_Area_Cent-500 and area < globales.omni3_Area_Cent+100:
					deteccion+=1
					M = cv2.moments(nuevoContorno)
					if (M["m00"]==0): M["m00"]=1
					x = int(M["m10"]/M["m00"])
					y = int(M['m01']/M['m00'])
					img2=cv2.circle(img2.copy(), (x,y), 4, (0,255,0), -1)
					#font = cv2.FONT_HERSHEY_SIMPLEX
					pts=CalcularXYZ(x,y)
					#print(int(pts[0]),int(pts[1][0]))
					#img2=cv2.putText(img2.copy(), '{},{}'.format(int(pts[0]),int(pts[1][0])),(int(x-100),int(y)), font, 0.75,(0,255,0),1,cv2.LINE_AA)

					#img2=cv2.drawContours(img2.copy(),[box],0,(0,0,255),2)
			if deteccion==1:
				deteccion=0
				globales.pts_px_omni_3=[x,y]
				om3x=int(pts[0])
				om3y=int(pts[1][0])
			elif deteccion>1:
				deteccion=0
				om3x=0
				om3y=0
			else:
				deteccion=0
				om3x=0
				om3y=0

		else:
			deteccion=0
			om3x=0
			om3y=0
	else:
		deteccion=0
		om3x=0
		om3y=0

	return img2,om1x,om1y,om2x,om2y,om3x,om3y

def detectar_dir_n_omni(img,n):
	img1=img.copy()
	frame = cv2.cvtColor(img1.copy(), cv2.COLOR_BGR2HSV)
	deteccion=0
	
	if n==0:
		mask = cv2.inRange(frame, globales.azulBajo, globales.azulAlto)
		_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		if len(contornos)>0:
			for c in contornos:
				nuevoContorno = cv2.convexHull(c)
				rect = cv2.minAreaRect(nuevoContorno)
				box = cv2.boxPoints(rect)
				box = np.int0(box)
				area = cv2.contourArea(box)
				if area > globales.omni1_Area_Sec-110 and area < globales.omni1_Area_Sec+150:
					deteccion+=1
					M = cv2.moments(nuevoContorno)
					if (M["m00"]==0): M["m00"]=1
					x = int(M["m10"]/M["m00"])
					y = int(M['m01']/M['m00'])
					pts=CalcularXYZ(x,y)
			if deteccion==1:
				deteccion=0
				return [int(pts[0]),int(pts[1][0])]
			elif deteccion>1:
				deteccion=0
				return []
			else:
				deteccion=0
				return []
		else:
			deteccion=0
			return []
	elif n==1:
		mask = cv2.inRange(frame, globales.verdeBajo, globales.verdeAlto)
		_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		if len(contornos)>0:
			for c in contornos:
				nuevoContorno = cv2.convexHull(c)
				rect = cv2.minAreaRect(nuevoContorno)
				box = cv2.boxPoints(rect)
				box = np.int0(box)
				area = cv2.contourArea(box)
				if area > globales.omni2_Area_Sec-20 and area < globales.omni2_Area_Sec+200:
					deteccion+=1
					M = cv2.moments(nuevoContorno)
					if (M["m00"]==0): M["m00"]=1
					x = int(M["m10"]/M["m00"])
					y = int(M['m01']/M['m00'])
					pts=CalcularXYZ(x,y)
			if deteccion==1:
				deteccion=0
				return [int(pts[0]),int(pts[1][0])]
			elif deteccion>1:
				deteccion=0
				return []
			else:
				deteccion=0
				return []
		else:
			deteccion=0
			return []

	
	elif n==2:
		mask1 = cv2.inRange(frame, globales.rojoBajo1, globales.rojoAlto1)
		mask2 = cv2.inRange(frame, globales.rojoBajo2, globales.rojoAlto2)
		mask = cv2.add(mask1, mask2)
		_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		if len(contornos)>0:
			for c in contornos:
				nuevoContorno = cv2.convexHull(c)
				rect = cv2.minAreaRect(nuevoContorno)
				box = cv2.boxPoints(rect)
				box = np.int0(box)
				area = cv2.contourArea(box)

				if area > globales.omni3_Area_Sec-100 and area < globales.omni3_Area_Sec+200:#
					deteccion+=1
					M = cv2.moments(nuevoContorno)
					if (M["m00"]==0): M["m00"]=1
					x = int(M["m10"]/M["m00"])
					y = int(M['m01']/M['m00'])
					pts=CalcularXYZ(x,y)
			if deteccion==1:
				deteccion=0
				return [int(pts[0]),int(pts[1][0])]
			elif deteccion>1:
				deteccion=0
				return []
			else:
				deteccion=0
				return []
		else:
			deteccion=0
			return []
			
def guardar_datos_exp1(n,omni_n):
	dir_img=''
	now=datetime.now()
	fechag=str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)
	if n==1:
		dir_data=globales.dir_work_aux+"/data/p2t/"+fechag+"omni"+str(omni_n+1)+"p2p.csv"
	elif n==2:
		if globales.tray_alg==0:
			dir_data=globales.dir_work_aux+"/data/Trayectoria/Simulacion_objetos/campos/"+fechag+"omni"+str(omni_n+1)+"tsimC.csv"
			dir_img=globales.dir_work_aux+"/data/Trayectoria/Simulacion_objetos/campos/"+fechag+"omni"+str(omni_n+1)+"tsimC.jpg"
		else:
			dir_data=globales.dir_work_aux+"/data/Trayectoria/Simulacion_objetos/A_estrella/"+fechag+"omni"+str(omni_n+1)+"tsimS.csv"
			dir_img=globales.dir_work_aux+"/data/Trayectoria/Simulacion_objetos/A_estrella/"+fechag+"omni"+str(omni_n+1)+"tsimS.jpg"

	elif n==3:
		if globales.tray_alg==0:
			dir_data=globales.dir_work_aux+"/data/Trayectoria/Deteccion_objetos/campos/"+fechag+"omni"+str(omni_n+1)+"trayC.csv"
			dir_img=globales.dir_work_aux+"/data/Trayectoria/Deteccion_objetos/campos/"+fechag+"omni"+str(omni_n+1)+"trayC.jpg"
		else:
			dir_data=globales.dir_work_aux+"/data/Trayectoria/Deteccion_objetos/A_estrella/"+fechag+"omni"+str(omni_n+1)+"trayS.csv"
			dir_img=globales.dir_work_aux+"/data/Trayectoria/Deteccion_objetos/A_estrella/"+fechag+"omni"+str(omni_n+1)+"trayS.jpg"

	f = open(dir_data, 'w')

	with f:

		if n==1:
			fnames = ['Ptox', 'Ptoy','Destx','Desty','Ptfx','Ptfy']
			writer = csv.DictWriter(f, fieldnames=fnames)  
    
			#print(globales.tarjeta_camara)
			writer.writeheader()
			writer.writerow({'Ptox' : str(globales.opc1_pto[0]), 'Ptoy': str(globales.opc1_pto[1]),'Destx': str(globales.opc1_dest[0]), 'Desty': str(globales.opc1_dest[1]),'Ptfx':str(globales.opc1_ptf[0]),'Ptfy':str(globales.opc1_ptf[1])})
		elif n==2 or n==3:
			fnames = ['Tray_omni_x', 'Tray_omni_y','Tray_gen_x','Tray_gen_y']
			writer = csv.DictWriter(f, fieldnames=fnames)  
    
			#print(globales.tarjeta_camara)
			writer.writeheader()
			for i in range (len(globales.pts_tray_aux_omni)):
				writer.writerow({'Tray_omni_x' : str(globales.pts_tray_aux_omni[i][0]), 'Tray_omni_y': str(globales.pts_tray_aux_omni[i][1]),'Tray_gen_x': str(globales.pts_tray_aux[i][0]), 'Tray_gen_y': str(globales.pts_tray_aux[i][1])})

			graftrayec(dir_img)

def guardar_datos_exp2(n):
	now=datetime.now()
	fechag=str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)
	if n==4:
		dir_data=globales.dir_work_aux+"/data/Simulacion/"+fechag+"csim.csv"
	elif n==5:
		dir_data=globales.dir_work_aux+"/data/Deteccion_clasificacion/"+fechag+"clas.csv"
	

	f = open(dir_data, 'w')

	with f:

		if n==4:			
			fnames = ['Ptox', 'Ptoy','Destx','Desty','Ptfx','Ptfy']
			writer = csv.DictWriter(f, fieldnames=fnames)  
    
			#print(globales.tarjeta_camara)
			writer.writeheader()
			writer.writerow({'Ptox' : str(globales.opc1_pto[0]), 'Ptoy': str(globales.opc1_pto[1]),'Destx': str(globales.opc1_dest[0]), 'Desty': str(globales.opc1_dest[1]),'Ptfx':str(globales.opc1_ptf[0]),'Ptfy':str(globales.opc1_ptf[1])})


def init_cuad_obstaculos():
	#Valores paara cuadricula
	aux_cuadricula=[]
	
	n_aux=globales.pt_max_x/globales.grid_tray
	if n_aux > int(n_aux):
		n=int(n_aux)+1
	else:
		n=int(n_aux)
	m_aux=globales.pt_max_y/globales.grid_tray
	if m_aux > int(m_aux):
		m=int(m_aux)+1
	else:
		m=int(m_aux)

	di=globales.capDe-globales.capIz
	dj=globales.capInf- globales.capSu
	dh=di/n
	if dh> int(dh):
		dh=int(dh)+1
	else:
		dh=int(dh)
	dl=dj/m
	if dl> int(dl):
		dl=int(dl)+1
	else:
		dl=int(dl)

	for i in range(m):
		
		for j in range(n):
			#aux_cuadricula.append([])
			limIx=dh*(j)+globales.capIz
			limIy=dl*(i)+globales.capSu
			limDx=dh*(j+1)+globales.capIz
			limDy=dl*(i+1)+globales.capSu

			if limDx<=globales.capDe and limDy<=globales.capInf:
				aux_cuadricula.append(([limIx,limIy],[limDx,limDy]))
			elif limDx>globales.capDe and limDy<= globales.capInf:
				aux_cuadricula.append(([limIx,limIy],[globales.capDe,limDy]))
			elif limDx<=globales.capDe and limDy>globales.capInf:
				aux_cuadricula.append(([limIx,limIy],[limDx,globales.capInf]))
			else:
				aux_cuadricula.append(([limIx,limIy],[globales.capDe,globales.capInf]))

			globales.cuad_grid_obs=aux_cuadricula

def grid_obstaculos(imag):
	img=form_cuadricula(imag.copy(),globales.cuad_grid_obs)
	for i in range(len(globales.cuad_obs)):
		img = cv2.rectangle(img,(globales.cuad_grid_obs[globales.cuad_obs[i]][0][0],globales.cuad_grid_obs[globales.cuad_obs[i]][0][1]),(globales.cuad_grid_obs[globales.cuad_obs[i]][1][0],globales.cuad_grid_obs[globales.cuad_obs[i]][1][1]),(0,0,0),-1)

	return img

def grid_objetos(imag):
	img=imag.copy()
	for i in range(len(globales.cuad_obj_rojos)):
		img=cv2.circle(img.copy(),(int(globales.cuad_grid_obs[globales.cuad_obj_rojos[i]][0][0]+(globales.cuad_grid_obs[globales.cuad_obj_rojos[i]][1][0]-globales.cuad_grid_obs[globales.cuad_obj_rojos[i]][0][0])/2),int(globales.cuad_grid_obs[globales.cuad_obj_rojos[i]][1][1]-(globales.cuad_grid_obs[globales.cuad_obj_rojos[i]][1][1]-globales.cuad_grid_obs[globales.cuad_obj_rojos[i]][0][1])/2)),10,(0,0,255),-1)
		

	for i in range(len(globales.cuad_obj_azul)):
		img=cv2.circle(img.copy(),(int(globales.cuad_grid_obs[globales.cuad_obj_azul[i]][0][0]+(globales.cuad_grid_obs[globales.cuad_obj_azul[i]][1][0]-globales.cuad_grid_obs[globales.cuad_obj_azul[i]][0][0])/2),int(globales.cuad_grid_obs[globales.cuad_obj_azul[i]][1][1]-(globales.cuad_grid_obs[globales.cuad_obj_azul[i]][1][1]-globales.cuad_grid_obs[globales.cuad_obj_azul[i]][0][1])/2)),10,(255,0,0),-1)
		
	for i in range(len(globales.cuad_obj_celeste)):
		img=cv2.circle(img.copy(),(int(globales.cuad_grid_obs[globales.cuad_obj_celeste[i]][0][0]+(globales.cuad_grid_obs[globales.cuad_obj_celeste[i]][1][0]-globales.cuad_grid_obs[globales.cuad_obj_celeste[i]][0][0])/2),int(globales.cuad_grid_obs[globales.cuad_obj_celeste[i]][1][1]-(globales.cuad_grid_obs[globales.cuad_obj_celeste[i]][1][1]-globales.cuad_grid_obs[globales.cuad_obj_celeste[i]][0][1])/2)),10,(228,170,0),-1)
		
		
	img=cv2.circle(img.copy(), (globales.DepoRojoX[0],globales.DepoRojoY[0]), 8, (0,0,255), -1)
	#font = cv2.FONT_HERSHEY_SIMPLEX
	#img=cv2.putText(img.copy(), 'Deposito Rojo',(int(globales.DepoRojoX[0]-100),int(globales.DepoRojoY[0]-10)), font, 0.55,(0,0,255),1,cv2.LINE_AA)
	
	img=cv2.circle(img.copy(), (globales.DepoAzulX[0],globales.DepoAzulY[0]), 8, (255,0,0), -1)
	#font = cv2.FONT_HERSHEY_SIMPLEX
	#img=cv2.putText(img.copy(), 'Deposito Azul',(int(globales.DepoAzulX[0]-100),int(globales.DepoAzulY[0]-10)), font, 0.55,(255,0,0),1,cv2.LINE_AA)
	
	img=cv2.circle(img.copy(), (globales.DepoCelX[0],globales.DepoCelY[0]), 8, (228,170,0), -1)
	#font = cv2.FONT_HERSHEY_SIMPLEX
	#img=cv2.putText(img.copy(), 'Deposito Celeste',(int(globales.DepoCelX[0]-100),int(globales.DepoCelY[0]-10)), font, 0.55,(228,170,0),1,cv2.LINE_AA)
	
	return img

#GUARDAR IMAGEN DE TRAYECTORIA
def graftrayec(dir_aux):
	grid_size=globales.grid_tray/1000
	intervalox=np.arange(0,globales.pt_max_x/1000,grid_size)   	  # intervalos para imagen grid x
	intervaloy=np.arange(0,globales.pt_max_y/1000,grid_size) 	  # intervalos para imagen grid y
	ox = []  # obstaculos x
	oy = []  # obstaculos y
	px = [] #puntos trayectoria x teorica
	py = [] #puntos trayectoria y teorica
	pxp= [] #puntos trayectoria x practica
	pyp= [] #puntos trayectoria y practica
	for i in range(len(globales.pts_tray_obs)):
		ox.append(globales.pts_tray_obs[i][0]/1000)
		oy.append(globales.pts_tray_obs[i][1]/1000)
	for i in range(len(globales.pts_tray_aux)):
		px.append(globales.pts_tray_aux[i][0]/1000)
		py.append(globales.pts_tray_aux[i][1]/1000)
		pxp.append(globales.pts_tray_aux_omni[i][0]/1000)
		pyp.append(globales.pts_tray_aux_omni[i][1]/1000)
	print(px,py)
	print(pxp,pyp)
	plt.axis([0,globales.pt_max_x/1000,0,globales.pt_max_y/1000])	#deino los ejes
	plt.plot(px,py, marker="o", color="red")	#grafica de trayectoria teorica
	plt.plot(pxp,pyp,marker="o",color="blue")	#grafica de trayectoria practica
	plt.scatter(ox,oy, marker="X", color="black" )	#grafica de obstaculos
	plt.xticks(intervalox)
	plt.yticks(intervaloy)
	plt.grid(grid_size)
	plt.title("Gráfica Trayectoria Teorica vs Práctica")
	plt.xlabel('Eje de las x')
	plt.ylabel('Eje de las y')
	rojo = mpatches.Patch(color='red', label='Trayectoria teorica')
	azul = mpatches.Patch(color='blue', label='Trayectoria practica')
	plt.legend(handles=[rojo,azul])
	plt.savefig(dir_aux) 
	plt.show()

#detectar obstaculos automatico
def detectar_obstaculos(img):
	img1=img.copy()
	frame = cv2.cvtColor(img1.copy(), cv2.COLOR_BGR2HSV)
	deteccion=0
	
	mask = cv2.inRange(frame, globales.obstaculoBajo, globales.obstaculoAlto)
	_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	if len(contornos)>0:
		for c in contornos:
			nuevoContorno = cv2.convexHull(c)
			rect = cv2.minAreaRect(nuevoContorno)
			box = cv2.boxPoints(rect)
			box = np.int0(box)
			area = cv2.contourArea(box)
			if area > globales.area_objeto[0] and area < globales.area_objeto[1]:
				#deteccion+=1
				M = cv2.moments(nuevoContorno)
				if (M["m00"]==0): M["m00"]=1
				x = int(M["m10"]/M["m00"])
				y = int(M['m01']/M['m00'])
				globales.pts_aux_obs_det.append([x,y])

def pant_obstaculos(img):
	img1=img.copy()
	frame = cv2.cvtColor(img1.copy(), cv2.COLOR_BGR2HSV)
	deteccion=0
	
	mask = cv2.inRange(frame, globales.obstaculoBajo, globales.obstaculoAlto)
	_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	if len(contornos)>0:
		for c in contornos:
			nuevoContorno = cv2.convexHull(c)
			rect = cv2.minAreaRect(nuevoContorno)
			box = cv2.boxPoints(rect)
			box = np.int0(box)
			area = cv2.contourArea(box)
			if area > globales.area_objeto[0] and area < globales.area_objeto[1]:
				img1=cv2.fillPoly(img1.copy(), pts =[box], color=(0,0,0))

	return img1

#Construccion de obstaculos para clasificador
def const_obs_cla():
	globales.pt_obs_cla_x=[]
	globales.pt_obs_cla_y=[]
	for i in range(len(globales.pt_obs_x)):
		globales.pt_obs_cla_x.append(globales.pt_obs_x[i])
		globales.pt_obs_cla_y.append(globales.pt_obs_y[i])
	pxx=[]
	pyy=[]
	if globales.n_omni_cla==1:
		if globales.st_omni2==1:
			pxx.append(globales.pts_px_omni_2[0])
			pyy.append(globales.pts_px_omni_2[1])
			pxx.append(globales.pts_px_omni_2[0]-27)
			pyy.append(globales.pts_px_omni_2[1]-27)
			pxx.append(globales.pts_px_omni_2[0])
			pyy.append(globales.pts_px_omni_2[1]-27)
			pxx.append(globales.pts_px_omni_2[0]+27)
			pyy.append(globales.pts_px_omni_2[1]-27)
			pxx.append(globales.pts_px_omni_2[0]-27)
			pyy.append(globales.pts_px_omni_2[1])
			pxx.append(globales.pts_px_omni_2[0]+27)
			pyy.append(globales.pts_px_omni_2[1])
			pxx.append(globales.pts_px_omni_2[0]-27)
			pyy.append(globales.pts_px_omni_2[1]+27)
			pxx.append(globales.pts_px_omni_2[0])
			pyy.append(globales.pts_px_omni_2[1]+27)
			pxx.append(globales.pts_px_omni_2[0]+27)
			pyy.append(globales.pts_px_omni_2[1]+27)
		if globales.st_omni3==1:
			pxx.append(globales.pts_px_omni_3[0])
			pyy.append(globales.pts_px_omni_3[1])
			pxx.append(globales.pts_px_omni_3[0]-27)
			pyy.append(globales.pts_px_omni_3[1]-27)
			pxx.append(globales.pts_px_omni_3[0])
			pyy.append(globales.pts_px_omni_3[1]-27)
			pxx.append(globales.pts_px_omni_3[0]+27)
			pyy.append(globales.pts_px_omni_3[1]-27)
			pxx.append(globales.pts_px_omni_3[0]-27)
			pyy.append(globales.pts_px_omni_3[1])
			pxx.append(globales.pts_px_omni_3[0]+27)
			pyy.append(globales.pts_px_omni_3[1])
			pxx.append(globales.pts_px_omni_3[0]-27)
			pyy.append(globales.pts_px_omni_3[1]+27)
			pxx.append(globales.pts_px_omni_3[0])
			pyy.append(globales.pts_px_omni_3[1]+27)
			pxx.append(globales.pts_px_omni_3[0]+27)
			pyy.append(globales.pts_px_omni_3[1]+27)
	elif globales.n_omni_cla==2:
		if globales.st_omni1==1:
			pxx.append(globales.pts_px_omni_1[0])
			pyy.append(globales.pts_px_omni_1[1])
			pxx.append(globales.pts_px_omni_1[0]-27)
			pyy.append(globales.pts_px_omni_1[1]-27)
			pxx.append(globales.pts_px_omni_1[0])
			pyy.append(globales.pts_px_omni_1[1]-27)
			pxx.append(globales.pts_px_omni_1[0]+27)
			pyy.append(globales.pts_px_omni_1[1]-27)
			pxx.append(globales.pts_px_omni_1[0]-27)
			pyy.append(globales.pts_px_omni_1[1])
			pxx.append(globales.pts_px_omni_1[0]+27)
			pyy.append(globales.pts_px_omni_1[1])
			pxx.append(globales.pts_px_omni_1[0]-27)
			pyy.append(globales.pts_px_omni_1[1]+27)
			pxx.append(globales.pts_px_omni_1[0])
			pyy.append(globales.pts_px_omni_1[1]+27)
			pxx.append(globales.pts_px_omni_1[0]+27)
			pyy.append(globales.pts_px_omni_1[1]+27)
		if globales.st_omni3==1:
			pxx.append(globales.pts_px_omni_3[0])
			pyy.append(globales.pts_px_omni_3[1])
			pxx.append(globales.pts_px_omni_3[0]-27)
			pyy.append(globales.pts_px_omni_3[1]-27)
			pxx.append(globales.pts_px_omni_3[0])
			pyy.append(globales.pts_px_omni_3[1]-27)
			pxx.append(globales.pts_px_omni_3[0]+27)
			pyy.append(globales.pts_px_omni_3[1]-27)
			pxx.append(globales.pts_px_omni_3[0]-27)
			pyy.append(globales.pts_px_omni_3[1])
			pxx.append(globales.pts_px_omni_3[0]+27)
			pyy.append(globales.pts_px_omni_3[1])
			pxx.append(globales.pts_px_omni_3[0]-27)
			pyy.append(globales.pts_px_omni_3[1]+27)
			pxx.append(globales.pts_px_omni_3[0])
			pyy.append(globales.pts_px_omni_3[1]+27)
			pxx.append(globales.pts_px_omni_3[0]+27)
			pyy.append(globales.pts_px_omni_3[1]+27)
	elif globales.n_omni_cla==3:
		if globales.st_omni1==1:
			pxx.append(globales.pts_px_omni_1[0])
			pyy.append(globales.pts_px_omni_1[1])
			pxx.append(globales.pts_px_omni_1[0]-27)
			pyy.append(globales.pts_px_omni_1[1]-27)
			pxx.append(globales.pts_px_omni_1[0])
			pyy.append(globales.pts_px_omni_1[1]-27)
			pxx.append(globales.pts_px_omni_1[0]+27)
			pyy.append(globales.pts_px_omni_1[1]-27)
			pxx.append(globales.pts_px_omni_1[0]-27)
			pyy.append(globales.pts_px_omni_1[1])
			pxx.append(globales.pts_px_omni_1[0]+27)
			pyy.append(globales.pts_px_omni_1[1])
			pxx.append(globales.pts_px_omni_1[0]-27)
			pyy.append(globales.pts_px_omni_1[1]+27)
			pxx.append(globales.pts_px_omni_1[0])
			pyy.append(globales.pts_px_omni_1[1]+27)
			pxx.append(globales.pts_px_omni_1[0]+27)
			pyy.append(globales.pts_px_omni_1[1]+27)
		if globales.st_omni2==1:
			pxx.append(globales.pts_px_omni_2[0])
			pyy.append(globales.pts_px_omni_2[1])
			pxx.append(globales.pts_px_omni_2[0]-27)
			pyy.append(globales.pts_px_omni_2[1]-27)
			pxx.append(globales.pts_px_omni_2[0])
			pyy.append(globales.pts_px_omni_2[1]-27)
			pxx.append(globales.pts_px_omni_2[0]+27)
			pyy.append(globales.pts_px_omni_2[1]-27)
			pxx.append(globales.pts_px_omni_2[0]-27)
			pyy.append(globales.pts_px_omni_2[1])
			pxx.append(globales.pts_px_omni_2[0]+27)
			pyy.append(globales.pts_px_omni_2[1])
			pxx.append(globales.pts_px_omni_2[0]-27)
			pyy.append(globales.pts_px_omni_2[1]+27)
			pxx.append(globales.pts_px_omni_2[0])
			pyy.append(globales.pts_px_omni_2[1]+27)
			pxx.append(globales.pts_px_omni_2[0]+27)
			pyy.append(globales.pts_px_omni_2[1]+27)
	globales.cuad_clasificador_obj=[]
	for i in range(len(pxx)):
		aux_selec=Buscar_pt_cuadricula(pxx[i],pyy[i],globales.cuad_grid_obs)
		if len(aux_selec)>0:
			if not (aux_selec[2] in globales.cuad_obs):
				globales.cuad_clasificador_obj.append(aux_selec[2])
				pts=CalcularXYZ(aux_selec[0],aux_selec[1])
				globales.pt_obs_cla_x.append(int(pts[0]))
				globales.pt_obs_cla_y.append(int(pts[1][0]))
	for i in range(len(globales.obj_rojo_real)):
		globales.pt_obs_cla_x.append(globales.obj_rojo_real[i][0])
		globales.pt_obs_cla_y.append(globales.obj_rojo_real[i][1])
	for i in range(len(globales.obj_azul_real)):
		globales.pt_obs_cla_x.append(globales.obj_azul_real[i][0])
		globales.pt_obs_cla_y.append(globales.obj_azul_real[i][1])
	for i in range(len(globales.obj_celeste_real)):
		globales.pt_obs_cla_x.append(globales.obj_celeste_real[i][0])
		globales.pt_obs_cla_y.append(globales.obj_celeste_real[i][1])


#detectar objetos automatico
def detectar_objetos(img):
	img1=img.copy()
	img2=img.copy()
	#deteccion=0
	#DETECTAR OBSTACULOS 
	
	img1=cv2.circle(img1.copy(), (globales.pts_px_omni_1[0],globales.pts_px_omni_1[1]), 60, (255,255,255), -1)
	img1=cv2.circle(img1.copy(), (globales.pts_px_omni_2[0],globales.pts_px_omni_2[1]), 60, (255,255,255), -1)
	img1=cv2.circle(img1.copy(), (globales.pts_px_omni_3[0],globales.pts_px_omni_3[1]), 60, (255,255,255), -1)
	frame = cv2.cvtColor(img1.copy(), cv2.COLOR_BGR2HSV)
	
	mask1 = cv2.inRange(frame, globales.rojoBajo1, globales.rojoAlto1)
	mask2 = cv2.inRange(frame, globales.rojoBajo2, globales.rojoAlto2)
	mask = cv2.add(mask1, mask2)	
	_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	if len(contornos)>0:
		for c in contornos:
			nuevoContorno = cv2.convexHull(c)
			rect = cv2.minAreaRect(nuevoContorno)
			box = cv2.boxPoints(rect)
			box = np.int0(box)
			area = cv2.contourArea(box)
			if area > globales.area_obj_cla[0] and area < globales.area_obj_cla[1]:
				#deteccion+=1
				M = cv2.moments(nuevoContorno)
				if (M["m00"]==0): M["m00"]=1
				x = int(M["m10"]/M["m00"])
				y = int(M['m01']/M['m00'])
				#img2=cv2.circle(img2.copy(), (x,y), 10, (0,0,255), -1)
				globales.point_obj_rojo.append([x,y])
		
				pts=CalcularXYZ(x,y)
				globales.obj_rojo_real.append([int(pts[0]),int(pts[1][0])])
	mask = cv2.inRange(frame, globales.azulBajo1, globales.azulAlto1)
	_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	if len(contornos)>0:
		for c in contornos:
			nuevoContorno = cv2.convexHull(c)
			rect = cv2.minAreaRect(nuevoContorno)
			box = cv2.boxPoints(rect)
			box = np.int0(box)
			area = cv2.contourArea(box)
			if area > globales.area_obj_cla[0]-30 and area < globales.area_obj_cla[1]:
				#deteccion+=1
				M = cv2.moments(nuevoContorno)
				if (M["m00"]==0): M["m00"]=1
				x = int(M["m10"]/M["m00"])
				y = int(M['m01']/M['m00'])
				#img2=cv2.circle(img2.copy(), (x,y), 10, (255,0,0), -1)
				globales.point_obj_azul.append([x,y])
		
				pts=CalcularXYZ(x,y)
				globales.obj_azul_real.append([int(pts[0]),int(pts[1][0])])
	mask = cv2.inRange(frame, globales.celesteBajo, globales.celesteAlto)
	_,contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	if len(contornos)>0:
		for c in contornos:
			nuevoContorno = cv2.convexHull(c)
			rect = cv2.minAreaRect(nuevoContorno)
			box = cv2.boxPoints(rect)
			box = np.int0(box)
			area = cv2.contourArea(box)
			if area > globales.area_obj_cla[0]-30 and area < globales.area_obj_cla[1]:
				#deteccion+=1
				M = cv2.moments(nuevoContorno)
				if (M["m00"]==0): M["m00"]=1
				x = int(M["m10"]/M["m00"])
				y = int(M['m01']/M['m00'])
				#img2=cv2.circle(img2.copy(), (x,y), 10, (228,170,0), -1)
				globales.point_obj_celeste.append([x,y])

				pts=CalcularXYZ(x,y)
				globales.obj_celeste_real.append([int(pts[0]),int(pts[1][0])])
	
	print(globales.obj_rojo_real)
	print(globales.obj_azul_real)
	print(globales.obj_celeste_real)

def dibjar_objetos_detectados(imag):
	img=imag.copy()
	for i in range(len(globales.point_obj_rojo)):
		img=cv2.circle(img.copy(),(globales.point_obj_rojo[i][0],globales.point_obj_rojo[i][1]),10,(0,0,255),-1)
		

	for i in range(len(globales.point_obj_azul)):
		img=cv2.circle(img.copy(),(globales.point_obj_azul[i][0],globales.point_obj_azul[i][1]),10,(255,0,0),-1)
		
	for i in range(len(globales.point_obj_celeste)):
		img=cv2.circle(img.copy(),(globales.point_obj_celeste[i][0],globales.point_obj_celeste[i][1]),10,(228,170,0),-1)
		
	aux_dt=int((globales.capInf-globales.capSu)/3)
	img=cv2.rectangle(img.copy(), (globales.capDe-50,globales.capSu), (globales.capDe,globales.capSu+aux_dt), (0,0,255), -1)
	#font = cv2.FONT_HERSHEY_SIMPLEX
	#img=cv2.putText(img.copy(), 'Deposito Rojo',(int(globales.DepoRojoX[0]-100),int(globales.DepoRojoY[0]-10)), font, 0.55,(0,0,255),1,cv2.LINE_AA)
	aux1_dt=int(globales.capSu+aux_dt)
	img=cv2.rectangle(img.copy(), (globales.capDe-50,aux1_dt), (globales.capDe,int(globales.capSu+2*aux_dt)), (255,0,0), -1)
	#font = cv2.FONT_HERSHEY_SIMPLEX
	#img=cv2.putText(img.copy(), 'Deposito Azul',(int(globales.DepoAzulX[0]-100),int(globales.DepoAzulY[0]-10)), font, 0.55,(255,0,0),1,cv2.LINE_AA)
	aux1_dt=int(globales.capSu+2*aux_dt)
	img=cv2.rectangle(img.copy(), (globales.capDe-50,aux1_dt), (globales.capDe,int(globales.capSu+3*aux_dt)), (228,170,0), -1)
	#font = cv2.FONT_HERSHEY_SIMPLEX
	#img=cv2.putText(img.copy(), 'Deposito Celeste',(int(globales.DepoCelX[0]-100),int(globales.DepoCelY[0]-10)), font, 0.55,(228,170,0),1,cv2.LINE_AA)
	
	return img