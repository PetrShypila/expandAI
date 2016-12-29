import sys
import numpy as np

nodes = int(sys.argv[1])

x = np.random.uniform(-100.0, 100.0, nodes)
y = np.random.uniform(0.0, 100.0, nodes)
z = np.random.uniform(-50.0, 50.0, nodes)

with open('brain_vertex_low.obj', 'w') as f:
    f.write("g brain\n")

    for n in np.arange(nodes):
        f.write("v {:.2f} {:.2f} {:.2f}\n".format(x[n], y[n], z[n]))
