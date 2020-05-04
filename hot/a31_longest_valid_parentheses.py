# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/3/10 19:26
# @author  : Mo
# @function: 32. Longest Valid Parentheses


"""
32. 最长有效括号
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
通过次数43,583提交次数145,953
"""
"""
32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
通过次数43,583提交次数145,953"""


class Solution:
    # 超时, O(N^3)
    def longestValidParenthesesmy(self, s):
        if not s or len(s) < 2:
            return 0
        len_s = len(s)
        len_res = []
        for i in range(len_s):
            for j in range(len_s-i+1):
                print(s[i:i+j])
                if self.isValid(s[i:i+j]):
                    len_res.append(len(s[i:i+j]))
        return max(len_res)

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0:
            return False

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "("}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
    # 栈, O(N) + O(NlogN)
    """    对于这种括号匹配问题，一般都是使用栈, 我们先找到所有可以匹配的索引号，然后找出最长连续数列！
       例如：s = )(()())，我们用栈可以找到，位置 2 和位置 3 匹配，位置 4 和位置 5 匹配，位置 1 和位置 6 匹配，
       这个数组为：2,3,4,5,1,6 这是通过栈找到的，我们按递增排序！1,2,3,4,5,6
       找出该数组的最长连续数列的长度就是最长有效括号长度！所以时间复杂度来自排序：O(nlogn)。
       接下来我们思考，是否可以省略排序的过程,在弹栈时候进行操作呢?直接看代码理解!所以时间复杂度为：O(n)。
        作者：powcai
        链接：https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-powcai/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""
    def longestValidParentheses1(self, s: str) -> int:
        if not s:
            return 0
        res = []
        stack = []
        # 首先求取匹配的索引
        for i in range(len(s)):
            if stack and s[i] == ")":
                stack_pop = stack.pop()
                res.append(stack_pop)
                res.append(i)
            if s[i] == "(":
                stack.append(i)
        res.sort() # 快排
        # print(res)
        i = 0
        ans = 0
        n = len(res) # 快排
        while i < n:
            j = i
            while j < n - 1 and res[j + 1] == res[j] + 1:
                j += 1
            ans = max(ans, j - i + 1)
            i = j + 1
        return ans
    # 栈优化, O(N), 省略排序的过程,在弹栈时候进行操作呢? 。
    def longestValidParentheses12(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res
    # dp方法
    """ 1. dp官方
        我们用 dp[i] 表示以 i 结尾的最长有效括号；
          当s[i]为(, dp[i]必然等于0，因为不可能组成有效的括号；
          那么 s[i] 为 )
              2.1 当 s[i-1]为(，那么dp[i]=dp[i-2]+2；
              2.2 当 s[i-1]为) 并且s[i-dp[i-1]-1]为(，那么dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]；
        时间复杂度：O(n)。
        作者：powcai
        链接：https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-powcai/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        2. 动态规划
        特判，若ss为空，返回00
        初试化dp=[0,...,0]dp=[0,...,0]，长度为nn。dp[i]dp[i]表示到ii位置的最长有效括号的长度。
        显然，当s[i]s[i]为((时，dp[i]=0dp[i]=0
        遍历字符串，遍历区间[1,n)[1,n)：
            当s[i]==)s[i]==)时，若s[i-1]==(s[i−1]==(，说明这两个有效。则dp[i]=dp[i-2]+2dp[i]=dp[i−2]+2
            否则s[i-1]==)s[i−1]==)，此时找到上一匹配字符串的上一位i-dp[i-1]-1i−dp[i−1]−1：
            若s[i-dp[i-1]-1]==(s[i−dp[i−1]−1]==(，说明s[i]s[i]可以和s[i-dp[i-1]-1]s[i−dp[i−1]−1]匹配：则dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2dp[i]=dp[i−1]+dp[i−dp[i−1]−2]+2，表示当前位置的最长有效括号长度等于上一位有效括号的长度加上自身匹配的上一位的有效括号的长度加上2。
            更新resres，res=max(res,dp[i])res=max(res,dp[i])
            返回resres
        
        作者：zhu_shi_fu
        链接：https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zhan-dong-tai-gui-hua-zhu-xing-jie-shi-dai-ma-pyth/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""
    def longestValidParentheses2(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i > 0 and s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res


if __name__ == '__main__':
    sol = Solution()
    longest_valid_parentheses = """))())(()))()(((()())(()(((()))))((()(())()((((()))())))())))()(()(()))))())(((())(()()))((())()())((()))(()(())(())((())((((()())()))((()(())()))()(()))))))()))(()))))()())()())()()()()()()()))()(((()()((()(())((()())))(()())))))))(()()(())())(()))))))()()())((((()()()())))))((())(())()()(()((()()))()()())(()())()))()(()(()())))))())()(())(()))(())()(())()((())()((((()()))())(((((())))())())(()((())((()()((((((())))(((())))))))(()()((((((()(((())()(()))(()())((()(((()((()(())())()())(((()))()(((()))))(())))(())()())()(((()))))((())())))())()()))((((()))(())()())()(((())(())(()()((())()())()()())())))((()())(()((()()()(()())(()))(()())((((()(()(((()(((())()((()(()))())()())))))))))))()())()(()(((())()))(((()))((((()())())(()())((()())(()()((()((((()())))()(())(())()))))(())())))))(((((((())(((((()))()))(()()()()))))))(()(()(()(()()(((()()))((()))())((())())()())()))()()(((())))()(())()()(())))(((()))))))))(())((()((()((()))))()()()((())((((((((((()(())))(())((()(()())())(((((((()()()()))())(((()())()(()()))))(()()))))(((()()((()()()(((()))))(()()())()()()(()))))()(())))))))()((((((((()((())))))))(()))()((()())())("""
    longest_valid_parentheses = "(()())("
    res = sol.longestValidParentheses1(longest_valid_parentheses)
    print(res)
    gg = 0

