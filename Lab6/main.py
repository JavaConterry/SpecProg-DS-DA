import numpy as np
import matplotlib.pyplot as plt
from data_generator import create_set_near_lin_func


x, y = create_set_near_lin_func(8, 500)

def part1():
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


def part2():
    def clip_gradients(gradient, threshold):
        if gradient > threshold:
            return threshold
        elif gradient < -threshold:
            return -threshold
        else:
            return gradient

    def MSE(x, y):
        b0, b1, learning_rate = 1, 1, 0.0001
        iterations = 1000
        dLdb0, dLdb1 = 0, 0
        y_h = []

        i = 0
        while not (np.isnan(dLdb0) or np.isnan(dLdb1) or i >= len(x)):
            y_h.append(b0 + b1 * x[i])
            dy = y[i] - y_h[i]
            dLdb0 += -2 * dy
            dLdb1 += -2 * x[i] * dy

            # gradient clipping for 
            dLdb0 = clip_gradients(dLdb0, gradient_clip_threshold)
            dLdb1 = clip_gradients(dLdb1, gradient_clip_threshold)

            b0 = b0 - learning_rate * dLdb0
            b1 = b1 - learning_rate * dLdb1

            i += 1

        return b1, b0

    # gradient clip threshold to overcome the error of "overflow encountered in double_scalars"
    gradient_clip_threshold = 1e3

    b1, b0 = MSE(x, y)

    fig, ax = plt.subplots()
    ax.scatter(x, y, label="Generated Data")
    line1, = ax.plot(x, [b1 * xi + b0 for xi in x], label="MSE linear regr", color='orange')
    plt.legend()
    plt.show()







part1()
part2()