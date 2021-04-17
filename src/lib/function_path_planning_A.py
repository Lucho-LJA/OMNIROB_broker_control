#!/usr/bin/env python3
import math

import matplotlib.pyplot as plt#!/usr/bin/env python3

import numpy as np
from config import globales




class AStarPlanner:

    def __init__(self, ox, oy, resolution, rr):
        """
        Initialize grid map for a star planning

        ox: x position list of Obstacles [m]
        oy: y position list of Obstacles [m]
        resolution: grid resolution [m]
        rr: robot radius[m]
        """

        self.resolution = resolution
        self.rr = rr
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = 0, 0
        self.obstacle_map = None
        self.x_width, self.y_width = 0, 0
        self.motion = self.get_motion_model()
        self.calc_obstacle_map(ox, oy)

    class Node:
        def __init__(self, x, y, cost, parent_index):
            self.x = x  # index of grid
            self.y = y  # index of grid
            self.cost = cost
            self.parent_index = parent_index
            #print(cost)
            #print(parent_index)

        def __str__(self):
            return str(self.x) + "," + str(self.y) + "," + str(
                self.cost) + "," + str(self.parent_index)

    def planning(self, sx, sy, gx, gy):
       

        start_node = self.Node(self.calc_xy_index(sx, self.min_x),
                               self.calc_xy_index(sy, self.min_y), 0.0, -1)
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x),
                              self.calc_xy_index(gy, self.min_y), 0.0, -1)

        open_set, closed_set = dict(), dict()
        open_set[self.calc_grid_index(start_node)] = start_node

        while 1:
            if len(open_set) == 0:
                print("Open set is empty..")
                break

            c_id = min(
                open_set,
                key=lambda o: open_set[o].cost + self.calc_heuristic(goal_node,open_set[o]))
            current = open_set[c_id]



            if current.x == goal_node.x and current.y == goal_node.y:
                print("Find goal")
                goal_node.parent_index = current.parent_index
                goal_node.cost = current.cost
                break

            # Remove the item from the open set
            del open_set[c_id]

            # Add it to the closed set
            closed_set[c_id] = current

            # expand_grid search grid based on motion model
            for i, _ in enumerate(self.motion):
                node = self.Node(current.x + self.motion[i][0],
                                 current.y + self.motion[i][1],
                                 current.cost + self.motion[i][2], c_id)
                n_id = self.calc_grid_index(node)

                # If the node is not safe, do nothing
                if not self.verify_node(node):
                    continue

                if n_id in closed_set:
                    continue

                if n_id not in open_set:
                    open_set[n_id] = node  # discovered a new node
                else:
                    if open_set[n_id].cost > node.cost:
                        # This path is the best until now. record it
                        open_set[n_id] = node

        rx, ry = self.calc_final_path(goal_node, closed_set)

        return rx, ry

    def calc_final_path(self, goal_node, closed_set):
        # generate final course
        rx, ry = [self.calc_grid_position(goal_node.x, self.min_x)], [
            self.calc_grid_position(goal_node.y, self.min_y)]
        parent_index = goal_node.parent_index
        while parent_index != -1:
            n = closed_set[parent_index]
            rx.append(self.calc_grid_position(n.x, self.min_x))
            ry.append(self.calc_grid_position(n.y, self.min_y))
            parent_index = n.parent_index

        return rx, ry

    @staticmethod
    def calc_heuristic(n1, n2):
        w = 1.0  # weight of heuristic
        d = w * math.hypot(n1.x - n2.x, n1.y - n2.y)
        return d

    def calc_grid_position(self, index, min_position):
        """
        calc grid position

        :param index:
        :param min_position:
        :return:
        """
        pos = index * self.resolution + min_position
        return pos

    def calc_xy_index(self, position, min_pos):
        return round((position - min_pos) / self.resolution)

    def calc_grid_index(self, node):
        return (node.y - self.min_y) * self.x_width + (node.x - self.min_x)

    def verify_node(self, node):
        px = self.calc_grid_position(node.x, self.min_x)
        py = self.calc_grid_position(node.y, self.min_y)

        if px < self.min_x:
            return False
        elif py < self.min_y:
            return False
        elif px >= self.max_x:
            return False
        elif py >= self.max_y:
            return False

        # collision check
        if self.obstacle_map[node.x][node.y]:
            return False

        return True

    def calc_obstacle_map(self, ox, oy):
        self.min_x = 0
        self.min_y = 0
        self.max_x = 2920
        self.max_y = 1867
        print("min_x:", self.min_x)
        print("min_y:", self.min_y)
        print("max_x:", self.max_x)
        print("max_y:", self.max_y)

        self.x_width = round((self.max_x - self.min_x) / self.resolution)
        self.y_width = round((self.max_y - self.min_y) / self.resolution)
        print("x_width:", self.x_width)
        print("y_width:", self.y_width)

        # obstacle map generation
        self.obstacle_map = [[False for _ in range(self.y_width)] for _ in range(self.x_width)]
        for ix in range(self.x_width):
            x = self.calc_grid_position(ix, self.min_x)
            for iy in range(self.y_width):
                y = self.calc_grid_position(iy, self.min_y)
                for iox, ioy in zip(ox, oy):
                    d = math.hypot(iox - x, ioy - y)
                    if d <= self.rr:
                        self.obstacle_map[ix][iy] = True
                        break

    @staticmethod
    def get_motion_model():
        # dx, dy, cost
        motion = [[1, 0, 1],
                  [0, 1, 1],
                  [-1, 0, 1],
                  [0, -1, 1],
                  [-1, -1, math.sqrt(2)],
                  [-1, 1, math.sqrt(2)],
                  [1, -1, math.sqrt(2)],
                  [1, 1, math.sqrt(2)]]

        return motion

def optimizacion(px,py):
    print(px[0],py[0])
    aux=1
    a=50
    while aux<(a-1):
        aux=0
        auxx=[]
        auxy=[]
        ang1=0
        ang2=0
        cont=0
        stop=len(px)
        for i in range(cont,stop):
            if cont<(len(px)):
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
                print(aux,ang1,ang2,len(px))
                print(cont)
        a=len(px)
        px=[]
        py=[]
        px=auxx
        py=auxy
        print(px,py)
    
    return px,py

def calcular_ruta_AS(px,py,dx,dy,ox11,oy11):

    ox1=ox11
    oy1=oy11
    # Inicializar
    sx = px/10  # start x position [cm]
    sy = py/10  # start y positon [cm]
    gx = dx/10 # goal x position [cm]
    gy = dy/10  # goal y position [cm]
    grid_size = globales.grid_tray/10  # potential grid size [cm]
    robot_radius = globales.ratio_robot/10 # robot radius [cm]

    # Setear Obstaculos
    ox, oy = [], []
    for i in range(0, 292):
    #for i in range(0, int(globales.pt_max_x/10)):
        ox.append(i)
        oy.append(0)
    for i in range(0, 186):
    #for i in range(0, int(globales.pt_max_y/10)):
        #ox.append(int(globales.pt_max_x/10))
        ox.append(292)
        oy.append(i)
    for i in range(0, 292):
    #for i in range(0, int(globales.pt_max_x/10)):
        ox.append(i)
        #oy.append(int(globales.pt_max_y/10))
        oy.append(186)
    for i in range(0, 186):
    #for i in range(0, int(globales.pt_max_y/10)):
        ox.append(0)
        oy.append(i)

    for i in range(len(ox1)):
        ox1[i]=int(ox1[i]/10)
        oy1[i]=int(oy1[i]/10)

    #ox1 = [100,100,100,100,100,100,100,100]   # obstacle x position list [m]
    #oy1 = [15,30,45,60,75,90,105,120]  # obstacle y position list [m]

    for i in range(len(ox1)):
        ox.append(ox1[i])
        oy.append(oy1[i])



    a_star = AStarPlanner(ox, oy, grid_size, robot_radius)

    rx, ry = a_star.planning(sx, sy, gx, gy)
    
    rx.reverse()
    ry.reverse()
    rx.append(gx)
    ry.append(gy)
    print('trayectoria_previa')
    print(rx)
    print(ry)
    print('---')
    pfx,pfy=optimizacion(rx,ry)
    for i in range(len(pfx)):
        pfx[i]=int(pfx[i]*10)
        pfy[i]=int(pfy[i]*10)
    #print(px,py)
    #pfx.pop(-2)
    #pfy.pop(-2)
    print('trayectoria')
    print(pfx)
    print(pfy)
    print('---')
    return pfx,pfy
