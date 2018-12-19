import matplotlib.pyplot as plt
import numpy as np

def graph(formula, x_range):
    x = np.array(x_range)
    #^ use x as range variable
    y = formula(x)
    #^          ^call the lambda expression with x
    #| use y as function result
    plt.plot(x,y)
    plt.show()

graph(lambda x: ((np.log(x)*10**6)/np.log(2)) + 1, range(0, 435*10**15, 10**19))

input('Press ENTER to continue')
