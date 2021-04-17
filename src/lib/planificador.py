#!/usr/bin/env python3
import numpy as np

def distancia_plan(robs,r,b,c,l_r,l_b,l_c):#Funcion encargada de hallar la distancia entre los objetos y los robots
	dist_c=[]#Vector de distancias de los robots con los objetos celestes
	dist_b=[]#Vector de distancias de los robots con los objetos azules
	dist_r=[]#Vector de distancias de los robots con los objetos rojos
	cod_r=[]#Indica el orden de los omnidireccionales al permutar con los puntos rojos
	cod_r1=[]#Indica el orden de los puntos rojos
	cod_b=[]#Indica el orden de los omnidireccionales al permutar con los puntos azules
	cod_b1=[]#Indica el orden de los puntos azules
	cod_c=[]#Indica el orden de los omnidireccionales al permutar con los puntos celestes
	cod_c1=[]#Indica el orden de los puntos celestes
	cont=0
	aux=0
	aux2=0
	a=[1,2,3]
	a1=[]
	for i in range(l_r+l_b+l_c):
		a1.append(i+1)
	for i in robs:
		for j in r:
			dist_r.append((np.hypot(j[0] - i[0], j[1] - i[1])))
			cod_r.append(a[aux])
			cont+=1
			cod_r1.append(a1[aux2])
			aux2+=1
			if cont==l_r:
				cont=0
				aux2=0
				aux+=1
	#print(cod_r)
	#print(cod_r1)
	cont=0
	aux=0
	aux2=l_r
	for i in robs:
		for j in b:
			dist_b.append((np.hypot(j[0] - i[0], j[1] - i[1])))
			cod_b.append(a[aux])
			cont+=1
			cod_b1.append(a1[aux2])
			aux2+=1
			if cont==l_b:
				cont=0
				aux+=1
				aux2=l_r
	#print(cod_b)
	#print(cod_b1)
	cont=0
	aux=0
	aux2=l_r+l_b
	for i in robs:
		for j in c:
			dist_c.append((np.hypot(j[0] - i[0], j[1] - i[1])))
			cod_c.append(a[aux])
			cont+=1
			cod_c1.append(a1[aux2])
			aux2+=1
			if cont==l_c:
				cont=0
				aux+=1
				aux2=l_r+l_b
	#print(cod_c)
	#print(cod_c1)
	cod_total=cod_r+cod_b+cod_c
	cod_total1=cod_r1+cod_b1+cod_c1
	#print(cod_total)
	#print(cod_total1)
	return(dist_r,dist_b,dist_c,cod_total,cod_total1)

def distancias_minimas_plan(rojos,azules,celestes,cod_total,l_rob,cod_total1):
	#print(cod_total)
	dist_total=rojos+azules+celestes
	#print(dist_total)
	min_1=[]
	pos_1=[]
	aux1=[]
	aux3=[]
	for i in range(l_rob):
		min_1.append(min(dist_total))
		pos_1.append(dist_total.index(min_1[i]))
		aux1.append(cod_total[pos_1[i]])
		aux3.append(cod_total1[pos_1[i]])
		#print(aux1,aux3)
		eliminar=[j for j,x in enumerate(cod_total) if x==aux1[i]]
		#print(eliminar)
		for k in eliminar:
			dist_total[k]=100
		eliminar1=[m for m,y in enumerate(cod_total1) if y==aux3[i]]
		#print(eliminar1)
		for l in eliminar1:
			dist_total[l]=100
		#print(dist_total)
	#print(min_1,pos_1,aux1)

	return(min_1,aux1,pos_1)


def ruta_corta_plan(robots_omni, obj_rojo, obj_azul, obj_celeste):

	"""for i in range(len(robots_omni)):
		robots_omni[i][0]=robots_omni[i][0]/1000
		robots_omni[i][1]=robots_omni[i][1]/1000
	for i in range(len(obj_rojo)):
		obj_rojo[i][0]=obj_rojo[i][0]/1000
		obj_rojo[i][1]=obj_rojo[i][1]/1000
	for i in range(len(obj_azul)):
		obj_azul[i][0]=obj_azul[i][0]/1000
		obj_azul[i][1]=obj_azul[i][1]/1000
	for i in range(len(obj_celeste)):
		obj_celeste[i][0]=obj_celeste[i][0]/1000
		obj_celeste[i][1]=obj_celeste[i][1]/1000"""
	

	#robots_omni=[[0.5,1.0],[3.0,2.0],[1.0,2.0]]#Se define los vectores de entrada de las posiciones de los robots en robots_omni
	#obj_rojo=[[1.5,4.0],[2.0,3.0],[2.1,3.1]]#Se define la ubicacion de los objetos a clasificar rojo en obj_rojo
	#obj_azul=[[2.5,3.0],[5.0,6.0]]#Se define la ubicacion de los objetos a clasificar azul en obj_azul
	#obj_celeste=[]#Se define la ubicacion de los objetos a clasificar celestes en obj_celeste
	#Obtengo 3 vectores de distancias de objetos rojos , azules , celestes
	color=0
	l_r=len(obj_rojo)
	l_b=len(obj_azul)
	l_c=len(obj_celeste)
	l_rob=len(robots_omni)
	disr,disb,disc,cod_total,cod_total1=distancia_plan(robots_omni,obj_rojo,obj_azul,obj_celeste,l_r,l_b,l_c)
	#print(disr,disb,disc)
	#print(cod_total)
	d_min,robot,pos=distancias_minimas_plan(disr,disb,disc,cod_total,l_rob,cod_total1)
	
	#puntos,omni=convertir_coordenadas(obj_rojo,obj_azul,obj_celeste,d_min,robot,robots_omni)
	obj_total=(obj_rojo*len(robots_omni))+(obj_azul*len(robots_omni))+(obj_celeste*len(robots_omni))
	puntos_finales=[]
	for i in pos:
		puntos_finales.append(obj_total[i])
	#print(obj_total)
	#print(d_min,robot,pos)

	for i in range(len(obj_rojo)):
		if obj_rojo[i]==puntos_finales[0]:
			obj_rojo.pop(i)
			color=1
			cont_elim=i
			break
	for i in range(len(obj_azul)):
		if obj_azul[i]==puntos_finales[0]:
			obj_azul.pop(i)
			color=2
			cont_elim=i
			break
	for i in range(len(obj_celeste)):
		if obj_celeste[i]==puntos_finales[0]:
			obj_celeste.pop(i)
			color=3
			cont_elim=i
			break

	return puntos_finales[0][0],puntos_finales[0][1],color, robot[0], obj_rojo, obj_azul, obj_celeste, cont_elim

