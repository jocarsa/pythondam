import matplotlib.pyplot as plt
import numpy as np

# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, axs = plt.subplots(3, 4)

##axs[1, 1].set_title('Axis [1, 1]')

axs[0, 0].plot(x, y)
axs[0, 1].plot(x, y, 'tab:orange')
axs[0, 2].plot(x, -y, 'tab:green')
axs[0, 3].plot(x, -y, 'tab:green')

axs[1, 0].plot(x, -y, 'tab:red')
axs[1, 1].plot(x, y)
axs[1, 2].plot(x, y, 'tab:orange')
axs[1, 3].plot(x, y, 'tab:orange')

axs[2, 0].plot(x, -y, 'tab:green')
axs[2, 1].plot(x, -y, 'tab:red')
axs[2, 2].plot(x, -y, 'tab:red')
axs[2, 3].plot(x, -y, 'tab:red')



for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

    
plt.show()
