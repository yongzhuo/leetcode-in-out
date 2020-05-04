# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/8/22 23:12
# @author   :Mo
# @function :无重复字符的最长子串(longest substring without repeating characters)


# 无重复字符得最长子串
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 示例 1:
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 解题思路
# 这道题主要用到思路是：滑动窗口
# 什么是滑动窗口？
# 其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！
# 如何移动？
# 我们只要把队列的左边的元素移出就行了，直到满足题目要求！
# 一直维持这样的队列，找出队列出现最长的长度时候，求出解！
# 时间复杂度：O(n)


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_left = 0
        len_cur = 0
        len_max = 0
        lookup_set = set()
        num = len(s)
        for i in range(num):
            len_cur += 1
            while s[i] in lookup_set:
                lookup_set.remove(s[str_left])
                len_cur -= 1
                str_left += 1
            if len_cur > len_max: len_max = len_cur
            lookup_set.add(s[i])
        return len_max


if __name__ == '__main__':
    sen = "abcdefghab"
    s1 = Solution()
    s1o = s1.lengthOfLongestSubstring(sen)
    print(s1o)

