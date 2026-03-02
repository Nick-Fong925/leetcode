"""
Found somewhat unintuitive in the beggining, important to check all linked list questions for 3 things
1. Does it need a dummy node?
2. Are we interating all  the points
3. Do we need dummy values

Initially implementation was bad because I did not think intuitively that v1 or v2 could actually be set as 0
This makes it significantly easier to work with not having many cases with pointers and other things

Time complexity: O(max(m,n)) -> generally one iteration but can be more because carry 
Space complexity: O(max(m,n)) -> we are storing a dummy node and storing basically the entire list if not more.
"""


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = result = ListNode(0, None)
        carry = 0

        while l1 or l2 or carry:
            v1 = 0
            v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next    
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            sum = v1 + v2 + carry
            carry = sum // 10
            sum %= 10

            curr_node.next = ListNode(sum, None)
            curr_node = curr_node.next
        return result.next