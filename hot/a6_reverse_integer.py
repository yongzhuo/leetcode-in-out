# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/9/6 19:42
# @author   :Mo
# @function :6.整数反转(Reverse Integer)


# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 示例 1:
# 输入: 123
# 输出: 321
#  示例 2:
# 输入: -123
# 输出: -321
# 示例 3:
# 输入: 120
# 输出: 21
# 注意:
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。




# 弹出和推入数字 & 溢出前进行检查
class Solution11(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_list = list(str(x))
        res_stack = []
        is_minus = False  # 用于处理负数

        while x_list:
            v = x_list.pop()
            if v == '-':
                is_minus = True
                continue
            res_stack.append(v)
        res = int(''.join(res_stack))

        if is_minus:
            res *= -1

        # 边界条件
        v_max = 0xffffffff / 2
        if res > (v_max - 1) or res < (v_max * (-1)):
            res = 0

        return res


class Solution12(object):
    # 本题的思路就是先判断给定整数x的正负情况，把符号首先给提取出来
    # 然后将abs(x)变成字符串，接着将字符串反转，最后恢复成整数
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 定义用来标记给定整数x的正负情况，若x>=0， 则flag=1；反之，则flag=-1
        flag = 1 if x >= 0 else -1
        abs_x = abs(x)
        # 将abs(x)变成字符串
        x_str = str(abs_x)
        # 将字符串x_str反转
        reverse_x_str = x_str[::-1]
        # 最后恢复成整数
        reverse_x_int = int(reverse_x_str) * flag
        if -2 ** 31 <= reverse_x_int <= 2**31 - 1:
            return reverse_x_int
        else:
            return 0


class Solution13(object):
    def reverse(self, x: int) -> int:
        y, res = abs(x), 0
        of = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > of: return 0
            y //= 10
        return res if x > 0 else -res


if __name__ == '__main__':
    sl = Solution11()
    slr = sl.reverse(12332543608979878965)
    print(slr)



