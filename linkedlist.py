class Node:
     def __init__(Self,data):
        Self.data=data
        Self.next=None

def insert_begin(head,data):
     new_node=Node (data)
     new_node.next=head
     head=new_node
     return head
def insert_end (head,data):
     new_node=Node (data)
     if head is None:
          return new_node
     temp=head
     while temp.next:
          temp=temp.next
          temp.next=new_node
          return head
def travers(head):
     temp=head
     while temp:
          print(temp.next,end="->")
     temp=temp.next
     print(None)
def delete_begin(head):
     if head is None:
          return 
     head=head.next
     return head
def delete_value(head,value):
     if head is None:
          return head
     if head.next==value:
          return head.next
     temp=head
     while temp.next and temp.next.next!= value:
          temp=temp.next
     if temp.next:
          temp.next=temp.next.next
          return head
def reverse(head):
     prev=None
     while curr:
      new_node=curr.next
      curr.next=prev
      prev=curr 
      curr=new_node
      return prev


          

     
     
     

          