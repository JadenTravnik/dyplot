import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt



class dynamic_3d_plotter():
    cube = 	  np.array([[1, -1, -1 ],
				  [1, 1, -1],
				  [-1, 1, -1],
				  [-1, -1, 1],
				  [1, -1, 1 ],
				  [1, 1, 1],
				  [-1, 1, 1]])
    def __init__(self, lims):
        self.lims = lims
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        plt.ion()
        plt.show()        

    def update(self, points):

        plt.cla()
        self.ax.set_xlim(self.lims[0], self.lims[1])
        self.ax.set_ylim(self.lims[2], self.lims[3])
        self.ax.set_zlim(self.lims[4], self.lims[5])
        Z = points

        r = [-1,1]

        X, Y = np.meshgrid(r, r)
        # plot vertices
        self.ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])

        # list of sides' polygons of figure
        verts = [[Z[0],Z[1],Z[2],Z[3]],
        [Z[4],Z[5],Z[6],Z[7]], 
        [Z[0],Z[1],Z[5],Z[4]], 
        [Z[2],Z[3],Z[7],Z[6]], 
        [Z[1],Z[2],Z[6],Z[5]],
        [Z[4],Z[7],Z[3],Z[0]], 
        [Z[2],Z[3],Z[7],Z[6]]]

        # plot sides
        self.ax.add_collection3d(Poly3DCollection(verts, 
        facecolors='#008800', linewidths=1, edgecolors='black', alpha=.65))
        
        
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()



'''
Sample Usage

import time

lims = [-5, 5, -5, 5, -5, 5]

d3 = dynamic_3d_plotter(lims)

points = np.array([[-1, -1, -1],
                  [1, -1, -1 ],
                  [1, 1, -1],
                  [-1, 1, -1],
                  [-1, -1, 1],
                  [1, -1, 1 ],
                  [1, 1, 1],
                  [-1, 1, 1]])


for i in np.arange(0, np.pi*4, np.pi*.1):
    theta, phi, psi = i, 1.4*i, .2*i
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(phi), np.sin(phi)],
        [0, -np.sin(phi), np.cos(phi)]
    ])
    Ry = np.array([
        [np.cos(theta), 0, -np.sin(theta)],
        [0, 1, 0],
        [np.sin(theta), 0, np.cos(theta)]
    ])
    Rz = np.array([
        [np.cos(psi), np.sin(psi), 0],
        [-np.sin(psi), np.cos(psi), 0],
        [0, 0, 1]
    ])
    R = np.matmul(np.matmul(Rz, Ry), Rx)

    d3.update(np.matmul(points,R))

    time.sleep(.1)

'''