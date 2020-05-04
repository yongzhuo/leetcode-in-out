# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/3/3 19:26
# @author  : Mo
# @function:

"""
29. 两数相除
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
通过次数36,595提交次数189,223
"""
"""
29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
通过次数36,595提交次数189,223
"""

class Solution:
    # 报错,不成功
    def dividemy(self, dividend: int, divisor: int) -> int:
        i = 0
        quotient = 0
        if dividend == 0:
            return 0
        if dividend > 0 and divisor > 0:
            while dividend >= quotient:
                quotient += divisor
                i += 1
            i -= 1
        elif dividend > 0 and divisor < 0:
            while dividend >= -quotient:
                quotient += divisor
                i -= 1
            i += 1
        elif dividend < 0 and divisor < 0:
            while -dividend >= -quotient:
                quotient += divisor
                i += 1
            i -= 1
        elif dividend < 0 and divisor > 0:
            while -dividend >= quotient:
                quotient += divisor
                i -= 1
            i += 1
        else:
            i = 0

        return i
    # 位移1
    def divide_(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        # 把除数不断左移，直到它大于被除数
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                result += 1 << count  # 这里的移位运算是把二进制（第count+1位上的1）转换为十进制
                dividend -= divisor
        if sign: result = -result
        return result if -(1 << 31) <= result <= (1 << 31) - 1 else (1 << 31) - 1
    # 位移2
    def divide(self, divd: int, dior: int) -> int:
        res = 0
        sign = 1 if divd ^ dior >= 0 else -1
        divd = divd if divd > 0 else -divd
        dior = dior if dior > 0 else -dior
        while divd >= dior:
            tmp, i = dior, 1
            while divd >= tmp:
                divd -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        res = res * sign
        return min(max(-2 ** 31, res), 2 ** 31 - 1)

if __name__ == '__main__':
    sol = Solution()
    dividend = 10
    divisor = 2
    res = sol.divide(dividend, divisor)
    print(res)
    sr = 0




