n=int(input("enter a number"))
count=0
while n>0:
    count+=1
    n//=10
print(count)

n = int(input("Enter number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print("Reversed:", rev)
n = int(input("Enter number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print("Reversed:", rev)

n=int(input("enter n:"))
count=0
if n==0:
    count=0
else: 
    while n >0:
       count+=1
       n//=10
print(count)
s=input("enter string:")
rev=s[::-1]
if rev==s:
    print("is planidrome")
else:
    print("not palindrome")

a=int(input("enter num1:"))
b=int(input("enter num2:"))
while b!=0:
    a,b=b,a%b
print("GCD",a)

n = int(input("enter n: "))

for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")

n = int(input("Enter number: "))

if n <= 1:
    print("Not Prime")
else:
    is_prime = True
    
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

def f(n):
    if n == 0:
        return
    print("Hello")
    f(n-1)

f(5)

def f(n):
    if n==0:
        return
    print("welcome")
    f(n-1)
f(8)

def f(i,n):
    if i>n:
        return
    print(i)
    f(i+1,n)
f(1,99)

def f(n):
    if n==0:
        return
    print(n)
    f(n-1)

f(8)

def sum_n(n):
    if n==0:
        return 0
    return(n+sum_n(n-1))
print(sum_n(8))

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(5))

a=[1,2,4,5,6]
print(a[::-1])

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(8))