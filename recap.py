stack=[]
s="datastruct"

for ch in s:
    stack.append(ch)

reversedstring=" "

while stack:
    reversedstring += stack.pop()

print(reversedstring)
'''Stack – Coding Questions
Implement a stack using a Python list with push, pop, peek, and is_empty.
Reverse a string using a stack.
Check whether a given string has balanced parentheses using a stack.
Evaluate a postfix expression using a stack.
Implement a stack using two queues.
Queue – Coding Questions
Implement a queue using a Python list with enqueue, dequeue, peek, and is_empty.
Implement a queue using collections.deque.
Reverse a queue.
Implement a circular queue.
Implement a queue using two stacks.'''
