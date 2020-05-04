# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/3/20 19:19
# @author  : Mo
# @function: 35. 搜索插入位置


"""35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
通过次数131,879提交次数290,836"""

"""35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
通过次数131,879提交次数290,836"""


from typing import List


class Solution:
    """暴力法"""
    def searchInsertmy(self, nums, target):
        if not nums:
            return False
        len_nums = len(nums)
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len_nums
        res = None
        for i in range(len_nums-1):
            if target>nums[i]:
                if target<=nums[i+1]:
                    res = i + 1
                    break
        if not res:
            return len_nums
        return res
    """排除法(减治思想), 两个角度(目标值,哪些不是目标值);
    收缩边界: [left, mid]|[mid + 1, right], [left, mid - 1]|[mid, right];
    边界取值: mid = left + (right - left) / 2   取代   mid = (left + right) / 2
    首先，插入位置有可能在数组的末尾（题目中的示例 3），需要单独判断；
其次，如果待插入元素比最后一个元素严格小，并且在这个数组中有和插入元素一样的元素，返回任意一个位置即可；
否则，插入的位置应该是严格大于 target 的第 1 个元素的位置。
因此，严格小于 target 的元素一定不是解，根据这个思路，可以写出如下代码。"""
    def searchInsert2(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size == 0:
            return 0

        # 特判
        if nums[size - 1] < target:
            return size

        left = 0
        right = size - 1

        while left < right:
            mid = left + (right - left) // 2
            # 严格小于 target 的元素一定不是解
            if nums[mid] < target:
                # 下一轮搜索区间是 [mid + 1, right]
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,5,6]
    target = 7
    res = sol.searchInsert2(nums, target)
    print(res)
    gg = 0




