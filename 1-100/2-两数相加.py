'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None


class Solution:
    def __init__(self):
        self.x = 0

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = val2 = 0
        w = 1
        while l1 != None:
            val1 = val1 + l1.val * w
            l1 = l1.next
            w *= 10
        w = 1
        while l2 != None:
            val2 = val2 + l2.val * w
            l2 = l2.next
            w *= 10

        val3 = val1 + val2
        val3 = str(val3)
        p = l3 = ListNode(val3[-1])
        for i in range(0, len(val3)-1)[::-1]:
            p.next = ListNode(val3[i])
            p = p.next
        return l3
