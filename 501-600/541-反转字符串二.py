# -*- encoding: utf-8 -*-
'''
@File    :   541-反转字符串2.py
@Time    :   2021/07/23 21:02:43
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
'''
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
 
示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
 
提示：

该字符串只包含小写英文字母。
给定字符串的长度和 k 在 [1, 10000] 范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def reverseStr(self, s: str, k: int):
        res_ = ''
        for i in range(0, len(s), 2*k):
            # 每2k个构建新字符串
            temp = s[i:i+2*k]
            # 判断反转
            if k < len(temp) <= 2*k:
                res = temp[0:k][::-1]+temp[k::]
            else:
                res = temp[::-1]
            res_ += res
        return res_


object = Solution()
s = "abcdefg"
k = 3
print(object.reverseStr(s, k))
