# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2019/12/31 19:22
# @author  : Mo
# @function: 11.盛最多水得容器(坐标轴上梯形面积)


# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 说明：你不能倾斜容器，且 n 的值至少为 2。
#
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。
# 在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
# 示例:
#
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/container-with-most-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def maxArea(self, height):
        maxarea = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                maxarea = max(maxarea, min(height[i], height[j]) * (j - i))
        return maxarea

    def maxArea2(self, height):
        len_height = len(height)
        maxarea = 0
        l = 0
        r = len_height - 1
        while l < r:
            maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
            if (height[l] < height[r]):
                l+=1
            else:
                r-=1
        return maxarea



if __name__ == '__main__':
    sol = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    maxarea = sol.maxArea2(height)
    print(maxarea)
