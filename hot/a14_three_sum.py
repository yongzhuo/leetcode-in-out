# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/1/2 19:08
# @author  : Mo
# @function: 15.三数之和


# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    # error
    def threeSume(self, num):
        res = []
        len_num = len(num)
        for i in range(len_num):
            for j in range(len_num):
                k = -(num[i] + num[j])
                if k in num:
                    index_k = num.index(k)
                    if i != j and j != index_k and i !=index_k:
                        res.append([k, num[i], num[j]])
        res_last = []
        for r in res:
            if not res_last:
                res_last.append(r)
            else:
                flag = 0
                for rr in res_last:
                    if r[0] in rr and r[1] in rr and r[2] in rr:
                        flag = 1
                if flag == 0:
                    res_last.append(r)

        return res_last

    # sort and then two point move
    def threeSum(self, nums):

        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res


if __name__ == '__main__':
    sol = Solution()
    num = [1,2,-2,-1] # [-1,0,1,2,-1,-4, 0, 0] # [1,2,3,4, -1,-2-3,-4,0]
    res = sol.threeSum(num)
    print(res)
