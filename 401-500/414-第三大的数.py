'''

给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。


示例 1：

输入：[3, 2, 1]
输出：1
解释：第三大的数是 1 。
示例 2：

输入：[1, 2]
输出：2
解释：第三大的数不存在, 所以返回最大的数 2 。
示例 3：

输入：[2, 2, 3, 1]
输出：1
解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。
'''

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]):
        # 集合 变 列表 再排序
        set_nums = list(set(nums))
        set_nums.sort()
        return set_nums[-1] if len(set_nums) < 3 else set_nums[-3]


'''
# 长度小于3的，直接返回最大值
ll_nums = list(set(nums))
if len(ll_nums) < 3:
    return max(ll_nums)
#初始化最大值，次大值，第三大值
a = b = c = 0
# 遍历列表：
for num in nums:
    # 大于最大值，依次更新，这里要注意更新顺序，先更新c, 然后b, 最后a
    if num > a:
        c = b
        b = a
        a = num
    # 更新次大值
    elif num > b and num != a:
        c = b
        b = num
    # 更新第三大值
    elif num > c and num != a and num != b:
        c = num
return c
'''


obj = Solution()
print(obj.thirdMax([2, 2, 3, 1]))
