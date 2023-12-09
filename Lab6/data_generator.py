import numpy as np

def create_set_near_lin_func(k, b): #function coefitients f(x)=kx+b
    x = np.linspace(0, 100, 1000)
    print(x.shape) #mean = 0
    y = k*x+b + np.random.normal(0, 100, 1000) 
    return x, y
