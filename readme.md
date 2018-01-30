# Dyplot

Don't you hate that there isn't a simple realtime matplotlib extension?
Sure there is the animation part of matplotlib but what if you want to test a sensor or visualize any data in realtime?

Thus I have made this repo.
There are 2 main files:
dyplot.py
dyplot3d.py

They are independent and easy to use.

## Dyplot

Using dyplot is easy!
`
import dyplot
import time
d = dyplot.DynamicPlot(window_x = 30, title = 'Trigonometry', xlabel = 'X', ylabel= 'Y')
d.add_line('sin(x)')
d.add_line('cos(x)')
d.add_line('cos(.5*x)')

for i in np.arange(0,40, .2):
    d.update(i, [np.sin(i), np.cos(i), np.cos(i/.5)])
    time.sleep(.01)
`

## Dyplot3d

The same goes for dyplot3d!

`
import time
# define the viewer lims [xmin, xmax, ymin, ymax, zmin, zmax]
lims = [-5, 5, -5, 5, -5, 5]

d3 = dynamic_3d_plotter(lims)
update_rate = .1
# use any points that make a 3d object, here its a cube
points = np.array([[-1, -1, -1],
                  [1, -1, -1 ],
                  [1, 1, -1],
                  [-1, 1, -1],
                  [-1, -1, 1],
                  [1, -1, 1 ],
                  [1, 1, 1],
                  [-1, 1, 1]])

# using some test data we can rotate the cube
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
    
    # make a rotation matrix
    R = np.matmul(np.matmul(Rz, Ry), Rx)

    # update the plot
    d3.update(np.matmul(points,R))
    # This is to control the speed of the update
    time.sleep(update_rate)
`