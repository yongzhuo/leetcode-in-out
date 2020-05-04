# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/1/13 19:52
# @author  : Mo
# @function: 21.合并两个有序链表


# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 初始化链表head
    def init_node(self, elemts):
        num = elemts
        head = None
        node = ListNode(-1)
        node.next = head
        head = node

        for n in num:
            node = ListNode(n)
            # 由于特殊情况当链表为空时没有next，所以在前面要做个判断
            if head == None:
                head = node
            else:
                cur = head
                while cur.next != None:
                    cur = cur.next
                cur.next = node
        return head
    # 归并排序(自己的链表都有-1头指针)
    def mergeTwoLists(self, l1, l2):
        head = None
        node = ListNode(-1)
        node.next = head
        p = node
        # letcode上删除
        l1, l2 = l1.next, l2.next

        # 等长部分
        while l1 and l2:
            if l2.val > l1.val:
                while p.next != None:
                    p = p.next
                p.next = ListNode(l1.val)
                l1 = l1.next
            else:
                while p.next != None:
                    p = p.next
                p.next = ListNode(l2.val)
                l2 = l2.next
        # 多出部分
        l1 = l1 if l1 else l2
        while l1:
            if l1:
                while p.next != None:
                    p = p.next
                p.next = ListNode(l1.val)
                l1 = l1.next
            else:
                break
        return node.next
    # 递归
    def mergeTwoLists2(self, l1, l2):# letcode上删除
        # l1, l2 = l1.next, l2.next
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    sol = Solution()
    num1, num2 = [-1, 0, 1, 2], [-4, -1, 0, 0]  # [1,2,3,4, -1,-2-3,-4,0]
    sol_num1 = sol.init_node(num1)
    sol_num2 = sol.init_node(num2)

    res = sol.mergeTwoLists2(sol_num1, sol_num2)
    while res.next != None:
        print(res.val)
        res = res.next




