def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 3
    else:
        return fib(n-1) + fib(n-2)
n=int(input("enter the number:"))
print(fib(n))