# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2019/12/31 19:12
# @author  : Mo
# @function: 12. 整数转罗马数字



# 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
#
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
#
# 示例 1:
#
# 输入: 3
# 输出: "III"
# 示例 2:
#
# 输入: 4
# 输出: "IV"
# 示例 3:
#
# 输入: 9
# 输出: "IX"
# 示例 4:
#
# 输入: 58
# 输出: "LVIII"
# 解释: L = 50, V = 5, III = 3.
# 示例 5:
#
# 输入: 1994
# 输出: "MCMXCIV"
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/integer-to-roman
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def intToRoman1(self, num: int) -> str:
        """
            十进制数转罗马数字
        :param num: int, like 8868
        :return: str, like 'IV'
        """

        roman2int = {'I':1,
                     'V':5,
                     'X':10,
                     'L':50,
                     'C':100,
                     'D':500,
                     'M':1000}
        int2roman = {}
        enum_ = []
        for k,v in roman2int.items():
            int2roman[v] = k
            enum_.append(v)
        enum_.sort(reverse=True)
        mount_list = []
        for i in range(len(enum_)-1):
            if num == 0:
                break
            e = enum_[i]
            pre_e = enum_[i+1]
            mount = num // e
            if num+pre_e==e and mount == 0:
                num = num - e + 1
                mount_list.append(int2roman[pre_e] + int2roman[e])
            elif mount >= 1:
                num = num - e * mount
                mount_list.append(mount * int2roman[e])

        return "".join(mount_list)

    def intToRoman2(self, num: int) -> str:
        ge = num % 10
        shi = num//10%10
        bai = num//100%10
        qian = num//1000
        str_ge = self.judge(ge,"I","V","X")
        str_shi = self.judge(shi,"X","L","C")
        str_bai = self.judge(bai,"C","D","M")
        str_qian = self.judge(qian,rm1 = "M")
        return str_qian+str_bai+str_shi+str_ge

    def judge(self,num=0,rm1="",rm2="",rm3=""):
        if num<=3:
            return num*rm1
        elif num == 4:
            return rm1+rm2
        elif num<=8:
            return rm2+rm1*(num-5)
        else:
            return rm1+rm3

    def intToRoman(self, num: int) -> str:
        num_dict = {1: 'I',
                    4: 'IV',
                    5: 'V',
                    9: 'IX',
                    10: 'X',
                    40: 'XL',
                    50: 'L',
                    90: 'XC',
                    100: 'C',
                    400: 'CD',
                    500: 'D',
                    900: 'CM',
                    1000: 'M'}
        roman_dict = {}
        for k, v in num_dict.items():
            roman_dict[v] = k
        print(roman_dict)


        res = ""
        for key in sorted(num_dict.keys())[::-1]:
            if (num == 0):
                break
            tmp = num // key
            if (tmp == 0):
                continue
            res += num_dict[key] * (tmp)
            num -= key * (tmp)
        return res

if __name__ == '__main__':
    sol = Solution()
    num = 1994
    roman = sol.intToRoman(num)
    print(roman)
