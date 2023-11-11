class Node:
    def __init__(self,data,next=None) :
        self.data=data
        self.next=next

    def __str__(self) :
        return f"node {self.data}-->{self.next}"

def print_ll(head):
    while head:
        print(head.data)
        head=head.next
        
    
a=Node(1,Node(2,Node(3,Node(4))))
print_ll(a)
                                       
        