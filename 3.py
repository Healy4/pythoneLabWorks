import math


def main(n, a, m):
    sum = 0
    for i in range(1, m+1):
        for j in range(1, a+1):
            for k in range(1, n+1):
                sum += 73*(9*k**3-1)-math.ceil((j**2)/64+63*i**3)**2
    return sum

print(main(4, 6, 2))