# -*- encoding: utf-8 -*-
'''
@File    :   594-最长和谐子数列.py
@Time    :   2021/08/10 22:15:58
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。

现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。

数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。

示例 1：

输入：nums = [1,3,2,2,5,2,3,7]
输出：5
解释：最长的和谐子序列是 [3,2,2,2,3]
示例 2：

输入：nums = [1,2,3,4]
输出：2
示例 3：

输入：nums = [1,1,1,1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-harmonious-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def findLHS(self, nums: List[int]):
        dic = {}
        res = 0
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        print(dic)
        for key in dic:
            if (key + 1) in dic:
                res = max(res, dic[key] + dic[key + 1])
        return res


object = Solution()
nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(object.findLHS(nums))
