# -*- encoding: utf-8 -*-
'''
@File    :   506-相对名次.py
@Time    :   2021/07/22 20:39:39
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''

给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。

(注：分数越高的选手，排名越靠前。)

示例 1:

输入: [5, 4, 3, 2, 1]
输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
N 是一个正整数并且不会超过 10000。
所有运动员的成绩都不相同。
'''


class Solution:
    def findRelativeRanks(self, score: List[int]):
        # 默认最少三名运动员
        # todo 少于三名运动员的判断
        score_sort = sorted(score, reverse=True)
        print(score_sort)
        rank_list = ["Gold Medal", "Silver Medal",
                     "Bronze Medal"]+[str(i+4) for i in range(len(score)-3)]
        print(rank_list)
        dic = dict(zip(score_sort, rank_list))
        print(dic)
        res = [dic.get(i) for i in score]
        return res


obj = Solution()
score = [5, 4, 3, 2, 1]
print(obj.findRelativeRanks(score))
