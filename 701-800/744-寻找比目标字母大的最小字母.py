# -*- encoding: utf-8 -*-
'''
@File    :   744-寻找比目标字母大的最小字母.py
@Time    :   2021/12/27 21:16:38
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。

在比较时，字母是依序循环出现的。举个例子：

如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'
 

示例：

输入:
letters = ["c", "f", "j"]
target = "a"
输出: "c"

输入:
letters = ["c", "f", "j"]
target = "c"
输出: "f"

输入:
letters = ["c", "f", "j"]
target = "d"
输出: "f"

输入:
letters = ["c", "f", "j"]
target = "g"
输出: "j"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # # 小写字母的ascll码值为97-122
        # target_num = ord(target)
        # for i in letters:
        #     i_num = ord(i)
        #     if i_num > target_num:
        #         return i
        # # 循环出现 不满足条件返回letter第一位
        # return letters[0]

        # 二分法
        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            elif letters[mid] > target:
                right = mid - 1
        print(left, right)
        print(left % len(letters))
        return letters[left % len(letters)]


letters = ["c", "f", "j"]
target = 'j'
obj = Solution()
print(obj.nextGreatestLetter(letters, target))
