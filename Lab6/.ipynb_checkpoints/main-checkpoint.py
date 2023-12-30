import numpy as np
import matplotlib.pyplot as plt
from data_generator import create_set_near_lin_func


x, y = create_set_near_lin_func(8, 500)

y_h = np.mean(y)
x_h = np.mean(x)


def MLS(x, y, x_h, y_h):  # Method of Least Squares
    enum_sum = 0
    denum_sum = 0
    for i in range(len(x)):
        dx = x[i] - x_h
        enum_sum += dx * (y[i] - y_h)
        denum_sum += dx * dx
    if (denum_sum != 0):
        beta1 = enum_sum / denum_sum
    beta0 = y_h - beta1 * x_h
    return beta1, beta0


np_y = np.polyfit(x, y, 1)
b1, b0 = MLS(x, y, x_h, y_h)

fig, ax = plt.subplots()
ax.scatter(x, y, label="Generated Data")
line, = ax.plot(x, np_y[0] * x + np_y[1],
                label="numpy linear regr", color='green')
line2, = ax.plot(x, b1 * x + b0, label="MLS linear regr", color='orange')




def in_treshold(val, treshold):
    return abs(val) < treshold

# Gradient descent method
def GDM(x, y, num_iterations = 1000000, learning_rate_b1=0.00000001, learning_rate_b0=0.0001):
    treshold = 0.001
    learning_rate = 0.00001
    b0, b1 = 0, 0
    dLdb0, dLdb1 = 0, 0
    i = 0
    stop = False
    
    while i<num_iterations:
        y_h = b0 + b1 * x
        dy = y - y_h        
        
        dLdb0 = -2 * np.mean(dy)
        dLdb1 = -2 * np.mean(x * dy)

        diff.append(b1)
        b0 = b0 - learning_rate_b0 * dLdb0
        b1 = b1 - learning_rate_b1 * dLdb1
        
        i += 1
        if(in_treshold(dLdb1, treshold) or in_treshold(dLdb0, treshold)):
            break
        
    return b1, b0

diff = []
b1, b0 = GDM(x, y, num_iterations = 1000000)
iter_ = np.arange(0, len(diff), 1)
print("b0_F", b0, "b1_F", b1)
line3, = ax.plot(x, [b1 * xi + b0 for xi in x],
                 label="Gradient descent method", color='red')
ax.legend()
plt.show()


fig, ax = plt.subplots()
line4, = ax.plot(iter_, diff, label='Number of iterations to b1 in Gradient descent method')
ax.legend()
plt.show()