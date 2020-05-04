# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/8/20 23:04
# @author   :Mo
# @function :两数相加(add two numbers)(链表)


# 两数相加
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 链表生成
def create_list_node(nums):
    # https://www.jianshu.com/p/b1bea96aba01
    num_next = None
    for num in reversed(nums):
        list_node = ListNode(num)
        list_node.next = num_next
        num_next = list_node
    return num_next

# 链表打印
def print_list_node(res: ListNode):
    list_node_print = ""
    while True:
        try:
            data_val = res.val
        except:
            data_val = None
        if data_val:
            list_node_print = list_node_print + ">" + str(data_val)
            res = res.next
        else:
            print(list_node_print)
            break


# 0.56s
class Solution1:
    def addTwoNumbers(self, l1, l2):
        target = ListNode(0)  # 作为根节点的引用
        p = target
        add = 0  # 作为上一次相加是否需要进1的依据
        while l1 and l2:
            # //整出结果的整数部分, %整除结果的余数部分
            p.next = ListNode((l1.val + l2.val + add) % 10)
            add = (l1.val + l2.val + add) // 10
            p, l1, l2 = p.next, l1.next, l2.next
        l1 = l1 if l1 else l2
        while add:
            if l1:
                p.next = ListNode((l1.val + add) % 10)
                add = (l1.val + add) // 10
                p, l1 = p.next, l1.next
            else:
                p.next = ListNode(add)
                p = p.next
                break
        p.next = l1

        return target.next


# 0.77s
class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x1 = ''
        while l1:
            x1 += str(l1.val)
            l1 = l1.next
        x2 = ''
        while l2:
            x2 += str(l2.val)
            l2 = l2.next
        res = int(x1[::-1]) + int(x2[::-1])
        res = str(res)[::-1]
        ans = ListNode(int(res[0]))
        ans1 = ans
        for i in res[1:]:
            ans.next = ListNode(int(i))
            ans = ans.next
        return ans1


# 0.56s
class Solution3:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n = l1.val + l2.val
        l3 = ListNode(n % 10)
        l3.next = ListNode(n // 10)
        p1 = l1.next
        p2 = l2.next
        p3 = l3
        while True:
            if p1 and p2:
                sum = p1.val + p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p1 = p1.next
                p2 = p2.next
                p3 = p3.next
            elif p1 and not p2:
                sum = p1.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p1 = p1.next
                p3 = p3.next
            elif not p1 and p2:
                sum = p2.val + p3.next.val
                p3.next.val = sum % 10
                p3.next.next = ListNode(sum // 10)
                p2 = p2.next
                p3 = p3.next
            else:
                if p3.next.val == 0:
                    p3.next = None
                break
        return l3


# 5 lines, 0.45s
class Solution4:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        if not (l1 or l2): return ListNode(1) if carry else None
        l1, l2 = l1 or ListNode(0), l2 or ListNode(0)
        val = l1.val + l2.val + carry
        l1.val, l1.next = val % 10, self.addTwoNumbers(l1.next, l2.next, val > 9)
        return l1


# 0.54s
class Solution5:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add = 0
        l3 = l4 = ListNode(0)
        while l1 or l2 or add:
            if l1 or l2:
                if l1:
                    num = l1.val + add
                    if l2:
                        num = num + l2.val
                elif l2:
                    num = l2.val + add
                    if l1:
                        num = num + l1.val
            else:
                num = add
            add = 0
            if num // 10 > 0:
                add = 1
                num = num % 10
            l3.val = num

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            if l1 or l2 or add:
                l3.next = ListNode(0)
                l3 = l3.next
        return l4


class Solution01:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        Pointer = ListNode(0)
        q = Pointer
        add = 0
        while l1 and l2:
            q.next = ListNode((l1.val + l2.val + add) % 10)
            add = (l1.val + l2.val + add)//10
            q, l1, l2 = q.next, l1.next, l2.next
        l1 = l1 if l1 else l2
        while add:
            if l1:
                q.next = ListNode((l1.val + add) % 10)
                add = (l1.val + add) // 10 if add else 0
                q, l1 = q.next, l1.next
            else:
                q.next = ListNode(add)
                q = q.next
                break
        q.next = l1
        return Pointer.next


if __name__=="__main__":
    import time
    time_start = time.time()
    for i in range(2):
        l1 = create_list_node([9, 5, 7, 7, 9])
        l2 = create_list_node([3, 1, 7])
        so = Solution01()
        res = so.addTwoNumbers(l1, l2)
    print(time.time()-time_start)
    print_list_node(l1)
    print_list_node(l2)
    print_list_node(res)



