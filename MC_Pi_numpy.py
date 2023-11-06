import numpy as np

def piApproximation(num):
    x = np.random.uniform(-1, 1, num)
    y = np.random.uniform(-1, 1, num)

    radius = x**2 + y**2
    inside = radius[radius<=1]

    return 4*len(inside)/num

if __name__ == "__main__":
    print(piApproximation(10**8))
# watch out, requires a lot of RAM!
