stack = []

stack.append(10)   # push
stack.append(20)
stack.append(30)

print(stack.pop())  # 30
print(stack[-1])    # 20 → peek


class Queue:
    # Creates an empty queue
    def __init__(self):
        self.queue = []

    # Adds an element to the rear/end of the queue
    def enqueue(self, x):
        self.queue.append(x)

    # Removes and returns the element from the front
    def dequeue(self):
        # Check if the queue is empty
        if len(self.queue) == 0:
            return -1

        # Remove and return the first element
        return self.queue.pop(0)

    # Returns the first element without removing it
    def front(self):
        # Check if the queue is empty
        if len(self.queue) == 0:
            return -1

        # Return the first element
        return self.queue[0]


class node:
    def__init__(self,data):
    self.data=data
    self.next=None

current=a
while current:
    print(current.data)
    current=current.next

count = 0
current = head

while current:
    count += 1
    current = current.next

print(count)

key=30
current=head
while current:
