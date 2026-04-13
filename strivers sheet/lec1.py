#input logic
name=input("enter your name:")
age=int(input("enter your age:"))
more=100-age
print("you will be 100 years in " ,more ,"years")
#datatypes
n=int(input("enter n"))
x=float(input("enter x"))
result=n+x
print(result)
print(type(result))
#if-else
num=int(input("enter num:"))

if num%5==0 and num%3==0:
    print("FizzBuzz")
elif num %3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")   
else:
    print(num)
# switch case (Python version)
n1 = int(input("enter number 1: "))
n2 = int(input("enter number 2: "))
operator = input("enter operation (+, -, *, /): ")

if operator == "+":
    print(n1 + n2)
elif operator == "-":
    print(n1 - n2)
elif operator == "*":
    print(n1 * n2)
elif operator == "/":
    if n2 != 0:
        print(n1 / n2)
    else:
        print("cannot divide by zero")
else:
    print("invalid operator")
#array-strings
s="programming"
count=0
for ch in s:
    if ch.isalpha()and ch not in "aeiou":
        count+=1
print(count)

