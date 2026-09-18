def print_num(n):
    if n == 0:
        return
    print(n)
    print_num(n - 1)

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

def fib(n):
    if n<=1:
        return -1
    return fib(n-1)+fib(n-2)

def reverse(s):
    if len(s)==0:
        return " "
    return reverse(s[1:])+s(0)cx