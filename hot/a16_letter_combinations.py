# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/1/5 19:22
# @author  : Mo
# @function: 17.电话号码的字母组合


# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
# 手机九宫格
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    # 手机号码便是 递归
    def letterCombinationsmy(self, digits):
        if not digits.strip():return None
        digit2str = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        res_digit = []
        for digit in digits:
            res_digit.append(list(digit2str[int(digit)]))

        def select_all_syn_sentence(count=0, candidate_list_set=[], syn_sentences=[]):
            """
              递归函数，将形如 [['1'], ['1', '2'], ['1']] 的list转为 ['111','121']
            :param count: int, recursion times
            :param candidate_list_set: list, eg.[['你'], ['是', '是不是'], ['喜欢', '喜爱', '爱'], ['米饭']]
            :param syn_sentences: list, Storing intermediate variables of syn setnence, eg.['你是喜欢米饭', '你是不是喜欢米饭', '你是不是爱米饭']
            :return: list, result of syn setnence, eg.['你是喜欢米饭', '你是不是喜欢米饭', '你是不是爱米饭']
            """
            syn_sentences_new = []
            count = count - 1
            if count == -1:
                return syn_sentences
            for candidate_list_set_one in candidate_list_set[0]:
                for syn_sentences_one in syn_sentences:
                    syn_sentences_new.append(syn_sentences_one + candidate_list_set_one)
            syn_sentences_new = select_all_syn_sentence(count=count, candidate_list_set=candidate_list_set[1:],
                                                        syn_sentences=syn_sentences_new)
            return syn_sentences_new

        dal = select_all_syn_sentence(count=len(res_digit) - 1,
                                                                 candidate_list_set=res_digit[1:],
                                                                 syn_sentences=res_digit[0])
        return dal

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output


if __name__ == '__main__':
    sol = Solution()
    strs = "34"  # ["dog","racecar","car"]
    res = sol.letterCombinations(strs)
    print(res)
    gg = 0







