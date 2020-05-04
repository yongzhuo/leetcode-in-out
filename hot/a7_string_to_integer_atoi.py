# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/9/6 19:58
# @author   :Mo
# @function :8.字符串转换整数 (atoi)

# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
#
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
#
# 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
#
# 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
#
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
#
# 在任何情况下，若函数不能进行有效的转换时，请返回 0。
#
# 说明：
#
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
#
# 示例 1:
#
# 输入: "42"
# 输出: 42
# 示例 2:
#
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
#      我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
# 示例 3:
#
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
# 示例 4:
#
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
#      因此无法执行有效的转换。
# 示例 5:
#
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
#      因此返回 INT_MIN (−231) 。

import re


class Solution1:
    def myAtoi(self, str: str) -> int:
        data = re.findall(r'\d+', str)
        if data:
            res = int(data[0])
            pos = str.index(data[0][0])
            if pos != 0:
                if str[pos-1] == "-":
                    res = -1 * res
        else:
            res = 0
        if -2 ** 31 > res:
            return -2 ** 31
        elif 2 ** 31 < res:
            return 2 ** 31
        else:
            return res


class Solution2:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)


class SolutionMy: #
    def __init__(self):
        self.max_add = 2 ** 31
        self.min_add = -2 ** 31

    def myAtoi(self, str: str) -> int:
        try:
            data_strs = str.replace(" ", "")# "".join(re.findall(r'[\w\-]', str))
            count = 0
            data_str = ""
            for ds in data_strs:
                if (count == 0 and (ds not in "-+0123456789")):
                    return 0
                elif count == 1 and ("+" == ds or "-" == ds):
                    return 0
                elif ds in "-+0123456789":
                    data_str += ds
                else:
                    break
                count += 1

            if (data_strs[0]=="+") and data_strs[1]=="0":
                return 0
            res = -1 * int(data_str[1:]) if data_str[0]=="-" else int(data_str)

            if self.min_add > res:
                return self.min_add
            elif self.max_add < res:
                return self.max_add
            else:
                return res
        except:
            return 0



if __name__ == '__main__':
    data = "000000000000001214235"
    sl = Solution1()
    i = sl.myAtoi(data)
    print(i)


"3.1415926"
"-+14325"
"   +0 123"
"   +12"
"   -12"
" 2  -12"
" ##2  -12"
"-"
"-91283472332"
"3.114"
"+-3"
