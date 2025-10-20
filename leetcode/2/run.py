"""
[9,9,9,9,9,9,9]
[9,9,9,9]
[8,9,9,9,]

	[9] -> [9] -> [9] -> [9] -> [9] -> [9] -> [9] -> None

	[9] -> [9] -> [9] -> [9] -> None
	_______
Carry    0      1     1      1      1      1      1      1
Sum	18     18     18     18     9      9      9      0
Value	[8] -> [9] -> [9] -> [9] -> [0] -> [0] -> [0] -> [1]


Assumption: 
It only stops, when we encounter a None on both list AND the carry for the next digit is zero. 

Sum the two digits, defining the current node value and the carry for the next.

Set the cur_node_value (digit_sum PLUS carry).
Create a new node, appending it to the final of our list.

If we encounter a None at list l1, for example, the contribution of that list to our digit_sum from now on will be zero. The same for l2. When both l1 and l2 next node are None, the execution ends. (Creating a final new node that will receive the sum contribution of l1 and l2, which is zero, plus the carry from the previous sum)

carry_from_previous_node = 0


while...

	cur_node.val = l1_contribution + l2_contribution + carry_from_previous_node

	if l1_cur_node.val == None:
		l1_contribution = 0
	else:
		l1_contribution = l1_cur_node.val 

	if l2_cur_node.val == None:
		l2_contribution = 0
	else:
		l2_contribution = l2_cur_node.val
		
	digit_sum = l1_contribution + l2_contribution
	
	if digit_sum < 10:	
		...
		# carry_for_next_node = ...
	
	l3_cur_node.val = digit_sum + carry_from_previous_node
	
	carry_from_previous_node = carry_for_next_node
	
	# Advance one node on the list.
	# At this point, one of them can be None. If this is the case, don't update anymore, just let the variable as none. When both become None, we break out of while loop.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Let's establish that our answer list is called l3

        carry_from_previous_node = 0
        carry_for_next_node = 0
        
        l1_cur_node = l1
        l2_cur_node = l2

        l3_head = ListNode()
        l3_cur_node = l3_head

        while True:            

            if l1_cur_node == None:
                l1_sum_contribution = 0
            else:
                l1_sum_contribution = l1_cur_node.val

            if l2_cur_node == None:
                l2_sum_contribution = 0
            else:
                l2_sum_contribution = l2_cur_node.val

            cur_node_value = l1_sum_contribution + l2_sum_contribution + carry_from_previous_node
            
            if cur_node_value < 10:
                carry_for_next_node = 0
            elif cur_node_value == 10:
                cur_node_value = 0
                carry_for_next_node = 1
            elif cur_node_value > 10:
                cur_node_value = cur_node_value % 10
                carry_for_next_node = 1

            l3_cur_node.val = cur_node_value
            carry_from_previous_node = carry_for_next_node

            if l1_cur_node is not None:
                l1_cur_node = l1_cur_node.next
            if l2_cur_node is not None:
                l2_cur_node = l2_cur_node.next
            
            if l1_cur_node is None and l2_cur_node is None and carry_from_previous_node == 0:
                break

            new_node = ListNode()
            l3_cur_node.next = new_node
            l3_cur_node = l3_cur_node.next
                

        return l3_head
