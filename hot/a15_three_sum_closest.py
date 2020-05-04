# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/1/3 19:20
# @author  : Mo
# @function: 16.最接近三数之和


# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum-closest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    # 双指针法, error 不能删除重复的数据
    def threeSumClosestmy(self, nums, target):
        num_target = [target-num if target-num>0 else num-target for num in nums]
        num_target_copy = num_target.copy() # copy.deepcopy(num_target)
        num_target_copy.sort()
        num_target_top3 = num_target_copy[0:3]
        idxs = []
        for ntt in num_target_top3:
            idx = num_target.index(ntt)
            idxs.append(idx)
        res = 0
        for idxs_one in idxs:
            res += nums[idxs_one]
        return res

    # 双指针法
    def threeSumClosest(self, nums, target):
        n = len(nums)
        if (not nums or n < 3):
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


if __name__ == '__main__':
    sol = Solution()
    strs = [1,1,-1] # ["dog","racecar","car"]
    target = -100
    res = sol.threeSumClosest(strs, target)
    print(res)
    gg = 0

