import numpy as np
import matplotlib.pyplot as plt


class DynamicScatter():

	def __init__(self, x, y, s=1, c='black'):
		plt.ion()
		self.figure, self.ax = plt.subplots()
		self.sc = self.ax.scatter(x, y, s=s, c=c)
		print('init')
		

	def update(self, data):
		print('update')
		self.sc.set_offsets(data)
		self.figure.canvas.draw()
		self.figure.canvas.flush_events()


'''
x = np.random.random(10)
y = np.random.random(10)

import time
ds = DynamicScatter(x, y)

for i in range(1000):
	time.sleep(.01)
	x += np.random.random(10)*.01 - .005
	y += np.random.random(10)*.01 - .005
	
	ds.update(np.hstack((x, y)))
'''
	
