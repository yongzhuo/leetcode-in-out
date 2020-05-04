# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/3/31 19:55
# @author  : Mo
# @function:


"""38. 外观数列
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

 

示例 1:

输入: 1
输出: "1"
解释：这是一个基本样例。
示例 2:

输入: 4
输出: "1211"
解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。
通过次数84,500提交次数154,401
"""


"""
38. Count and Say
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".
通过次数84,500提交次数154,401"""


from collections import defaultdict, Counter
from typing import List

"""下一个数是对上一个数的描述，比方说 1211 里有 “ 1 个 1 ， 1 个 2 ， 2 个 1 ” ，
                                        那么 111221 就是它的下一个数。通常我们把这个数列叫做“外观数列”。
"""
class Solution:
    # my, 直接正向, 求法同2,3.
    def countAndSay(self, n: int) -> str:
        def count_str(res_pre):
            if res_pre == "1":
                return "11"
            i_pre = []
            res_return = ""
            len_pre = len(res_pre)
            for i in range(len_pre):
                if not i_pre:
                    i_pre.append(res_pre[i])
                elif i_pre[-1] == res_pre[i] and i != len_pre - 1:
                    i_pre.append(res_pre[i])
                elif i == len_pre - 1 and i_pre:
                    if i_pre[-1] == res_pre[i]:
                        res_return += str(len(i_pre) + 1) + i_pre[-1]
                    else:
                        res_return += str(len(i_pre)) + i_pre[-1]
                        i_pre = [res_pre[i]]
                        res_return += str(len(i_pre)) + i_pre[-1]
                else:
                    res_return += str(len(i_pre)) + i_pre[-1]
                    i_pre = [res_pre[i]]

            return res_return
        if n == 1:
            return "1"
        n = n - 1
        sequence1 = "1"
        for i in range(n):
            res = count_str(sequence1)
            sequence1 = res
        return sequence1
    """使用递归的方法
这道题其实跟斐波那契数列有点类似，都是基于上一项的结果得出下一项的结果，因此适合使用递归来解决问题。

因为确定了n=1时的值，所以基线条件就可以设置为 n <= 1 时返回。


在后面的循环里，思路是当遇到的字符串与上一个相等的时候，计数器+1，否则结束计数，并将当前结果添加到res变量中，并且计数器恢复到1。
比较需要注意的是边际条件，在字符串开头跟结尾的时候做了单独的处理。

作者：mmmz
链接：https://leetcode-cn.com/problems/count-and-say/solution/python3-di-gui-fa-jie-wai-guan-shu-lie-by-mmmz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""
    # 递归
    def countAndSay1(self, n: int) -> str:
        if n <= 1:
            return '1'
        pre = self.countAndSay(n - 1)

        res = ''
        count = 1
        for idx in range(len(pre)):

            if idx == 0:
                count = 1

            elif pre[idx] != pre[idx - 1]:
                tmp = str(count) + pre[idx - 1]
                res += tmp
                count = 1
            elif pre[idx] == pre[idx - 1]:
                count += 1

            if idx == len(pre) - 1:
                tmp = str(count) + pre[idx]
                res += tmp
        return res
    """
    要求第n个s字符串只需分析第n-1个字符串：

创建一个栈（用其他结构可能更好）
遍历字符串：
1.当字符与栈内字符相同或者栈为空时入栈
2.当字符与栈内字符不相同时，取栈的长度+栈内字符，清空栈并将新的元素入栈
（注意：最后栈不为空所以在循环结束后需要在进行一次取栈的长度+栈内字符的操作）

作者：ripking
链接：https://leetcode-cn.com/problems/count-and-say/solution/dong-tai-gui-hua-fa-by-ripking/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""
    # 动态规划
    def countAndSay2(self, n: int) -> str:
        num = []
        num.append("")
        num.append("1")
        if n == 1: return num[1]
        for i in range(2, n + 1):
            p = []
            s = ""
            for x in num[i - 1]:
                if p == [] or x == p[0]:
                    p.append(x)
                else:
                    s += str(len(p))
                    s += p[0]
                    p = []
                    p.append(x)
            s += str(len(p))
            s += p[0]
            num.append(s)

        return num[n]


if __name__ == '__main__':
    sol = Solution()
    n = 32
    res = sol.countAndSay2(n)
    print(res)
    gg = 0


    # def count_str(res_pre):
    #     if res_pre == "1":
    #         return "11"
    #     i_pre = []
    #     res_return = ""
    #     len_pre = len(res_pre)
    #     for i in range(len_pre):
    #         if not i_pre:
    #             i_pre.append(res_pre[i])
    #         elif i_pre[-1] == res_pre[i] and i != len_pre - 1 :
    #             i_pre.append(res_pre[i])
    #         elif i == len_pre - 1 and i_pre:
    #             if i_pre[-1] == res_pre[i]:
    #                 res_return += str(len(i_pre) + 1) + i_pre[-1]
    #             else:
    #                 res_return += str(len(i_pre)) + i_pre[-1]
    #                 i_pre = [res_pre[i]]
    #                 res_return += str(len(i_pre)) + i_pre[-1]
    #         else:
    #             res_return += str(len(i_pre)) + i_pre[-1]
    #             i_pre = [res_pre[i]]
    #
    #     return res_return
    #
    # print(count_str("11"))
