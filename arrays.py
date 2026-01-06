'''ARRAY QUESTIONS
Write a Python program to create an array and print all its elements.
Write a program to find the sum of all elements in an array.
Write a program to search for a given number in an array.
Write a program to update an element at a given index in an array.
Write a program to count how many elements are present in an array.'''

"solutions"
A=[10,20,34,89]
for x in A:
    print(x)

A = [10, 20, 34, 89]
total = 0
for x in A:
    total = total + x
print(total)

A=[12,23,45,67]
if 12 in A:
 print("present")
else:
  print("absent")
   
A.append(87)
print(A)
A[0]=32
print(A)


print(len(A))