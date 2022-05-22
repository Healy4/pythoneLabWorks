def main(n):
    if n:
        res = main(n-1)
        return (res/40-res**3-1)
    else:
        return -0.46

print(main(6))