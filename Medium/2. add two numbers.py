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

    def __repr__(self):
        if self:
            # return str(self.val)
            return "{} -> {}".format(self.val, self.next)

class Solution(object):
    def addTwoNumbers(self, l1, l2):     #Time:  O(max(m,n))   Space: O(max(m,n))
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
            carry = result // 10
            temp.next = newNode
            temp = temp.next
        return dummy.next

    def addTwoNumbers1(self, l1, l2):
        temp = dummy = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            val = (l1 and l1.val or 0) + (l2 and l2.val or 0) + carry
            carry = val // 10
            temp.next = ListNode(val % 10)
            l1 = l1 and l1.next
            l2 = l2 and l2.next
            temp = temp.next
        return dummy.next

    def addTwoNumbers2(self, l1, l2):
        dummy = ListNode(0)
        temp, carry = dummy, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            temp.next = ListNode(val)
            temp = temp.next

        if carry == 1:
            temp.next = ListNode(1)

        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(4)
    l2 = ListNode(2)
    l2.next = ListNode(3)
    l2.next.next = ListNode(5)
    print(Solution().addTwoNumbers1(l1, l2))