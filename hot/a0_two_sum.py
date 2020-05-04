# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/8/20 23:44
# @author   :Mo
# @function :两数之和(two sum)(NP问题, list中两数之和为一定值)


# 1.两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 暴力法
class Solution1:
    def twoSum(self, nums, target):
        lens = len(nums)
        j = -1
        for i in range(lens):
            if (target - nums[i]) in nums:
                if (nums.count(target - nums[i]) == 1) & (
                        target - nums[i] == nums[i]):  # 如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
                    continue
                else:
                    j = nums.index(target - nums[i], i + 1)  # index(x,i+1)是从num1后的序列后找num2
                    break
        if j > 0:
            return [i, j]
        else:
            return []


class Solution12: # 暴力法, num1
    def twoSum(self, nums, target):
        lens = len(nums)
        j = -1
        for i in range(1, lens):
            temp = nums[:i]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                break
        if j >= 0:
            return [j, i]


class Solution2: # 用字典模拟哈希求解, 字典记录了num1和num2的值和位置，而省了再查找num2索引的步骤
    def twoSum(self, nums, target):
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]


# 奇怪,if else还比快 if ; ...
# 无论在不在里面都可以，如果不在就是减去后边的，因为num作为分隔符始终会分割两个加数，{}
class Solution21: # 用字典模拟哈希求解, 字典记录了num1和num2的值和位置，而省了再查找num2索引的步骤
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            # j = hashmap.get(target - num)
            # if j is not None:
            #     return [i, j]
            # hashmap[num] = i  # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况
            res = target - num
            if res in hashmap:
                return [hashmap[res], i]
            else:
                hashmap[num] = i


class Solution3: # 极快, 11s
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        keys = {}
        for i, v in enumerate(nums):
            if target-v in keys:
                return [keys[target-v],i]
            else:
                keys[v] = i
        return None


class Solution6:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        keys = {}
        for i, v in enumerate(nums):
            if target-v in keys:
                return [keys[target-v],i]
            else:
                keys[v] = i
        return None


class Solution01: # 暴力法
    def twoSum(self, nums, target):
         len_nums = len(nums)
         for i in range(len_nums):
             for j in range(len_nums):
                 if i != j:
                     nums_sum = nums[i] + nums[j]
                     if nums_sum == target:
                         return [i, j]


class Solution02: # 20s
    def twoSum(self, nums, target):
         result = {}
         for index, num in enumerate(nums):
             result[num] = index
         for i, num in enumerate(nums):
             j = result.get(target - num)
             if j is not None and i != j:
                 return [i, j]


if __name__=="__main__":
    # 如果要打全部, 将rerturn转化为print就好
    import time
    l1 = [12, 18, 77, 7, 2, 2, 17, 11, 15, 19]
    l2 = 9
    time_start = time.time()
    for i in range(1):
        so = Solution21()
        res = so.twoSum(l1, l2)
        print(res)
    print(time.time()-time_start)
    # print(l1)
    # print(l2)

