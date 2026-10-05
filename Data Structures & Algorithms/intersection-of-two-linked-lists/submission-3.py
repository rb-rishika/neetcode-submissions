# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def getLength(head):
            length=0
            while head:
                head=head.next
                length+=1
            return length

        lengthA= getLength(headA)
        lengthB= getLength(headB)

        if lengthA > lengthB:
            for _ in range(lengthA-lengthB):
                headA=headA.next
        else: 
            for _ in range(lengthB-lengthA):
                headB=headB.next
        
        while headA!=headB:
            headA=headA.next
            headB=headB.next
        return headB


                
                