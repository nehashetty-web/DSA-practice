'''STRING QUESTIONS
Write a Python program to print each character of a string on a new line.
Write a program to find the length of a string without using the len() function.
Write a program to check whether a given character is present in a string.
Write a program to count the number of vowels in a string.
Write a program to create a new string by adding a character to the end of the given string.'''
"solutions"


s="Ammaa"
if "a" in s:
    print("present")

for ch in s:
    print(ch)

count=0
for _ in s:
    count+=1
    print(count)

s = input("Enter a string: ")

for ch in s:
    if ch in "aeiouAEIOU":
        print(ch, "is a vowel")

k="nana"
k+="loveu"
print(k)