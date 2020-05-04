
# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/9/26 19:39
# @author   :Mo
# @function :10.正则表达式匹配

# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 示例 3:
#
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 示例 4:
#
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 示例 5:
#
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/regular-expression-matching
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



# 方法
# 1：回溯
# 想法
#
# 如果没有星号（正则表达式中的 * ），问题会很简单——我们只需要从左到右检查匹配串
# s
# 是否能匹配模式串
# p
# 的每一个字符。
#
# 当模式串中有星号时，我们需要检查匹配串
# s
# 中的不同后缀，以判断它们是否能匹配模式串剩余的部分。一个直观的解法就是用回溯的方法来体现这种关系。
#
# 算法
#
# 如果没有星号，我们的代码会像这样：
#
# Python
#
#
# def match(text, pattern):
#     if not pattern: return not text
#     first_match = bool(text) and pattern[0] in {text[0], '.'}
#     return first_match and match(text[1:], pattern[1:])
#
#
# 如果模式串中有星号，它会出现在第二个位置，即 \text
# {pattern[1]}
# pattern[1] 。这种情况下，我们可以直接忽略模式串中这一部分，或者删除匹配串的第一个字符，前提是它能够匹配模式串当前位置字符，即 \text
# {pattern[0]}
# pattern[0] 。如果两种操作中有任何一种使得剩下的字符串能匹配，那么初始时，匹配串和模式串就可以被匹配。
#
# JavaPython
#
#
# class Solution(object):
#     def isMatch(self, text, pattern):
#         if not pattern:
#             return not text
#
#         first_match = bool(text) and pattern[0] in {text[0], '.'}
#
#         if len(pattern) >= 2 and pattern[1] == '*':
#             return (self.isMatch(text, pattern[2:]) or
#                     first_match and self.isMatch(text[1:], pattern))
#         else:
#             return first_match and self.isMatch(text[1:], pattern[1:])
#
#
# 复杂度分析
#
# 时间复杂度：用
# TT
# 和
# PP
# 分别表示匹配串和模式串的长度。在最坏情况下，函数
# match(text[i:], pattern[2j:])
# 会被调用 \binom
# {i + j}
# {i}(
#     i
# i + j
# ​
# ) 次，并留下长度为
# O(T - i)
# O(T−i) 和
# O(P - 2 * j)
# O(P−2∗j) 长度的字符串。因此，总时间为 \sum_
# {i = 0} ^ T \sum_
# {j = 0} ^ {P / 2} \binom
# {i + j}
# {i}
# O(T + P - i - 2j)∑
# i = 0
# T
# ​
# ∑
# j = 0
# P / 2
# ​
# (
#     i
# i + j
# ​
# )O(T + P−i−2j) 。通过本文以外的一些知识，我们可以证明它的时间复杂度为
# O\big((T + P)
# 2 ^ {T + \frac
# {P}
# {2}}\big)O((T + P)
# 2
# T +
# 2
# P
# ​
#
# ) 。
#
# 空间复杂度：对于
# match
# 函数的每一次调用，我们都会产生如上所述的字符串，可能还会产生重复的字符串。如果内存没有被重复利用，那么即使只有总量为
# O(T ^ 2 + P ^ 2)
# O(T
# 2
# + P
# 2
# ) 个不同的后缀，也会花费总共
# O\big((T + P)
# 2 ^ {T + \frac
# {P}
# {2}}\big)O((T + P)
# 2
# T +
# 2
# P
# ​
#
# ) 的空间。
#
# 方法
# 2: 动态规划
# 想法
#
# 因为题目拥有
# 最优子结构 ，一个自然的想法是将中间结果保存起来。我们通过用 \text
# {dp(i, j)}
# dp(i, j)
# 表示 \text
# {text[i:]}
# text[i:]
# 和 \text
# {pattern[j:]}
# pattern[j:]
# 是否能匹配。我们可以用更短的字符串匹配问题来表示原本的问题。
#
# 算法
#
# 我们用[方法
# 1] 中同样的回溯方法，除此之外，因为函数
# match(text[i:], pattern[j:])
# 只会被调用一次，我们用 \text
# {dp(i, j)}
# dp(i, j) 来应对剩余相同参数的函数调用，这帮助我们节省了字符串建立操作所需要的时间，也让我们可以将中间结果进行保存。
#
# 自顶向下的方法
#
# JavaPython
#
#
# class Solution(object):
#     def isMatch(self, text, pattern):
#         memo = {}
#
#         def dp(i, j):
#             if (i, j) not in memo:
#                 if j == len(pattern):
#                     ans = i == len(text)
#                 else:
#                     first_match = i < len(text) and pattern[j] in {text[i], '.'}
#                     if j + 1 < len(pattern) and pattern[j + 1] == '*':
#                         ans = dp(i, j + 2) or first_match and dp(i + 1, j)
#                     else:
#                         ans = first_match and dp(i + 1, j + 1)
#
#                 memo[i, j] = ans
#             return memo[i, j]
#
#         return dp(0, 0)
#
#
# 自底向上的方法
#
# JavaPython
#
#
# class Solution(object):
#     def isMatch(self, text, pattern):
#         dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
#
#         dp[-1][-1] = True
#         for i in range(len(text), -1, -1):
#             for j in range(len(pattern) - 1, -1, -1):
#                 first_match = i < len(text) and pattern[j] in {text[i], '.'}
#                 if j + 1 < len(pattern) and pattern[j + 1] == '*':
#                     dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
#                 else:
#                     dp[i][j] = first_match and dp[i + 1][j + 1]
#
#         return dp[0][0]
#
#
# 复杂度分析
#
# 时间复杂度：用
# TT
# 和
# PP
# 分别表示匹配串和模式串的长度。对于i = 0, ..., Ti = 0, ..., T
# 和
# j = 0, ..., Pj = 0, ..., P
# 每一个
# dp(i, j)
# 只会被计算一次，所以后面每次调用都是
# O(1)
# O(1)
# 的时间。因此，总时间复杂度为
# O(TP)
# O(TP) 。
#
# 空间复杂度：我们用到的空间仅有
# O(TP)
# O(TP)
# 个
# boolean
# 类型的缓存变量。所以，空间复杂度为
# O(TP)
# O(TP) 。



class Solution(object):
    def match(self, text, pattern):
        if not pattern: return not text
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        return first_match and self.match(text[1:], pattern[1:])

    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


class Solution2(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == '__main__':
    sol = Solution2()
    text = "aabb"
    pattern = "ab"
    judge = sol.isMatch(text, pattern)
    print(judge)
    gg =0
