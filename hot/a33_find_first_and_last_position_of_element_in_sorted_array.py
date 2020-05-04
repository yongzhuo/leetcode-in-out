# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/3/20 20:04
# @author  : Mo
# @function: 34. 在排序数组中查找元素的第一个和最后一个位置(34. Find First and Last Position of Element in Sorted Array)


"""34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
通过次数72,708提交次数185,363"""

"""34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
通过次数72,708提交次数185,363"""


class Solution:
    """思路,二分查找保证logN，然后再向前-向后查找相同的数字"""
    def searchRangemy(self, nums, target):
        i = 0
        j = len(nums)
        if len(nums)<1: return [-1, -1]
        if nums[0]>target or nums[-1]<target: return [-1, -1]
        start_end = []
        mid_i = -1
        # 二分查找
        while i <= j:
            mid = (i+j)//2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] == target:
                start_end.append(mid)
                mid_i = mid
                break
            else:
                j = mid - 1
        # 向前,向后查找相同的
        if mid_i !=-1:
            for k in range(mid_i-1, -1, -1):
                if nums[k] == nums[mid_i]:
                    start_end.append(k)
                else:
                    break
            for k in range(mid_i+1, len(nums)):
                if nums[k] == nums[mid_i]:
                    start_end.append(k)
                else:
                    break
        if not start_end:
            return [-1, -1]
        start_end.sort()
        start_end = start_end*2 if len(start_end)==1 else [start_end[0], start_end[-1]]

        return start_end

    """二分查找两次,找到最左边和最右边的数据list, 用一个left哨兵确认就可以了"""
    def searchRange1(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] > target or (left and target == nums[mid]):
                    hi = mid
                else:
                    lo = mid + 1
            return lo


if __name__ == '__main__':
    sol = Solution()
    nums = [5,7,7,7, 8,8,10]
    target = 7
    res = sol.searchRange1(nums, target)
    print(res)
    gg = 0









