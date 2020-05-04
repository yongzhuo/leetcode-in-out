# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/9/9 19:19
# @author   :Mo
# @function :9. 回文数
# @ways     :解题思路
#               a.转化为字符串反转比对
#               b.数字,一一对比,%1000,10
#               c.反转一半比对,前后


# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 进阶:
#
# 你能不将整数转为字符串来解决这个问题吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindrome-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




class Solution00:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            y = str(x)[::-1]
            if y == str(x):
                return True
            else:
                return False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        elif x < 10: return True
        elif x % 10 == 0: return False
        x1 = list()
        while x > 0:
            x1.append(x % 10)
            x = x//10
        for i in range(len(x1)//2):
            if x1[i] != x1[len(x1)-1-i]: return False
        return True


if __name__ == '__main__':
    ques = 12321
    sol = Solution()
    judge = sol.isPalindrome(ques)
    print(ques)
    print(judge)









