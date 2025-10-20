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
