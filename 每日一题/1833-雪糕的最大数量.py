# -*- encoding: utf-8 -*-
'''
@File    :   1833-雪糕的最大数量.py
@Time    :   2021/07/02 19:42:57
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
夏日炎炎，小男孩 Tony 想买一些雪糕消消暑。

商店中新到 n 支雪糕，用长度为 n 的数组 costs 表示雪糕的定价，其中 costs[i] 表示第 i 支雪糕的现金价格。Tony 一共有 coins 现金可以用于消费，他想要买尽可能多的雪糕。

给你价格数组 costs 和现金量 coins ，请你计算并返回 Tony 用 coins 现金能够买到的雪糕的 最大数量 。

注意：Tony 可以按任意顺序购买雪糕。

 

示例 1：

输入：costs = [1,3,2,4,1], coins = 7
输出：4
解释：Tony 可以买下标为 0、1、2、4 的雪糕，总价为 1 + 3 + 2 + 1 = 7
示例 2：

输入：costs = [10,6,8,7,7,8], coins = 5
输出：0
解释：Tony 没有足够的钱买任何一支雪糕。
示例 3：

输入：costs = [1,6,3,1,2,5], coins = 20
输出：6
解释：Tony 可以买下所有的雪糕，总价为 1 + 6 + 3 + 1 + 2 + 5 = 18 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-ice-cream-bars
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def maxIceCream(self, costs: List[int], coins: int):
        # costs.sort()
        # if coins < costs[0]:
        #     return 0
        # pay = 0
        # branch = 0
        # for i in costs:
        #     pay += i
        #     branch += 1
        #     while pay >= coins:
        #         if pay > coins:
        #             return branch-1
        #         elif pay == coins:
        #             return branch
        # return len(costs)

        # 从小到大排序 然后用总的钱减
        costs.sort()
        ret = 0
        for cost in costs:
            coins -= cost
            if coins < 0:
                break
            ret += 1
        return ret


object = Solution()
costs = [1, 3, 2, 4, 1]
coins = 7
print(object.maxIceCream(costs, coins))
