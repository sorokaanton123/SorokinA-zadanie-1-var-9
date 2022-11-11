import matplotlib.pyplot as plt
import numpy as np
import json
import os


x = np.linspace(-10, 10, 500)
A = 0
y = 0.5+((np.sin(x**2 - A**2))**2 - 0.5)/(1 + 0.001*(x**2 + A**2))

plt.axis([-10, 10, 0, 2])
plt.plot(x, y)

if 'results' not in os.listdir():
    os.makedirs(os.path.join(os.getcwd(), 'results'))

with open("results/results.json", "w", encoding="utf-8") as file:
    di = {'x': [x[i] for i in range(len(x))],
          'y': [y[i] for i in range(len(y))]}
    json.dump(di, file, sort_keys=True, indent=4)

plt.show()
