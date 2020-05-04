# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/1/9 19:20
# @author  : Mo
# @function: 19.删除链表的倒数第N个字节



# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # for循环时候两个指针同时移动
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 增加一个特殊节点方便边界判断
        p = ListNode(-1)
        p.next, a, b = head, p, p
        # 第一个循环，b指针先往前走n步
        while n > 0 and b:
            b, n = b.next, n - 1
        # 假设整个链表长5，n是10，那么第一次遍历完后b就等用于空了
        # 于是后面的判断就不用做了，直接返回
        if not b:
            return head
        # 第二次，b指针走到链表最后，a指针也跟着走
        # 当遍历结束时，a指针就指向要删除的节点的前一个位置
        while b.next:
            a, b = a.next, b.next
        # 删除节点并返回
        a.next = a.next.next
        return p.next
    # 娅点
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy
        for i in range(n + 1):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
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


if __name__ == '__main__':
    sol = Solution()
    num = [-1,0,1,2,-1,-4, 0, 0] # [1,2,3,4, -1,-2-3,-4,0]
    sol_num = sol.init_node(num)
    res = sol.removeNthFromEnd(sol_num, 3)
    while res.next != None:
        print(res.val)
        res = res.next


