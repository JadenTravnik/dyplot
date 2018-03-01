import numpy as np
import matplotlib.pyplot as plt


class DynamicTree():

	def __init__(self):
		plt.ion()

		self.layers = [0]

		self.figure, self.ax = plt.subplots()
		self.ax.set_xlim([-1, 11])
		self.ax.set_ylim([-1, 11])
		self.sc = self.ax.scatter([0], [0])
		self.connections = {}
		self.nodes = {}


		self.x = []
		self.y = []
		self.lines = []

	def addlayer(self):
		self.layers.append(0)

	def addpoint(self, layerID, pid):
		self.layers[layerID] += 1
		self.nodes[pid] = (layerID, self.layers[layerID])
		self.x.append(layerID)
		self.y.append(self.layers[layerID])

	def addline(self, pid1, pid2):
		if pid1 not in self.connections:
			self.connections[pid1] = []

		if pid2 not in self.connections[pid1]:
			self.connections[pid1].append(pid2)
			self.lines.append(list([self.nodes[pid1], self.nodes[pid2]]))

	def update(self):
		self.ax.relim()
	        self.ax.autoscale_view()
		self.sc.set_offsets(np.array([self.x, self.y]).T)
		for l in self.lines:
			self.ax.plot([l[0][0], l[1][0]], [l[0][1], l[1][1]])
		self.figure.canvas.draw()
		self.figure.canvas.flush_events()

	def randP(self):
		return np.random.choice(self.nodes.keys())
		


import time
dt = DynamicTree()

l = 0
n = 0

maxn = 10
for i in range(100):
	if n < maxn:
		dt.addpoint(l, str(l) + '-' + str(n))
		n += 1
	else:
		n = 0
		dt.addlayer()
		l += 1
		
	if l > 1:
		l1 = np.random.randint(l-1)
		n1 = np.random.randint(maxn)
		l2 = l1 + 1
		n2 = np.random.randint(dt.layers[l2])
		dt.addline(str(l1) + '-' + str(n1), str(l2) + '-' + str(n2))

	dt.update()
	time.sleep(.1)
