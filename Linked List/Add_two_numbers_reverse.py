class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def Add_two_numbers_reverse(l1,l2):
    carry=0
    ans=p=Node(123)
    while l1 and l2:
        sum_of_nodes=l1.data+l2.data+carry
        carry=sum_of_nodes//10
        p.next=Node(sum_of_nodes%10)
        p,l1,l2=p.next,l1.next,l2.next
    while l1:
        sum_of_nodes=l1.data+carry
        carry=sum_of_nodes//10
        p.next=Node(sum_of_nodes%10)
        p,l1=p.next,l1.next
    while l2:
        sum_of_nodes=l2.data+carry
        carry=sum_of_nodes//10
        p.next=Node(sum_of_nodes%10)
        p,l2=p.next,l2.next
    if carry:
        p.next=Node(carry)

    return ans.next