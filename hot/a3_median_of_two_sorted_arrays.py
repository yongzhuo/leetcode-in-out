# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/9/4 19:48
# @author   :Mo
# @function :4.寻找两个有序数组的中位数(median of two sorted arrays)


# 奇数个数的中位数是它的中间数，偶数个数的中位数是它中间两位数的均值


# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 你可以假设 nums1 和 nums2 不会同时为空。
# 示例 1:
# nums1 = [1, 3]
# nums2 = [2]
# 则中位数是 2.0
# 示例 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# 则中位数是 (2 + 3)/2 = 2.5
# 在真实的面试中遇到过这道题？


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1 and not nums2:
            return 0
        if not nums1 or not nums2:
            res = nums1 + nums2
        def merge(a, b):
            c = []
            h = j = 0
            while j < len(a) and h < len(b):
                if a[j] < b[h]:
                    c.append(a[j])
                    j += 1
                else:
                    c.append(b[h])
                    h += 1

            if j == len(a):
                for i in b[h:]:
                    c.append(i)
            else:
                for i in a[j:]:
                    c.append(i)

            return c

        def merge_sort(lists):
            if len(lists) <= 1:
                return lists
            middle = int(len(lists) / 2)
            left = merge_sort(lists[:middle])
            right = merge_sort(lists[middle:])
            return merge(left, right)

        listss = nums1 + nums2
        res = merge_sort(listss)
        len_res = int(len(res)/2)
        if len(res) > 2 and len(res)%2==0:
            res_ = (res[len_res] + res[len_res - 1])/2
        elif len(res) > 2 and len(res)%2!=0:
            res_ = res[len_res]
        elif len(res) > 1:
            res_ = (res[0] + res[1])/2
        else:
            res_ = res[0]
        return res_


# 归并排序, java改python版本
class Solution2:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        nums3 = [0] * (len1 + len2)
        i = j = k = 0
        while (i < len1 and j < len2): # 处理完其中一个list(nums1或者nums2), 既一个list分完
            if (nums1[i] < nums2[j]):
                nums3[k] = nums1[i]
                i = i + 1
            else:
                nums3[k] = nums2[j]
                j = j + 1
            k = k + 1

        while (i < len1): # 如果nums1中的大数比nums2多
            nums3[k] = nums1[i]
            k = k + 1
            i = i + 1

        while (j < len2): # 如果nums2中的大数比nums1多
            nums3[k] = nums2[j]
            k = k + 1
            j = j + 1

        l = int((len1 + len2) / 2)
        if ((len1 + len2) % 2 != 0): # 如果n是奇数
            return nums3[l]
        else:
            return (nums3[l-1] + nums3[l])/2


if __name__ == '__main__':
    nums1 = [1, 3, 5, 7, 9]
    nums2 = [2, 4, 19]
    slt = Solution2()
    gg = slt.findMedianSortedArrays(nums1, nums2)
    print(gg)