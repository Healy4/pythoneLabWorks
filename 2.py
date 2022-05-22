import math


def main(y):
    if y < 135:
        result = math.log2(69*y**2)**5-12*y**6
        return result
    elif y >= 160:
        result = 69-y**4
        return result
    else:
        result = 58*math.cos(y)**5
        result += math.log10(77*y**2+63+98*y)**7+78*y**6
        return result
