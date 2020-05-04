# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/3/9 19:09
# @author  : Mo
# @function:


"""
31. 下一个排列
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
通过次数46,624提交次数141,663
"""

"""31. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""




class Solution:
    # 从最后一位开始寻找这位后面比它还小的数字,交换这两个数字,然后把剩下的元素排序.
    # 有点儿问题
    def nextPermutationmy(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        for i in range(len_nums-1, 0, -1):
            if nums[i] > nums[i-1]:
                if i == 1 and nums[i-1]==max(nums):
                    nums.reverse()
                else:
                    j = len_nums - 1
                    while j > i and nums[i] < nums[j]:
                        j -= 1
                    temp = nums[i-1]
                    nums[i-1] = nums[i]
                    nums[i] = temp
                    re = nums[i:].sort()
                    for h in range(len(re)):
                        nums[len_nums - 1 - h] = re[h]
                break
    """下一个排列
问题描述
这道题是 LeetCode 31题。

“下一个排列”的定义是：给定数字序列的字典序中下一个更大的排列。如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

我们可以将该问题形式化地描述为：给定若干个数字，将其组合为一个整数。如何将这些数字重新排列，以得到下一个更大的整数。如 123 下一个更大的数为 132。如果没有更大的整数，则输出最小的整数。

以 1,2,3,4,5,6 为例，其排列依次为：

123456
123465
123546
...
654321
可以看到有这样的关系：123456 < 123465 < 123546 < ... < 54321。

算法推导
如何得到这样的排列顺序？这是本文的重点。我们可以这样来分析：

我们希望下一个数比当前数大，这样才满足“下一个排列”的定义。因此只需要将后面的大数与前面的小数交换，就能得到一个更大的数。比如 123456，将 5 和 6 交换就能得到一个更大的数 123465。
我们还希望下一个数增加的幅度尽可能的小，这样才满足“下一个排列与当前排列紧邻“的要求。为了满足这个要求，我们需要：
在尽可能靠右的低位进行交换，需要从后向前查找
将一个尽可能小的大数与前面的小数交换。比如 123465，下一个排列应该把 5 和 4 交换而不是把 6 和 4 交换
将大数换到前面后，需要将大数后面的所有数重置为升序，升序排列就是最小的排列。以 123465 为例：首先按照上一步，交换 5 和 4，得到 123564；然后需要将 5 之后的数重置为升序，得到 123546。显然 123546 比 123564 更小，123546 就是 123465 的下一个排列
以上就是求“下一个排列”的分析过程。

算法过程
标准的“下一个排列”算法可以描述为：

从后向前查找第一个相邻升序的元素对 (i,j)，满足 A[i] < A[j]。此时 [j,end) 必然是降序
在 [j,end) 从后向前查找第一个满足 A[i] < A[k] 的 k。A[i]、A[k] 分别就是上文所说的“小数”、“大数”
将 A[i] 与 A[k] 交换
可以断定这时 [j,end) 必然是降序，逆置 [j,end)，使其升序
如果在步骤 1 找不到符合的相邻元素对，说明当前 [begin,end) 为一个降序顺序，则直接跳到步骤 4
该方法支持数据重复，且在 C++ STL 中被采用。

作者：imageslr
链接：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        答题思路：从后往前寻找第一个升序对(i,j)即nums[i]<nums[j] 再从后往前找第一个大于nums[i]的数即为大数，交换着两个元素即将大数换到前面，然后将大数后面的部分倒序
        """
        n = len(nums)
        if n < 2: return nums
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:  # 要是前者大于等于后者 则不是要调整的目标 继续前移  ！第一遍出错就是这儿没有等于
            i -= 1
        if i == 0 and nums[i] == max(nums):  # 此数为最大数
            return nums.reverse()
        else:  # 151    i=1
            j = n - 1
            while j > i - 1 and nums[j] <= nums[i - 1]:
                j -= 1
            temp = nums[i - 1]  # i-1为小数  j为大数 交换之
            nums[i - 1] = nums[j]
            nums[j] = temp
            re = nums[i:]
            for h in range(len(re)):
                nums[n - 1 - h] = re[h]
            return nums


if __name__ == '__main__':
    sol = Solution()
    nums = [2,1,3,4,5,6]
    sol.nextPermutation(nums)
    print(nums)







