import numpy as np
import matplotlib.pyplot as plt

# data
X = np.linspace(-2, 3, num=50, endpoint=True)
b = 2.0
Y = X + b
#Y = np.sin(X*np.pi*2)
# plot stuff
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
#ax.set_title('linear neuron')

# move axes
ax.spines['left'].set_position(('axes', 0.5))
# ax.spines['left'].set_smart_bounds(True)
ax.yaxis.set_ticks_position('left')
'''
ax.spines['bottom'].set_position(('axes', 0.30))
# ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
'''
ax.set_ylim(-3, 3)
ax.set_xlim(-3,3)
ax.spines['bottom'].set_position('zero')
xlabel = ax.xaxis.get_label()
lpos = xlabel.get_position()
xlabel.set_position((0, lpos[1]))

# title'
ax.set_title('Linear Neuron', y=1.10,color="red")


# axis labels
ax.xaxis.set_label_coords(1.04, 0.30 - 0.025)
ax.yaxis.set_label_coords(0.30 - 0.03, 1.04)
y_label = ax.set_ylabel('output')
y_label.set_rotation(20)
ax.set_xlabel('input')

ax.get_xaxis().set_visible(True)
ax.get_yaxis().set_visible(True)

# grid
ax.grid(True)

ax.plot(X, Y, '-.', linewidth=1.5)

fig.tight_layout()

plt.show()
