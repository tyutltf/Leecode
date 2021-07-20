# -*- encoding: utf-8 -*-
'''
@File    :   485-最大连续1的个数.py
@Time    :   2021/07/20 21:13:23
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
给定一个二进制数组， 计算其中最大连续 1 的个数。

 

示例：

输入：[1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
 

提示：

输入的数组只包含 0 和 1 。
输入数组的长度是正整数，且不超过 10,000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-consecutive-ones
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]):
        count = 0
        ans = 0
        for i in nums:
            if i == 1:
                count += 1
                if ans < count:
                    ans = count
            else:
                count = 0
        return ans


obj = Solution()
nums = [1, 1, 0, 1, 1, 1]
print(obj.findMaxConsecutiveOnes(nums))
