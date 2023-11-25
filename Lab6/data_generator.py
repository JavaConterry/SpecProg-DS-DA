import numpy as np

def create_set_near_lin_func(k, b): #function coefitients f(x)=kx+b
    x, y = np.random.randint(100, high=5000, size=3000), np.random.randint(100, high=100000, size=3000)
    indices_to_delete = []
    def f(x):
        return k*x + b

    for i in range(len(x)):
        if abs(f(x[i]) - y[i]) > 5000:
            indices_to_delete.append(i)

    x = np.delete(x, indices_to_delete)
    y = np.delete(y, indices_to_delete)
    return x, y
