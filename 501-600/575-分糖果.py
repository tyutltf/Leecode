# -*- encoding: utf-8 -*-
'''
@File    :   575-分糖果.py
@Time    :   2021/08/09 21:18:06
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。

示例 1:

输入: candies = [1,1,2,2,3,3]
输出: 3
解析: 一共有三种种类的糖果，每一种都有两个。
     最优分配方案：妹妹获得[1,2,3],弟弟也获得[1,2,3]。这样使妹妹获得糖果的种类数最多。
示例 2 :

输入: candies = [1,1,2,3]
输出: 2
解析: 妹妹获得糖果[2,3],弟弟获得糖果[1,1]，妹妹有两种不同的糖果，弟弟只有一种。这样使得妹妹可以获得的糖果种类数最多。
'''


class Solution:
    def distributeCandies(self, candies: List[int]):
        # res = []
        # for i in candies:
        #     if i not in res:
        #         res.append(i)
        # if len(res) < len(candies)/2:
        #     return len(res)
        # else:
        #     return int(len(candies)/2)

        res = 0
        if len(set(candies)) < len(candies) // 2:
            res = len(set(candies))
        else:
            res = len(candies) // 2
        return res


obj = Solution()
candies = [1, 1, 2, 2, 3, 3]
print(obj.distributeCandies(candies))
