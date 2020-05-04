# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/1/17 19:18
# @author  : Mo
# @function: 24.两两交换链表中的节点


# 24.两两交换链表中的节点
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例: # 给定1->2->3->4, 你应该返回2->1->4->3.

"""24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.
Example:
    Given 1->2->3->4, you should return the list as 2->1->4->3."""


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
    # 自己的方法, 遍历一遍, 获取elements然后再排序
    def swapPairs1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        elements = []
        count = 0
        head = head.next
        while head.next != None:
            if count % 2 == 0:
                elements.append(head.val)
            else:
                if len(elements)>2:
                    elements = elements[:-1] + [head.val]+ elements[-1:]
                else:
                    elements = [head.val] + elements
            head = head.next
            count += 1
        if len(elements) % 2 != 0:
            if len(elements) > 2:
                elements = elements[:-1] + [head.val] + elements[-1:]
            else:
                elements = [head.val] + elements
        else:
            elements = elements + [head.val]

        res_head = self.init_node(elements)
        return res_head.next
    # 递归, swap数据交换操作
    """
        方法一：递归
    这个题目要求我们从第一个节点开始两两交换链表中的节点，且要真正的交换节点。
    
    算法：从链表的头节点 head 开始递归。
    每次递归都负责交换一对节点。由 firstNode 和 secondNode 表示要交换的两个节点。
    下一次递归则是传递的是下一对需要交换的节点。若链表中还有节点，则继续递归。
    交换了两个节点以后，返回 secondNode，因为它是交换后的新头。
    在所有节点交换完成以后，我们返回交换后的头，实际上是原始链表的第二个节点。
    复杂度分析:
        时间复杂度：O(N)O(N)，其中 NN 指的是链表的节点数量。
        空间复杂度：O(N)O(N)，递归过程使用的堆栈空间。
    作者：LeetCode
    链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/liang-liang-jiao-huan-lian-biao-zhong-de-jie-di-19/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """
    def swapPairs_g(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next = self.swapPairs_g(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node
    """方法二：迭代
        我们把链表分为两部分，即奇数节点为一部分，偶数节点为一部分，A 指的是交换节点中的前面的节点，B 指的是要交换节点中的后面的节点。在完成它们的交换，我们还得用 prevNode 记录 A 的前驱节点。
        算法：
        firstNode（即 A） 和 secondNode（即 B） 分别遍历偶数节点和奇数节点，即两步看作一步。
        交换两个节点：
         firstNode.next = secondNode.next
         secondNode.next = firstNode
        还需要更新 prevNode.next 指向交换后的头。
        prevNode.next = secondNode
        迭代完成后得到最终的交换结果。
        复杂度分析：
            时间复杂度：O(N)O(N)，其中 NN 指的是链表的节点数量。
            空间复杂度：O(1)O(1)。
        
        作者：LeetCode
        链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/liang-liang-jiao-huan-lian-biao-zhong-de-jie-di-19/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""
    def swapPairs_(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:
            # Nodes to be swapped
            first_node = head
            second_node = head.next

            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head node.
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    num1 = [1, 2, 3, 4]
    nums = sol.init_node(num1)

    res = sol.swapPairs1(nums)
    try:
        while True:
            print(res.val)
            res = res.next
    except:
        gg = 0




