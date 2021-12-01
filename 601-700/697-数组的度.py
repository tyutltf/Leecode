# -*- encoding: utf-8 -*-
'''
@File    :   697-数组的度.py
@Time    :   2021/12/01 20:51:07
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
import collections

'''
给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

 

示例 1：

输入：[1, 2, 2, 3, 1]
输出：2
解释：
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
示例 2：

输入：[1,2,2,3,1,4,2]
输出：6
 

提示：

nums.length 在1到 50,000 区间范围内。
nums[i] 是一个在 0 到 49,999 范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/degree-of-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def findShortestSubArray(self, nums: List[int]):
        # todo 自己解法 超时
        # x = dict((a, nums.count(a)) for a in nums)
        # grade_mode = [k for k, v in x.items() if max(x.values()) == v]
        # res = []
        # for i in grade_mode:
        #     temp = []
        #     for j in range(len(nums)):
        #         if nums[j] == i:
        #             temp.append(j)
        #             break
        #     for k in range(len(nums)-1, 0, -1):
        #         if nums[k] == i:
        #             temp.append(k)
        #             break
        #     res.append(temp[-1]-temp[0]+1)
        # return min(res)

        left, right = dict(), dict()
        counter = collections.Counter()
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            counter[num] += 1
        degree = max(counter.values())
        res = len(nums)
        for k, v in counter.items():
            if v == degree:
                res = min(res, right[k] - left[k] + 1)
        return res


obj = Solution()
nums = [1, 2, 2, 3, 1, 4, 3]
print(obj.findShortestSubArray(nums))
