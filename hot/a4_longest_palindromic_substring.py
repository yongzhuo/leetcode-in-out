# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/9/4 19:59
# @author   :Mo
# @function :最长回文子串(longest Palindrome)


# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
# 输入: "cbbd"
# 输出: "bb"
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 中心扩散
class Solution1:
    def longestPalindrome(self, s):
        size = len(s)
        if size == 0:
            return ''

        # 至少是 1
        longest_palindrome = 1
        longest_palindrome_str = s[0]

        for i in range(size):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)

            # 当前找到的最长回文子串
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > longest_palindrome:
                longest_palindrome = len(cur_max_sub)
                longest_palindrome_str = cur_max_sub

        return longest_palindrome_str

    def __center_spread(self, s, size, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """
        l = left
        r = right

        while l >= 0 and r < size and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r], r - l - 1


# 动态规划-状态转移矩阵
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s
        # 二维 dp 问题
        # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
        # 设置为 None 是为了方便调试，看清楚代码执行流程
        dp = [[False for _ in range(size)] for _ in range(size)]

        longest_l = 1
        res = s[0]

        # 因为只有 1 个字符的情况在最开始做了判断
        # 左边界一定要比右边界小，因此右边界从 1 开始
        for r in range(1, size):
            for l in range(r):
                # 状态转移方程：如果头尾字符相等并且中间也是回文
                # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
                # 否则要继续看收缩以后的区间的回文性
                # 重点理解 or 的短路性质在这里的作用
                judge_l_r = (s[l] == s[r])
                judge_r_l = (r - l <= 2)
                judge_dp = dp[l + 1][r - 1] # 只有一个的情况
                if judge_l_r and (judge_r_l or judge_dp):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[l:r + 1]
            # # 调试语句
            # for item in dp:
            #     print(item)
            # print('---')
        return res


if __name__ == '__main__':
    text = "bb大b大a大b大aa" # "abacdfgdcaba"
    sl = Solution()
    longest_palindrome = sl.longestPalindrome(text)
    print(longest_palindrome)


    # import tensorflow as tf
    # tfe = tf.contrib.eager
    # tfe.enable_eager_execution()
    #
    # input_arg = tf.ones([1, 3, 3, 5])
    # filter_arg = tf.ones([1, 1, 5, 1])
    # op = tf.contrib.slim.conv2d(input_arg, filter_arg, stride=1, padding='VALID')
    #
    # print(op)
