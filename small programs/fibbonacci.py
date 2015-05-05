def fib(n):
    list = [0]*(n+2)
    list[1] = 1

    for i in range(n):
        list[i+2] = list[i] + list[i+1]

    return list[n-1]

print (fib(10))
