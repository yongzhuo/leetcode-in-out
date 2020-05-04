# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/1/14 19:25
# @author  : Mo
# @function: 23. 合并K个排序链表


# from Queue import PriorityQueue


# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
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
    # 暴力法，先合并所有数字，排序，然后再创建，
        # 时间复杂度：O(NlogN) ，其中 NN 是节点的总数目。
        # 遍历所有的值需花费 O(N)O(N) 的时间。
        # 一个稳定的排序算法花费 O(NlogN) 的时间。
        # 遍历同时创建新的有序链表花费 O(N) 的时间。
        # 空间复杂度：O(N) 。
        # 排序花费 O(N) 空间（这取决于你选择的算法）。
        # 创建一个新的链表花费 O(N)O(N) 的空间。
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

    # 方法2：逐一比较算法
    #     比较k个节点（每个链表的首节点），获得最小值的节点。
    #     将选中的节点接在最终有序链表的后面。
    #     复杂度分析
    #     时间复杂度： O(kN)，其中k是链表的数目。几乎最终有序链表中每个节点的时间开销都为O(k)k - 1次比较）。
    #     总共有NN个节点在最后的链表中。
    #     空间复杂度：O(n)
    #     创建一个新的链表空间开销为O(n)
    #     O(1) 。重复利用原来的链表节点，每次选择节点时将它直接接在最后返回的链表后面，而不是创建一个新的节点。
    # 方法3：用优先队列优化方法
    #     几乎与上述方法一样，除了将比较环节用优先队列进行了优化。
    def mergeKLists2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next

    def mergeKLists3(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next


if __name__ == '__main__':
    sol = Solution()
    num1, num2, num3 = [-1, 0, 1, 2], [-4, -1, 0, 0], [1, 2]  # [1,2,3,4, -1,-2-3,-4,0]
    sol_num1 = sol.init_node(num1)
    sol_num2 = sol.init_node(num2)
    sol_num3 = sol.init_node(num3)

    res = sol.mergeKLists3([sol_num1, sol_num2, sol_num3])
    while res.next != None:
        print(res.val)
        res = res.next
