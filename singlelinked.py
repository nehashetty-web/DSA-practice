'''Write a program to create a singly linked list and display all its elements.
Write a program to insert a new node at the beginning of a singly linked list.
Write a program to delete the last node from a singly linked list.
Write a program to search for a given element in a singly linked list and display 
whether it is found or not.'''
# inserting in beginning
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_begin(head, data):
    new_node =Node(data)
    new_node.next = head
    head = new_node
    return head

# insert at end
def insert_end(head, data):
    new_node = Node (data)
    if head is None:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head

# traversal
def travers(head):
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print(None)

# delete in beginning
def delete_begin(head):
    if head is None:
        return head
    head = head.next
    return head

# delete by value
def delete_value(head, value):
    if head is None:
        return head
    if head.data == value:
        return head.next
    temp = head
    while temp.next and temp.next.data != value:
        temp = temp.next
    if temp.next:
        temp.next = temp.next.next
    return head

head = None
head = insert_begin(head, 10)
travers(head)
