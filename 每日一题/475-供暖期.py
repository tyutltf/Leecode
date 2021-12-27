# -*- encoding: utf-8 -*-
'''
@File    :   475-供暖期.py
@Time    :   2021/12/20 20:47:20
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typeing import List
'''

冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

在加热器的加热半径范围内的每个房屋都可以获得供暖。

现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

说明：所有供暖器都遵循你的半径标准，加热的半径也一样。


示例 1:

输入: houses = [1,2,3], heaters = [2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
示例 2:

输入: houses = [1,2,3,4], heaters = [1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
示例 3：

输入：houses = [1,5], heaters = [2]
输出：3
'''


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters = heaters + [-float("inf"), float("inf")]
        houses.sort()
        heaters.sort()
        i, j, ans = 0, 0, 0
        while i < len(houses):
            cur = float("inf")
            while heaters[j] <= houses[i]:
                cur = houses[i] - heaters[j]
                j += 1
            cur = min(cur, heaters[j] - houses[i])
            ans = max(cur, ans)
            i += 1
            j -= 1
        return ans
