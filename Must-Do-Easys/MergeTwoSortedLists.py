# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        startNode = ListNode()
        tailNode = startNode
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                tailNode.next = list1
                list1 = list1.next
                
            elif list1.val > list2.val:
                tailNode.next = list2
                list2= list2.next
                
            else:
                tailNode.next = list1
                list1 = list1.next
                tailNode = tailNode.next

                tailNode.next = list2
                list2= list2.next
                
            tailNode = tailNode.next
        
        if list1 == None and list2 != None:
            tailNode.next = list2
        
        elif list1!= None and list2 == None:
            tailNode.next = list1
            
        return startNode.next