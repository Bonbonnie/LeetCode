'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            runner = cur.next
            while runner and cur.val == runner.val:
                runner = runner.next
            cur.next = runner
            cur = runner
        return head

    def deleteDuplicates1(self, head):
        if not head:
            return head
        if head.next:
            if head.val == head.next.val:
                head = self.deleteDuplicates1(head.next)
            else:
                head.next = self.deleteDuplicates1(head.next)
        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    print(Solution().deleteDuplicates1(head))