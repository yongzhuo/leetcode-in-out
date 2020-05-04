# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/9/5 14:24
# @author   :Mo
# @function :


def merge_two(nums1, nums2):
    """
        归并排序
    :param nums1: 
    :param nums2: 
    :return: 
    """
    len_1 = len(nums1)
    len_2 = len(nums2)
    nums3 = [0] * (len_1 + len_2)
    i=j=k=0

    while i < len_1 and j < len_2:
        if nums1[i] < nums2[j]:
            nums3[k] = nums1[i]
            i += 1
        else:
            nums3[k] = nums1[j]
            j += 1
        k += 1

    while i < len_1:
        nums3[k] = nums1[i]
        i += 1
        k += 1

    while j < len_2:
        nums3[k] = nums2[j]
        j += 1
        k += 1

    mid = int((len_1 + len_2) / 2)
    if ((len_1 + len_2) % 2) != 0:
        res = nums3[mid]
    else:
        res = (nums3[mid] + nums3[mid+1]) / 2

    return res

# 动态规划-状态转移矩阵
class Solution:
    def longestPalindrome(self, text: str) -> str:
        len_text = len(text)
        if len_text <= 1:
            return text

        martix = [[False for _ in range(len_text)] for _ in range(len_text)]

        l = 1
        res = text[0]
        for i in range(1, len_text):
            for j in range(i):
                if text[i]==text[j] and (i - j <= 2 or martix[j+1][i-1]):
                    martix[j][i] = True
                    cur_len = i - j + 1
                    if cur_len > l:
                        l = cur_len
                        res = text[j:i + 1]
        return res




if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [6, 89, 90]
    res_ = merge_two(nums1, nums2)
    print(res_)
    sl = Solution()
    text = "大大大大"
    dp = sl.longestPalindrome(text)
    print(dp)