# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/1/14 19:24
# @author  : Mo
# @function: 22. 括号生成


# 22. 括号生成
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/generate-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 22.生成括号
class Solution:

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0:
            return False

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
    # 先全部生成, 再判断对不对
    def generateParenthesis(self, n):
        len_n = n - 1
        sums = [["("]] + [["(", ")"] for i in range(len_n+n)]

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

        dals = select_all_syn_sentence(count=len(sums) - 1, candidate_list_set=sums[1:], syn_sentences=sums[0])

        res = []
        for dal in dals:
            if self.isValid(dal):
                res.append(dal)
        return res
    # 官方先生成1 再判断
    # 为了生成所有序列，我们使用递归。长度为n的序列就是'('加上所有长度为n - 1的序列，以及')'加上所有长度为n - 1的序列。
    # 为了检查序列是否为有效的，我们会跟踪平衡，也就是左括号的数量减去右括号的数量的净值。如果这个值始终小于零或者不以零结束，该序列就是无效的，否则它是有效的。
    def generateParenthesis2(self, n):
        def generate(A=[]):
            if len(A) == 2 * n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans
    # # 回溯, 官方先生成2 再判断 (卡特兰数)
    # **h(n)= h(0)*h(n-1)+h(1)*h(n-2) + ... + h(n-1)*h(0) (n>=2);
    # **h(n)=h(n-1)*(4*n-2)/(n+1);
    # 只有在我们知道序列仍然保持有效时才添加'(' or ')'，而不是像
    # 方法一那样每次添加。我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，
    # 如果我们还剩一个位置，我们可以开始放一个左括号。 如果它不超过左括号的数量，我们可以放一个右括号。
    def generateParenthesis3(self, N):
        ans = []

        def backtrack(S='', left=0, right=0):
            # print(S)
            if len(S) == 2 * N:
                ans.append(S)
                # return返回的是上一级, 第二次返回也是返回上一级
                return
            if left < N:
                print("L" + S + "      " + str(left) + " "+ str(right))
                backtrack(S + '(', left + 1, right)
            if right < left:
                print("R" + S + "      " + str(left) + " "+ str(right))
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans
    # 闭合数
    # 为了枚举某些内容，我们通常希望将其表示为更容易计算的不相交子集的总和。
    # 考虑有效括号序列S的闭包数：至少存在index >= 0，使得S[0], S[1], ..., S[2 * index + 1]是有效的。 显然，每个括号序列都有一个唯一的闭包号。 我们可以尝试单独列举它们。
    # 算法: 对于每个闭合数c，我们知道起始和结束括号必定位于索引0和2 * c + 1。然后两者间的2 * c个元素一定是有效序列，其余元素一定是有效序列。
    def generateParenthesis4(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis4(c):
                for right in self.generateParenthesis4(N - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans


if __name__ == '__main__':
    sol = Solution()

    res = sol.generateParenthesis4(2)
    for r in res:
        print(r)

