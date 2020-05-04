# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/3/2 19:03
# @author  : Mo
# @function: 28. Implement strStr()


"""
28. 实现 strStr()
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

通过次数134,343提交次数339,548
"""
"""
28. Implement strStr()
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

通过次数134,343提交次数339,548
"""


class Solution:
    # 自己实现, 字典, 时间O(2(H-N)), 空间O(H+N+(H-N))
    def strStrmy(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        len_hay = len(haystack)
        len_range = len_hay-len_needle
        if len_range < 0:
            return -1
        # 所有haystack中等于needle长度的字符串
        dict_haystack = {}
        for i in range(len(haystack)-len_needle, -1, -1):
            dict_haystack[haystack[i:i+len_needle]] = i
        # 字典keys匹配
        if needle in dict_haystack:
            return dict_haystack[needle]
        else:
            return -1

    # Sunday 匹配机制与偏移表(筛除了这一步,如果下一个字符不在needle中, 则跳过len(needle)次), 最坏情况：O(nm)O(nm); 平均情况：O(n)O(n)
    def strStr_1(self, haystack: str, needle: str) -> int:

        # Func: 计算偏移表
        def calShiftMat(st):
            dic = {}
            for i in range(len(st) - 1, -1, -1):
                if not dic.get(st[i]):
                    dic[st[i]] = len(st) - i
            dic["ot"] = len(st) + 1
            return dic

        # 其他情况判断
        if len(needle) > len(haystack): return -1
        if needle == "": return 0

        # 偏移表预处理
        dic = calShiftMat(needle)
        idx = 0

        while idx + len(needle) <= len(haystack):

            # 待匹配字符串
            str_cut = haystack[idx:idx + len(needle)]

            # 判断是否匹配
            if str_cut == needle:
                return idx
            else:
                # 边界处理
                if idx + len(needle) >= len(haystack):
                    return -1
                # 不匹配情况下，根据下一个字符的偏移，移动idx
                cur_c = haystack[idx + len(needle)]
                if dic.get(cur_c):
                    idx += dic[cur_c]
                else:
                    idx += dic["ot"]

        return -1 if idx + len(needle) >= len(haystack) else idx

    # 双指针法
    def strStr_2(self, haystack, needle):
        i = 0
        if needle == "":
            return 0
        while i <= len(haystack) - len(needle):
            if haystack[i: i + len(needle)] == needle:
                return i
            i += 1
        return -1

    # 双指针O(m*n)超时，优化如下
    def strStr_3(self, haystack: str, needle: str) -> int:
        # 避免不必要的遍历
        if len(needle) == 0: return 0
        if len(needle) > len(haystack): return -1
        from collections import Counter
        haystack_dict = Counter(haystack)
        needle_dict = Counter(needle)
        for key in needle_dict:
            if key in haystack_dict and needle_dict[key] <= haystack_dict[key]:
                pass
            else:
                return -1
        # 避免 needle 太长
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    sol = Solution()
    haystack = "11vaa11qweaab"
    needle = "11q"
    res = sol.strStr_2(haystack, needle)
    print(res)



