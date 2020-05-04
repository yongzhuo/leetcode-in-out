# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/1/6 19:12
# @author  : Mo
# @function: 18.四数之和


class Solution:
    # sort and then two point move
    def fourSum1(self, nums, target):
        n = len(nums)
        if (not nums or n < 4):
            return None
        nums.sort()
        res = float("inf")
        for i in range(n):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                cur_sum = nums[i] + nums[L] + nums[R]
                if (cur_sum == target):
                    return target
                if (abs(cur_sum - target) < abs(res - target)):
                    res = cur_sum
                if (cur_sum - target < 0):
                    L += 1
                else:
                    R -= 1
        return res
    # 先排序后, 双指针法
    def fourSum(self, nums, target):
        n = len(nums)
        if n < 4: return []
        nums.sort()
        res = []
        for i in range(n - 3):
            # 防止重复 数组进入 res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 当数组最小值和都大于target 跳出
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # 当数组最大值和都小于target,说明i这个数还是太小,遍历下一个
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue
            for j in range(i + 1, n - 2):
                # 防止重复 数组进入 res
                if j - i > 1 and nums[j] == nums[j - 1]:
                    continue
                # 同理
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                # 同理
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue
                # 双指针
                left = j + 1
                right = n - 1
                while left < right:
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif tmp > target:
                        right -= 1
                    else:
                        left += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    num = [1, 2, -2, -1, 0, 2, 13, -13, -12] # [-1,0,1,2,-1,-4, 0, 0] # [1,2,3,4, -1,-2-3,-4,0]
    target = 0
    res = sol.fourSum(num, target)
    print(res)