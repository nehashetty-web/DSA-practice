'''Write a program to push and pop elements in a stack using Python list.
Write a program to display all elements of a stack.
Write a program to reverse a string using stack.
Write a program to check whether a given expression has balanced parentheses.
Write a program to find the top (peek) element of a stack without removing it.
If you want, I can make it even easier, or format it exactly like exam question paper 📄😊'''
"solutio94ns"
s=[]
s.append(8)
s.append(3)
s.append(13)
s.append(3)
s.append(4)
print(s[-1])

s.pop(4)
print(s[-1])
def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in '({[':          # opening brackets
            stack.append(ch)
        else:                    # closing brackets
            if not stack:
                return False
            top = stack.pop()
            if top != pairs[ch]:
                return False

    return len(stack) == 0
