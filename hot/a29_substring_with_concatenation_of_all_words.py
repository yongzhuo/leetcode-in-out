# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/3/3 19:59
# @author  : Mo
# @function:


"""
30. 串联所有单词的子串
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1：
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
通过次数24,766提交次数83,693
"""
"""
30. Substring with Concatenation of All Words
You are given a string, s, and a list of words, words, that are all of the same length. 
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once 
and without any intervening characters.

Example 1:
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
通过次数24,766提交次数83,693
"""

from collections import Counter


class Solution:
    # 排序再比较, 不行，超出时间限制
    def findSubstringmy(self, s, words):
        if not s or not words:
            return []
        res_permutation = []
        def permutation(nums, p, q):
            if p == q:
                res_permutation.append(list(nums))
            else:
                for i in range(p, q):
                    nums[i], nums[p] = nums[p], nums[i]
                    permutation(nums, p + 1, q)
                    nums[i], nums[p] = nums[p], nums[i]
        permutation(words, 0, len(words))
        res_ = []
        for rp in res_permutation:
            str_rp = "".join(rp)
            for i in range(len(s)):
                flag = s[i:].find(str_rp)
                if flag != -1:
                    res_.append(flag+i)
        return list(set(res_))

    def findSubstring0(self, s, words):
        from collections import Counter
        if not s or not words:
            return []
        len_ws = len(words)
        len_s = len(s)
        len_w = len(words[0])
        pattern = Counter(words)
        res_ = []
        for i in range(0, len_s-len_ws*len_w+1):
            list_words = []
            for j in range(len_ws):
                start = i+j*len_w
                s_t = s[start:start + len_w]
                list_words.append(s_t)
            counter_list = Counter(list_words)
            if counter_list == pattern:
                res_.append(i)
        return res_



    # 哈希表
    def findSubstring1(self, s, words):
        from collections import Counter
        if not s or not words: return []
        one_word = len(words[0])
        all_len = len(words) * one_word
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, n - all_len + 1):
            tmp = s[i:i + all_len]
            c_tmp = []
            for j in range(0, all_len, one_word):
                c_tmp.append(tmp[j:j + one_word])
            if Counter(c_tmp) == words:
                res.append(i)
        return res

    # 滑动窗口, set比较
    def findSubstring2(self, s, words):
        if not words: return []
        pattern, dist, res = Counter(words), len(words[0]), []
        len_be = len(s) - len(words) * dist + 1
        for begin in range(len_be):
            cur_list = []
            for cnt in range(len(words)):
                s_start = begin + cnt * dist
                s_end = begin + (cnt + 1) * dist
                cur_list.append(s[s_start: s_end])
            if Counter(cur_list) == pattern: res.append(begin)
        return res



if __name__ == '__main__':
    sol = Solution()
    # s = "zhuoyongbarfoothefoobarmanmomoyonzhuo"
    # words = ["yong", "zhuo"]

    s = "barfoothefoobarman"
    print(s[0:6])
    words = ["foo", "bar"]

    s = "foobarfoobar"
    fb = "foobar"
    gg = s.find(fb, 0, len(s))

    words = ["foo", "bar"]

    # s = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
    # words = ["dhvf", "sind", "ffsl", "yekr", "zwzq", "kpeo", "cila", "tfty", "modg", "ztjg", "ybty", "heqg", "cpwo", "gdcj",
    #  "lnle", "sefg", "vimw", "bxcb"]
    res = sol.findSubstring0(s, words)
    print(res)
    sr = 0



