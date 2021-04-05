# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None

        num1, num2 = 0, 0

        len1 = self.getlength(l1) - 1
        while len1 >= 0:
            num1 = num1 + (l1.val) * (10**len1)
            l1 = l1.next
            len1 -= 1

        len2 = self.getlength(l2) - 1
        while len2 >= 0:
            num2 = num2 + (l2.val)*(10**len2)
            l2 = l2.next
            len2 -= 1
        ans = num1 + num2

        head = None
        for i in str(ans):
            node = ListNode(int(i))
            node.next = head
            head = node
        return head


    def getlength(self, head):
        temp = head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        return length