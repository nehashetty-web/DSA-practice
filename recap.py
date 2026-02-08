stack=[]
s="datastruct"

for ch in s:
    stack.append(ch)

reversedstring=" "

while stack:
    reversedstring += stack.pop()

print(reversedstring)
'''Stack Coding Questions
Implement a stack using a Python list with push, pop, peek, and is_empty.
Reverse a string using a stack.
Check whether a given string has balanced parentheses using a stack.
Evaluate a postfix expression using a stack.
Implement a stack using two queues.
Queue Coding Questions
Implement a queue using a Python list with enqueue, dequeue, peek, and is_empty.
Implement a queue using collections.deque.
Reverse a queue.
Implement a circular queue.
Implement a queue using two stacks.'''
"solutions"
stack=[]
stack.append(3)
stack.pop()
if stack:
  print(stack[-1])
if not stack:
    print("empty")
"--------------------------------------------------------"
s="gurucharan"
stack=[]

for ch in s:
    stack.append(ch)
reverse=""
while stack:
    reverse+=stack.pop()
print(reverse)
"-------------------------------------------------------------"
def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if top != pairs[ch]:
                return False

    return len(stack) == 0
"---------------------------------------------------------"

def evaluate_postfix(expr):
    stack = []

    for ch in expr:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a // b)

    return stack[0]

class queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def enqueue(self,x):
        self.s1.append(x)
    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            print("queue is empty")
            return
        return self.s2.pop()