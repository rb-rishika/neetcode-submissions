# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0 or not lists:
            return None
        #this makes sure there is only one list
        while(len(lists)>1):
            mergeLists=[]
            for i in range(0, len(lists), 2):
                l1= lists[i]
                l2= lists[i+1] if i+1<len(lists) else None
                mergeLists.append(self.mergeTwoSortedLists(l1,l2))#[[1,3,5,7],[2,4], [6,8]] -> [[1,2,3,4,5,7]]
            lists=mergeLists
        return lists[0]

    def mergeTwoSortedLists(self, l1, l2):
        head=curr=ListNode()
        while l1 and l2:
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        if l1:
            curr.next=l1
        if l2:
            curr.next=l2
        return head.next
        