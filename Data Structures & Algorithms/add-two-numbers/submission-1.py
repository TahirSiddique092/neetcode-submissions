# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next

        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        
        ans = int(num1) + int(num2)

        dummy = ListNode()
        tail = dummy

        if ans == 0:
            return ListNode(0)
        while ans > 0:
            rem = ans%10
            new_node = ListNode(rem)
            ans = ans // 10
            tail.next = new_node
            tail = tail.next
        
        return dummy.next
