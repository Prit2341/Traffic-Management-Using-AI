import pandas as pd
import matplotlib.pyplot as plt

columns = ['Static', 'Dynamic']
x = []
y = []
df = pd.read_csv("chart.csv", usecols=columns)
df.plot()
plt.plot(x, y, marker='s')
plt.xlabel('Simulation Attempts')
plt.ylabel('No. of Vehicles passed per 1 Simulation')
plt.title('Comparison: Current Static System vs Our Dynamic System', fontsize=15)
plt.grid()
plt.show()