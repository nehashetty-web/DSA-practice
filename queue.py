'''Implement a Queue using a Python list with enqueue, dequeue, peek, and is_empty operations.
Implement a Queue using collections.deque and perform basic operations (enqueue, dequeue, peek).
Reverse a given Queue.
Implement a Circular Queue with enqueue and dequeue operations.
Implement a Queue using two stacks.'''
q=[]
q.append(2)
q.append(4)
print("queue",q)
front=q.pop(0)
print(q)
peek=q[0]
print(q)
front=q.pop(0)

if q:
    print("full")
else:
    print("empty")

from collections import deque

q = deque([10, 20, 30, 40])
print("Original queue:", q)

stack = []

# Step 1: Move queue elements to stack
while q:
    stack.append(q.popleft())

# Step 2: Move stack elements back to queue
while stack:
    q.append(stack.pop())

print("Reversed queue:", q)

