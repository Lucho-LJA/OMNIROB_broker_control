#!/usr/bin/env python3
"""

Planificador por Campos Potenciales

author: Gabriel Guerra

"""

from collections import deque
import numpy as np
import matplotlib.pyplot as plt
from config import globales

# Parameters
KP = 0.05  # attractive potential gain
ETA = 10  # repulsive potential gain
AREA_WIDTH = 8  # potential area width [m]
# the number of previous positions used to check oscillations
OSCILLATIONS_DETECTION_LENGTH = 3

show_animation = False


def calc_potential_field(gx, gy, ox, oy, reso, rr, sx, sy):
    
    #minx = min(min(ox), sx, gx) - AREA_WIDTH / 2.0
    minx=0.3
    #miny = min(min(oy), sy, gy) - AREA_WIDTH / 2.0
    miny=0.3
    #maxx = max(max(ox), sx, gx) + AREA_WIDTH / 2.0
    maxx=globales.pt_max_x/1000-0.3
    #maxy = max(max(oy), sy, gy) + AREA_WIDTH / 2.0
    maxy=globales.pt_max_y/1000-0.3
    xw = int(round((maxx - minx) / reso))
    
    yw = int(round((maxy - miny) / reso))
    

    # calc each potential
    pmap = [[0.0 for i in range(yw)] for i in range(xw)]
    for ix in range(xw):
        x = ix * reso + minx

        for iy in range(yw):
            y = iy * reso + miny
            ug = calc_attractive_potential(x, y, gx, gy)
            uo = calc_repulsive_potential(x, y, ox, oy, rr)
            uf = ug + uo
            #print(uf)
            pmap[ix][iy] = uf

    return pmap, minx, miny


def calc_attractive_potential(x, y, gx, gy):
    
    return  0.5 * KP * np.hypot(x - gx, y - gy)


def calc_repulsive_potential(x, y, ox, oy, rr):
    # search nearest obstacle
    minid = -1
    
    dmin = float("inf")
    for i, _ in enumerate(ox):
        d = np.hypot(x - ox[i], y - oy[i])
        if dmin >= d:
            dmin = d
            minid = i


    # calc repulsive potential
    dq = np.hypot(x - ox[minid], y - oy[minid])

    if dq <= rr:
        if dq <= 0.1:
            dq = 0.1
        return 0.5 * ETA * (1.0 / dq - 1.0 / (rr)) ** 2
    else:
        return 0.0


def get_motion_model():
    # dx, dy
    motion = [[1, 0],[0, 1],[-1, 0],[0, -1],[-1, -1],[-1, 1],[1, -1],[1, 1]]

    return motion


def oscillations_detection(previous_ids, ix, iy):
    previous_ids.append((ix, iy))

    if (len(previous_ids) > OSCILLATIONS_DETECTION_LENGTH):
        previous_ids.popleft()

    # check if contains any duplicates by copying into a set
    previous_ids_set = set()
    for index in previous_ids:
        if index in previous_ids_set:
            return True
        else:
            previous_ids_set.add(index)
    return False


def potential_field_planning(sx, sy, gx, gy, ox, oy, reso, rr):

    # calc potential field
    pmap, minx, miny = calc_potential_field(gx, gy, ox, oy, reso, rr, sx, sy)

    # search path
    d = np.hypot(sx - gx, sy - gy)
    ix = round((sx - minx) / reso)
    iy = round((sy - miny) / reso)
    gix = round((gx - minx) / reso)
    giy = round((gy - miny) / reso)
    #print(ix,iy)


    rx, ry = [sx], [sy]
    motion = get_motion_model()
    previous_ids = deque()
    while d >= reso:
        minp = float("inf")
        minix, miniy = -1, -1
        for i, _ in enumerate(motion):
            inx = int(ix + motion[i][0])
            iny = int(iy + motion[i][1])
            if inx >= len(pmap) or iny >= len(pmap[0]) or inx < 0 or iny < 0:
                p = float("inf")  # outside area
                print("outside potential!")
            else:
                p = pmap[inx][iny]
            if minp > p:
                minp = p
                minix = inx
                miniy = iny
        ix = minix
        iy = miniy
        xp = ix * reso + minx
        yp = iy * reso + miny
        d = np.hypot(gx - xp, gy - yp)
        rx.append(xp)
        ry.append(yp)


        if (oscillations_detection(previous_ids, ix, iy)):
            print("Oscillation detected at ({},{})!".format(ix, iy))
            break
    return rx, ry

def optimizacion(px,py):
    aux=1
    a=50
    cont=0
    while aux<(a-1):
        aux=0
        auxx=[]
        auxy=[]
        ang1=0
        ang2=0
        
        stop=len(px)
        for i in range(cont,stop):
            if cont<len(px):
                try:
                    ang1=np.arctan((py[cont+1]-py[cont])/((px[cont+1]-px[cont])))*(180/ np.pi)
                    ang1=round(ang1,2)
                except:
                    ang1=100
                try:
                    ang2=np.arctan((py[cont+2]-py[cont])/((px[cont+2]-px[cont])))*(180/ np.pi)
                    ang2=round(ang2,2)
                except:
                    ang2=100
                if ang1==ang2:
                    auxx.append(px[cont])
                    auxy.append(py[cont])
                    cont+=2
                else:
                    auxx.append(px[cont])
                    auxy.append(py[cont])
                    cont+=1
                    aux+=1
                #print(aux,ang1,ang2,len(px))
                #print(cont)
        a=len(px)
        px=[]
        py=[]
        px=auxx
        py=auxy
        #print(px,py)

    return px,py


def draw_heatmap(data):
    data = np.array(data).T
    plt.pcolor(data, vmax=100.0, cmap=plt.cm.Blues)

def potencial(sx, sy, gx, gy, ox, oy, grid_size, robot_radius):
    gx1=gx
    gy1=gy
    avoid=100
    avoid1=100
    px1=[]
    py1=[]
    banderay=0
    banderax=0
    cont_1=0
    while avoid1!=1:
        avoid=0
        
        while avoid!=1 and cont_1<10000:
            px, py = potential_field_planning(sx, sy, gx1, gy1, ox, oy, grid_size, robot_radius)
            if (np.abs(gx1-px[-1])<0.15) and (np.abs(gy1-py[-1])<0.15):
                px.append(gx1)
                py.append(gy1)
                avoid=1
            else:
                print("Ruta no encontrada")
                cont_1=cont_1+1
                print(cont_1)
                if np.abs(sx-gx1)>np.abs(sy-gy1):
                    if gy1>0.3 and banderay!=1:
                        gy1=gy1-(2*grid_size)
                    else:
                        gy1=gy1+(2*grid_size)
                        banderay=1
                    for i in range(len(oy)):
                        if gx1==ox[i] and gy1==oy[i]:
                            gy1=gy1-(2*grid_size)
                else:
                    if gx1>0.3 and banderax!=1:
                        gx1=gx1-(2*grid_size)
                    else:
                        gx1=gx1+(2*grid_size)
                        banderax=1
                    for i in range(len(ox)):
                        if gx1==ox[i] and gy1==oy[i]:
                            gx1=gx1-(2*grid_size)

        if cont_1>=10000:
            avoid1=1
            
        else:
            if gx!=gx1 or gy!=gy1:
                px1=px
                py1=py
                sx=gx1
                sy=gy1
                gx1=gx
                gy1=gy
            else:
                avoid1=1
    if cont_1>=10000:
        return [],[]
    else:
        px=px1+px
        py=py1+py  
        return px,py



def calcular_ruta_campos(px,py,dx,dy,ox1,oy1):
    #print("potential_field_planning start")
    ox=ox1
    oy=oy1
    sx = px/1000  # start x position [m]
    sy = py/1000  # start y positon [m]
    gx = dx/1000 # goal x position [m]
    gy = dy/1000  # goal y position [m]
    grid_size = globales.grid_tray/1000  # potential grid size [m]
    robot_radius = globales.ratio_robot/1000 # robot radius [m]

    #ox = [15.0, 5.0, 20.0, 25.0]  # obstacle x position list [m]
    #oy = [25.0, 15.0, 26.0, 25.0]  # obstacle y position list [m]
    for i in range(len(ox)):
        ox[i]=ox[i]/1000
        oy[i]=oy[i]/1000

    #ox = [0.4, 1.2, 0.9,1.4,2.3,1.1,1.3]  # obstacle x position list [m]
    #oy = [0.4, 0.4, 0.4,1.5,1.6,1.3,1.1]  # obstacle y position list [m]
    
    # path generation
    px, py = potencial(sx, sy, gx, gy, ox, oy, grid_size, robot_radius)
    for i in range(len(px)):
        px[i]=round(px[i],3)
        py[i]=round(py[i],3)
    #print(px,py)
    px.append(gx)
    py.append(gy)
    pfx,pfy=optimizacion(px,py)
    for i in range(len(pfx)):
        pfx[i]=int(pfx[i]*1000)
        pfy[i]=int(pfy[i]*1000)
    #print(px,py)
    if len(pfx)>=2:
        pfx.pop(-2)
        pfy.pop(-2)
    #print(px,py)
    #pfx.pop(0)
    #pfy.pop(0)
    print('trayectoria')
    print(pfx)
    print(pfy)
    print('---')
    return pfx,pfy 
