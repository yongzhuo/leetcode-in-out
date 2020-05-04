# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/9/5 19:09
# @author   :Mo
# @function : Z 字形变换(zigzag conversion)


import numpy as np


# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
# 请你实现这个将字符串进行指定行数变换的函数：
# string convert(string s, int numRows);
# 示例 1:
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 示例 2:
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zigzag-conversion
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 方案一, 顺序思维
#    利用先垂直方向后水平方向的思路展开,
#    range从大到小循环get到了【range(numRows-2, 0, -1)】
class Solution0:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ""
        if numRows == 1:return s
        s_Rows = [""] * numRows
        i  = 0
        n = len(s)
        while i < n:
            for j in range(numRows):
                if i < n:
                    s_Rows[j] += s[i]
                    i += 1
            for j in range(numRows-2,0,-1):
                if i < n:
                    s_Rows[j] += s[i]
                    i += 1
        return "".join(s_Rows)


# 方案二, 还是顺序思维
#    与方案一不同, i%(numRows-1)判断是向下还是向上,godown
class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        cache = [[] for i in range(numRows)]   # create numRows empty lists
        if numRows==1:
            return s
        godown = False                       # set godown flag
        for i,string in enumerate(s):
            j = i%(numRows-1)                # every numRows element change down or up
            if j == 0:
                godown = ~godown
            if godown:
                cache[j].append(string)
            else:
                cache[numRows - 1 - j].append(string)
        cache = [''.join(cache[i]) for i in range(numRows)]
        return ''.join(cache)


# 方案三, 规律穷举法
#     垂直水平变幻用的还是 IndexCol%(numRows-1)
#     根据数据组建N的规律, 用一个数组保存, 还可以打出完整的Z字形变幻
class Solution11:
    def convert(self, s, numRows):
            if numRows <= 1:
                return s
            DecArray = self.getArray(s, numRows)
            print(DecArray)
            result = ''.join(DecArray.flatten())
            result = result.replace('-', '')
            return result

    # 构建Z型数组法获得相关数组
    def getArray(self, s, numRows):
            DecArray = np.array([['-'] * len(s)] * numRows)
            ArrayIndex = 0
            IndexCol = 0
            while ArrayIndex < len(s):
                if IndexCol % (numRows - 1) == 0:
                    line = ArrayIndex - (2 * numRows - 2) * int(IndexCol / (numRows - 1))
                    if line < numRows:
                        DecArray[line][IndexCol] = s[ArrayIndex]
                    else:
                        IndexCol += 1
                        ArrayIndex -= 1
                else:
                    sum = int(IndexCol / (numRows - 1) + 1) * (numRows - 1)
                    line = sum - IndexCol
                    DecArray[line][IndexCol] = s[ArrayIndex]
                    IndexCol += 1
                ArrayIndex += 1
            return DecArray


# 方案四, 同方案一、二
#    不同的是, 用字典保存数据,
# 垂直-水平判断(curRow == numRows - 1); curRow += 1 if goingDown else -1
class Solution12:
    def convert(self, s, numRows):
        if numRows <= 1:
            return s
        DecDict = self.getArray(s, numRows)
        print(DecDict)
        rows = min(len(s), numRows)
        ListStr = []
        for line in range(rows):
            ListStr.extend(DecDict[line])
        return ''.join(ListStr)

    # 按行排序法获得相关数组
    def getArray(self, s, numRows):
        rows = min(len(s), numRows)
        DecDict = {}
        for row in range(rows):
            DecDict[row] = []
        curRow = 0
        goingDown = False
        for index in range(len(s)):
            DecDict[curRow].extend(s[index])
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1
        return DecDict


if __name__ == '__main__':
    text = "ajvfqjjwnbwiogeb2poerob2w"
    sl = Solution1()
    slc = sl.convert(text, 6)
    print(slc)
