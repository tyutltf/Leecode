# -*- encoding: utf-8 -*-
'''
@File    :   551-学生出勤记录.py
@Time    :   2021/07/23 21:22:23
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
# * from collections import Counter
'''
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。

你需要根据这个学生的出勤记录判断他是否会被奖赏。

示例 1:

输入: "PPALLP"
输出: True
示例 2:

输入: "PPALLL"
输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/student-attendance-record-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def checkRecord(self, s: str):
        # 改解法没考虑到连续
        # dic = Counter(s)
        # if dic.get('A') and dic.get('L'):
        #     if dic.get('A') <= 1 and dic.get('L') <= 2:
        #         return True
        #     else:
        #         return False
        # elif dic.get('A'):
        #     if dic.get('A') <= 1:
        #         return True
        #     else:
        #         return False
        # elif dic.get('L'):
        #     if dic.get('L') <= 2:
        #         return True
        #     else:
        #         return False

        # ? 解题思路 满足A>1 或 LLL 在字符串里面的 都是Fasle 其余全True
        if s.count('A') > 1:
            return False
        if 'LLL' in s:
            return False
        else:
            return True


obj = Solution()
s = "LALL"
print(obj.checkRecord(s))
