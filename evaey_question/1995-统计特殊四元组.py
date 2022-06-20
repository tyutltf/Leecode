# -*- encoding: utf-8 -*-
'''
@File    :   1995-统计特殊四元组.py
@Time    :   2021/12/29 24:31:18
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
from collections import Counter
'''
给你一个 下标从 0 开始 的整数数组 nums ，返回满足下述条件的 不同 四元组 (a, b, c, d) 的 数目 ：

nums[a] + nums[b] + nums[c] == nums[d] ，且
a < b < c < d
 

示例 1：

输入：nums = [1,2,3,6]
输出：1
解释：满足要求的唯一一个四元组是 (0, 1, 2, 3) 因为 1 + 2 + 3 == 6 。
示例 2：

输入：nums = [3,3,6,4,5]
输出：0
解释：[3,3,6,4,5] 中不存在满足要求的四元组。
示例 3：

输入：nums = [1,1,1,3,5]
输出：4
解释：满足要求的 4 个四元组如下：
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-special-quadruplets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路与算法

和LC经典的第一题有异曲同工之处。枚举左边两者和，枚举右边两者差，动态更新相同数目到答案。
即 nums[a] + nums[b] == nums[d] - nums[c]

另外同样可以采用背包动态规划思想，我们要选三个到背包里，
维护 不选的各个值的个数、选一个各个值的个数、选两个各个值的个数、选三个各个值的个数。
在遍历到每个数，统计选三个了的各值中该数的个数就是答案的一部分。

'''


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        # ans = 0
        # for a in range(len(nums)):
        #     for b in range(a+1, len(nums)):
        #         for c in range(b+1, len(nums)):
        #             for d in range(c+1, len(nums)):
        #                 if nums[a]+nums[b]+nums[c] == nums[d]:
        #                     ans += 1
        # return ans

        l, ans = Counter(), 0
        for i in range(1, len(nums) - 2):
            print(i)
            # 到目前为止统计了所有0到i的两坐标和
            for j in range(i):
                print(j)
                l[nums[i] + nums[j]] += 1
                print(l)
            # 目前第三个坐标为i+1，枚举第四个坐标j的范围
            for j in range(i + 2, len(nums)):
                # 叠加以前统计的左半段和的结果，i+1作为第三个idx和j最多组成这么多
                ans += l[nums[j] - nums[i+1]]
        return ans


obj = Solution()
nums = [1, 1, 1, 3, 5]
print(obj.countQuadruplets(nums))
