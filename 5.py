import math


def main(x, z):
    n = len(x)
    y = [0]
    z = y + z
    x = y + x
    res = 0
    for i in range(1,n+1):
        res += 91*(math.fabs(z[n+1-i]**2-x[math.ceil(i/4)]**3))**6
    return 30*res
    
print(main([-0.96, 0.7, 0.04, 0.98, -0.34],
[-0.73, 0.3, 0.82, 0.21, 0.44]))
print(main([0.26, 0.34, 0.54, 0.28, -0.88],
[-0.55, 0.03, 0.62, 0.75, -0.65]))