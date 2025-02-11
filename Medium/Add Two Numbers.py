class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        head = None  # This will be the head of the result linked list
        current = None
        
        # Iterate while l1 or l2 is not null
        while l1 or l2 or carry:
            # Get the current values of l1 and l2, default to 0 if they are null
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10  # Carry for the next iteration
            
            # Create a new node for the current digit
            new_node = ListNode(total % 10)
            
            # If it's the first node, set the head
            if not head:
                head = new_node
            else:
                current.next = new_node
            
            # Move to the next node in the result list
            current = new_node
            
            # Move to the next nodes in l1 and l2, if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return head