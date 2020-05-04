# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/3/2 19:25
# @author  : Mo
# @function: 26. 删除排序数组中的重复项

"""
26. 删除排序数组中的重复项
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
通过次数255,751提交次数524,351

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
通过次数255,751提交次数524,351

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 自己的, 引入了其他list,不对
    def removeDuplicates(self, nums):
        num_o = []
        for num in nums:
            if num not in num_o:
                num_o.append(num)
        len_num_o = len(num_o)
        for i in range(len_num_o):
            nums[i] = num_o[i]
        # for j in range(len_num_o, len(nums)):
        return len_num_o
    # soft后删除的
    def removeDuplicates2(self, nums):
        for i in range(len(nums))[::-1]:
            if i - 1 != -1:
                if nums[i - 1] == nums[i]:
                    del nums[i]
        return len(nums)

    def removeDuplicates3(self, nums):
        if not nums:
            return False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                i -= 1
        return len(nums)
    # 双指针
    def removeDuplicates4(self, nums):
        flag = 0  # 定义一个指针变量
        for num in nums:  # 遍历数组
            if nums[flag] != num:  # 若指针指向的元素与当前遍历数组的元素不同
                flag += 1  # 指针后移一位
                nums[flag] = num  # 修改数组，将不同的元素占用重复元素的位置
                # 若相同则指针不动，数组继续往后遍历
        # 注意考虑数组为空的情况（flag初始值为0，由于要求数组长度，故需要加1）
        return len(nums) and flag + 1


if __name__ == '__main__':
    sol = Solution()
    num1 = [1,2,3,4]
    res = sol.removeDuplicates4(num1)
    print(res)





