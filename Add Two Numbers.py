# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1=l1
        p2=l2
        c=0
        head=curr=ListNode(0) #just to assign likedlist head.next is returned at end
        while (p1 or p2):
            if(p1 is None):
                v=p2.val+c
            elif(p2 is None):
                v=p1.val+c
            else:
                v=p1.val+p2.val+c
                
            
            if(v>=10):
                c=1
            else:
                c=0
            curr.next=ListNode(v%10)
            curr=curr.next
            
            if(p1 is None):#when linkedlist1 ends but not ll2
                p2=p2.next
            elif(p2 is None):#when ll2 ends but not ll1
                p1=p1.next
            else:
                p1=p1.next
                p2=p2.next
            if(p1 is None and p2 is None and c==1 ): #this condition is not to ignore carry at last
                curr.next=ListNode(c)
        
        
        
        return head.next