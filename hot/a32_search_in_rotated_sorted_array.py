# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/3/16 21:21
# @author  : Mo
# @function: 33. 搜索旋转排序数组(33. Search in Rotated Sorted Array)


"""33. 搜索旋转排序数组
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
通过次数83,958提交次数230,145"""
"""33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
通过次数83,958提交次数230,145
"""


def binner_find(lst, value):
    """二分查找"""
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[0] < lst[-1]:
            if lst[mid] > value:
                end = mid - 1
            elif lst[mid] < value:
                start = mid + 1
            else:
                return mid
        else:
            if lst[mid] < value:
                end = mid - 1
            elif lst[mid] > value:
                start = mid + 1
            else:
                return mid

    return -1


L = [3, 6, 12, 17, 25, 32, 43, 55, 68]
# print(binner_find(L, 43))


class Solution:
    # 失败, 二分查找, 有顺序
    def searchmy(self, nums, target):
        i = 0
        j = len(nums)
        while i <= j:
            mid = (i+j)//2
            if nums[mid] > target:
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                return mid
        return -1

    """方法思路：
        1.根据首尾判断是否旋转
        2.若未旋转，直接二分查找（注意：可以直接判断target是否在首尾之内，否则直接返回-1）
        3.若旋转，先找旋转点（以找到最大值为例）
        （1）情况一：target在[0,index_max]之内：此范围二分查找
        （2）情况二：target在[index_max+1,len(nums)-1]之内：此范围二分查找
        （3）情况三：若不在以上两种情况则直接返回-1"""
    def search1(self, nums, target):
        if len(nums) < 1: return -1
        # 二分查找
        def two_find(m, n):
            if m > n: return -1
            mid = (m + n) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return two_find(m, mid - 1)
            else:
                return two_find(mid + 1, n)

        # 找旋转点，返回最大值处
        def find_max(m, n):
            mid = (m + n) // 2
            if nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] >= nums[0]:
                return find_max(mid + 1, n)
            else:
                return find_max(m, mid - 1)

        if nums[0] <= nums[-1]:  # 如果数组没有旋转!("="是为了在nums长度为1时也能算进此)
            if target >= nums[0] and target <= nums[-1]:
                return two_find(0, len(nums) - 1)
            else:
                return -1
        else:
            index_max = find_max(0, len(nums) - 1)
            if target >= nums[0] and target <= nums[index_max]:
                return two_find(0, index_max)
            elif target >= nums[index_max + 1] and target <= nums[len(nums) - 1]:
                return two_find(index_max + 1, len(nums) - 1)
            else:
                return -1

    """注意到原数组为有限制的有序数组（除了在某个点会突然下降外均为升序数组）

if nums[0] <= nums[I] 那么 nums[0] 到 nums[i] 为有序数组,那么当 nums[0] <= target <= nums[i] 时我们应该在 0-i0−i 范围内查找；

if nums[i] < nums[0] 那么在 0-i0−i 区间的某个点处发生了下降（旋转），那么 I+1I+1 到最后一个数字的区间为有序数组，并且所有的数字都是小于 nums[0] 且大于 nums[i]，当target不属于 nums[0] 到 nums[i] 时（target <= nums[i] < nums[0] or nums[i] < nums[0] <= target），我们应该在 0-i0−i 区间内查找。
上述三种情况可以总结如下：

    nums[0] <= target <= nums[i]
               target <= nums[i] < nums[0]
                         nums[i] < nums[0] <= target
所以我们进行三项判断：

(nums[0] <= target)， (target <= nums[i]) ，(nums[i] < nums[0])，现在我们想知道这三项中有哪两项为真（明显这三项不可能均为真或均为假（因为这三项可能已经包含了所有情况））

所以我们现在只需要区别出这三项中有两项为真还是只有一项为真。

使用 “异或” 操作可以轻松的得到上述结果（两项为真时异或结果为假，一项为真时异或结果为真，可以画真值表进行验证）

之后我们通过二分查找不断做小 target 可能位于的区间直到 low==high，此时如果 nums[low]==target 则找到了，如果不等则说明该数组里没有此项。

作者：LukeLee
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/ji-jian-solution-by-lukelee/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""
    def search2(self, nums, target):
        low = 0
        high = len(nums)-1
        while low<high:
            mid = (low+high)//2
            # 异或, 一真时候才真, 两真则为假, 不存在3真或3假
            if (nums[0]>target) ^ (nums[0]>nums[mid]) ^ (target>nums[mid]):
                low = mid + 1
            else:
                high = mid
        return low if low==high and nums[low]==target else -1


if __name__ == '__main__':
    sol = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    res = sol.search2(nums, target)
    print(res)
    gg = 0





