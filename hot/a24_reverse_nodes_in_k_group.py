# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/2/28 19:00
# @author  : Mo
# @function: reverse-nodes-in-k-group


"""25. K 个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""

"""25. Reverse Nodes in k-Group
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
Example:
    Given this linked list: 1->2->3->4->5
    For k = 2, you should return: 2->1->4->3->5
    For k = 3, you should return: 3->2->1->4->5
Note:
    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, only nodes itself may be changed.
    """
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 初始化链表head, -1为头指针
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
    # 先链表转为list, 再排序, 再list转链表
    def reverseKGroupmy(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        elements = []
        elements.append(head.val)
        while head.next != None:
            head=head.next
            elements.append(head.val)

        if len(elements) < k:
            res_head = self.init_node(elements)
        else:
            elements_re = []
            len_ele = len(elements)
            for i in range(len_ele):
                if i % k == 0 or len_ele < k or (len_ele > k and i >= (len_ele//k)*k):
                    elements_re.append(elements[i])
                else:
                    if i > k:
                        len_k = i % k
                        elements_re = elements_re[:-len_k] + [elements[i]] + elements_re[-len_k:]
                    else:
                        elements_re = [elements[i]] + elements_re
            res_head = self.init_node(elements_re)

        return res_head.next
    # 栈,每次迭代设置k, 分别判断, 设置一个list保存ListNode
    def reverseKGroup_1(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        while True:
            count = k
            stack = []
            tmp = head
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            # 注意,目前tmp所在k+1位置
            # 说明剩下的链表不够k个,跳出循环
            if count:
                p.next = head
                break
            # 翻转操作
            while stack:
                p.next = stack.pop()
                p = p.next
            # 与剩下链表连接起来
            p.next = tmp
            head = tmp

        return dummy.next
    # 尾插法, 孤立cur然后依次插在后部分
    def reverseKGroup_2(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        tail = dummy
        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail: break
            head = pre.next
            while pre.next != tail:
                cur = pre.next  # 获取下一个元素
                # pre与cur.next连接起来,此时cur(孤单)掉了出来
                pre.next = cur.next
                cur.next = tail.next  # 和剩余的链表连接起来
                tail.next = cur  # 插在tail后面
            # 改变 pre tail 的值
            pre = head
            tail = head
        return dummy.next
    # 递归
    def reverseKGroup_3(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup_3(cur, k)
            while count:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur
        return head


if __name__ == '__main__':
    sol = Solution()
    num1 = [1,2,3,4]
    k = 2
    nums = sol.init_node(num1)
    # res = sol.reverseKGroupmy(nums.next, k)
    res = sol.reverseKGroup_2(nums.next, k)
    # res = sol.reverseKGroup_3(nums.next, k)

    try:
        while True:
            print(res.val)
            res = res.next
    except:
        gg = 0







