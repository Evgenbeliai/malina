import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('GoogleApps.csv') 
# plot() - метод построение диаграммы

# s = pd.Series(index = [1,2, 3, 4, 5,6, 7], data = [-3,-2, 0, 0, -4, -5, -4])
# s.plot()
# plt.show()

# df["Size"].plot(kind = "hist") # - Гистограмма
#df[df['Type'] == 'Paid']['Price'].plot(kind = 'box') # Ящик с усами
#df.plot(x = 'Installs', y = 'Rating', kind = 'scatter')
df['Content Rating'].value_counts().plot(kind = 'pie')
plt.show()