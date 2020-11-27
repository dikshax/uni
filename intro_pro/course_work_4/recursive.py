def rfunc(n):
    if n == 1:
        return 1
    else:
        return n * rfunc(n - 1)
one = rfunc(5)
print(one)