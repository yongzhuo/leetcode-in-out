# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/1/2 19:01
# @author  : Mo
# @function: 14.最长公共前缀


# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-common-prefix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    # 水平扫描, 行
    # 复杂度分析:
    # 时间复杂度：O(S)是所有字符串中字符数量的总和。
    # 最坏的情况下，nn个字符串都是相同的。
    # 空间复杂度：O(1)
    def longestCommonPrefix(self, strs):
        """
            几个字符串的公共前缀
        :param strs: list, like ["flower","flow","flight"]
        :return: str, like "fl"
        """
        len_strs = len(strs)
        if len_strs == 0: return ""
        prefix = strs[0]
        for i in range(len_strs):
            while not strs[i].startswith(prefix):
                prefix = prefix[0: len(prefix)-1]
                if not prefix:return ""
        return prefix
    # 水平扫描, 列
    # 时间复杂度：O(S)
    # 但是最好的情况下n * minLenn∗minLen次比较，其中minLenminLen是数组中最短字符串的长度。
    # 空间复杂度：O(1)
    def longestCommonPrefix2(self, strs):
        """
            几个字符串的公共前缀
        :param strs: list, like ["flower","flow","flight"]
        :return: str, like "fl"
        """
        len_strs = len(strs)
        if len_strs == 0 or not strs: return ""
        for i in range(len(strs[0])):
            str_0_i = strs[0][i]
            for j in range(len_strs):
                if i == len(strs[j]) or strs[j][i] != str_0_i:
                    return strs[0][0:i]
        return strs[0]
    # 水平扫描, 二分查找
    # 时间复杂度：O(S)
    # 但是最好的情况下n * minLenn∗minLen次比较，其中minLenminLen是数组中最短字符串的长度。
    # 空间复杂度：O(1)
    def longestCommonPrefix3(self, strs):
        """
            几个字符串的公共前缀
        :param strs: list, like ["flower","flow","flight"]
        :return: str, like "fl"
        """
        def is_common_prefix(strs, middle):
            str_c = strs[0][0:middle]
            for str in strs:
                if not str.startswith(str_c):
                    return False
            return True


        if not strs: return ""
        len_strs = len(strs)
        if len_strs == 0: return ""
        len_min = len("".join(strs))
        for str in strs:
            len_min = min(len(str), len_min)
        high, low = len_min, 1
        while low < high:
            middle = int((high+low)/2)
            if is_common_prefix(strs, middle):
                low = middle + 1
            else:
                high = middle - 1
        return strs[0][0:int((high+low)/2)]



if __name__ == '__main__':
    sol = Solution()
    strs = ["flower","flow","floight"] # ["dog","racecar","car"]
    res = sol.longestCommonPrefix3(strs)
    print(res)

