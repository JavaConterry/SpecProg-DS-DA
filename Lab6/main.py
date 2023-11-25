import numpy as np
import matplotlib.pyplot as plt
from data_generator import create_set_near_lin_func


x, y = create_set_near_lin_func(8, 500)

y_h = np.mean(y)
x_h = np.mean(x)

def MLS(x, y, x_h, y_h): #Method of Least Squeres
    enum_sum = 0
    denum_sum = 0
    for i in range(len(x)):
        dx = x[i]-x_h
        enum_sum+=dx*(y[i]-y_h)
        denum_sum+=dx*dx
    if(denum_sum!=0):
        beta1=enum_sum/denum_sum
    beta0 = y_h-beta1*x_h
    return beta1, beta0

np_y = np.polyfit(x, y, 1)
b1, b0 = MLS(x, y, x_h, y_h)
fig, ax = plt.subplots()
ax.scatter(x, y, label = "Generated Data")
line, = ax.plot(x, np_y[0]*x+np_y[1], label="numpy linear regr", color = 'green')
line2, = ax.plot(x, b1*x+b0, label="MLS linear regr", color = 'orange')
print(np_y[0]-b1)
plt.legend()
plt.show()