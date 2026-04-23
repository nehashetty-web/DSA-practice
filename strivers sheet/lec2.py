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