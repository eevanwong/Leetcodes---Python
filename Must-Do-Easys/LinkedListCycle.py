
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        np = set()
        
        while head is not None:
            if head in np:
                return True
            else:
                np.add(head)
            head = head.next
                
        return False 
        
        # we can use a set to store the nodes
        
# O(n) space, q asks for O(1) space, can be done by hashing the node

# my attempt at hashing node:

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:        
        while head is not None:
            if head.val >= 10**6:
                return True
            else:
                head.val += 10**6
            head = head.next
                
        return False 
        
        # we can use a set to store the nodes


# very non elegant solution cuz i just did a num thats outside the potential range of head.val (-10**5 < val < 10**5), still works tho