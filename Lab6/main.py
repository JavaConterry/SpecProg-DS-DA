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


def clip_gradients(gradient, threshold):
    if gradient > threshold:
        return threshold
    elif gradient < -threshold:
        return -threshold
    else:
        return gradient


def MSE(x, y, learning_rate_b0=0.1, learning_rate_b1=0.0001):
    b0, b1 = 1, 1
    dLdb0, dLdb1 = 0, 0
    i = 0
    while not (np.isnan(dLdb0) or np.isnan(dLdb1) or i >= len(x)):
        y_h = b0 + b1 * x
        dy = y - y_h
        dLdb0 = -2 * np.mean(dy)
        dLdb1 = -2 * np.mean(x * dy)

        # gradient clipping for
        dLdb0 = clip_gradients(dLdb0, gradient_clip_threshold)
        dLdb1 = clip_gradients(dLdb1, gradient_clip_threshold)
        # print("dL0", dLdb0, "dL1", dLdb1)
        b0 = b0 - learning_rate_b0 * dLdb0
        b1 = b1 - learning_rate_b1 * dLdb1

        i += 1

    return b1, b0


# gradient clip threshold to overcome the error of "overflow encountered in double_scalars"
gradient_clip_threshold = 1e3
b1, b0 = MSE(x, y)

line3, = ax.plot(x, [b1 * xi + b0 for xi in x],
                 label="MSE linear regr", color='red')
ax.legend()
plt.show()



iter_x = np.arange(0.00001, 0.1, 0.00005)
diff = []
for i in range(len(iter_x)):
    b1, b0 = MSE(x, y, learning_rate_b1 = iter_x[i])
    diff.append(np_y[0] - b1)
    print("x: ",iter_x[i],"diff: ", diff[i])

fig, ax = plt.subplots()
line4, = ax.plot(iter_x, diff, label='MSE/numpy learning rate graph')
ax.legend()
plt.show()