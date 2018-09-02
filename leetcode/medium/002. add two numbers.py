'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        temp = dummy
        carry = 0
        while l1 or l2 or carry:
            result = carry
            if l1:
                result += l1.val
                l1 = l1.next
            if l2:
                result += l2.val
                l2 = l2.next
            newNode = ListNode(result % 10)
            carry = result / 10
            temp.next = newNode
            temp = temp.next
        return dummy.next

    def addTwoNumbers1(self, l1, l2):
        temp = dummy = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            val = (l1 and l1.val or 0) + (l2 and l2.val or 0) + carry
            carry = val / 10
            temp.next = ListNode(val % 10)
            l1 = l1 and l1.next
            l2 = l2 and l2.next
            temp = temp.next
        return dummy.next


if __name__ == "__main__":
    list1 = ListNode(-1)
    list1.val = 2
    list1.next = 4
    # list1.next.next = 3
    list2 = ListNode(0)
    list2.val = 5
    list2.next = 6
    # list2.next.next = 4
    print(Solution().addTwoNumbers(list1, list2))
    #assert (Solution().addTwoNumbers(list1, list2) == [7, 0, 8])
