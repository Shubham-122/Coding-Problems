# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        dummy_head = ListNode(0)
        temp = dummy_head
        carry=0

        while l1!=None or l2!=None or carry!=0:
            summ=0
            if l1:
                summ+=l1.val
                l1=l1.next
            
            if l2:
                summ+=l2.val
                l2=l2.next

            summ+=carry
            carry = summ//10
            new= ListNode(summ%10)
            temp.next=new
            temp=temp.next
        return dummy_head.next


        