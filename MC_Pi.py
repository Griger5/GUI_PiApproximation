from random import uniform

def piApproximation(num):
    inside = 0

    for _ in range(num):
        x = uniform(-1, 1)
        y = uniform(-1, 1)

        if x**2+y**2 < 1:
            inside += 1

    return 4*inside/num

if __name__ == "__main__":
    print(piApproximation(10**6))
