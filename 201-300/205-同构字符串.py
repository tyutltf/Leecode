# -*- encoding: utf-8 -*-
'''
@File    :   205-同构字符串.py
@Time    :   2021/07/13 20:33:15
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

 

示例 1:

输入：s = "egg", t = "add"
输出：true
示例 2：

输入：s = "foo", t = "bar"
输出：false
示例 3：

输入：s = "paper", t = "title"
输出：true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/isomorphic-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isIsomorphic(self, s: str, t: str):
        if not s:
            return True
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]] = t[i]
            else:
                if dic[s[i]] != t[i]:
                    return False
        return True

        # 另一种 index 解法
        # return all(s.index(s[i]) == t.index(t[i])  for i in range(len(s)))

        '''
        自己解法 考虑不周
        def isIsomorphic(self, s: str, t: str):
            if self.get_num(s) == self.get_num(t):
                return True
            else:
                return False

        def get_num(self, s):
            s_list = list(s)
            res = []
            temp = []
            for i in s_list:
                if i not in temp:
                    temp.append(i)
                    res.append(1)
                else:
                    temp.append(i)
                    num = temp.count(i)+1
                    res.append(num)
            return res
        '''


obj = Solution()
print(obj.isIsomorphic('add', 'cdd'))
