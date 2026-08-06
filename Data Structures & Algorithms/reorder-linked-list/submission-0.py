# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Goal 1- to find mid point
        #Goal 2- to reverse everything after mid 
        #Goal 3- to to merge these lists one by one

        #Goal-1
        slow = head
        fast = head.next 

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        secondHalf= slow.next

        #Goal 2
        slow.next=None
        prev=None #refer ipad

        while secondHalf:
            temp= secondHalf.next 
            secondHalf.next = prev
            prev= secondHalf
            secondHalf=temp
        
        #1-> 2-> 3-> None | None <-4 <- 5

        #Goal 3 (merging)
        firstLL, secondLL = head, prev
        while secondLL:
            tmp1,tmp2= firstLL.next, secondLL.next
            firstLL.next= secondLL #1-> 5->
            secondLL.next = tmp1
            firstLL, secondLL= tmp1, tmp2 #incr poimters

         



        


    

         
        