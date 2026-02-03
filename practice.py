'''Write a Python program to create a singly linked list and display its elements.
Write a Python function to insert a node at the beginning of a singly linked list.
rite a Python function to insert a node at the end of a singly linked list.'''
"solutions"
class Node:
    def __init__(self, data):
     self.data=data
     self.next=None
def travers(head):
   temp=head
   while temp:
      print(temp.data,end="->")
      temp=temp.next
print(None)


n1=node(10)
n2=node(80)
n3=node(30)

head=n1

travers(head)
