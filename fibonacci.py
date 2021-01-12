def fibonacci_generator(limit):
    fibo = [1]
    if limit <= 0:
        print('Range cannot be zero.')
    elif limit > 0:
        a, b = 0, 1
        for i in range(0, limit-1):
            fibo1 = a + b
            fibo.append(fibo1)
            a = b
            b = fibo1
        return fibo
    else:
        print("Invalid limit")


try:
    lim = int(input("Enter the range of Fibonacci series: "))
    print(fibonacci_generator(lim))
except ValueError:
    print("Invalid value range.")
