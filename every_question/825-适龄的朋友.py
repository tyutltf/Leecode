# -*- encoding: utf-8 -*-
'''
@File    :   825-适龄的朋友.py
@Time    :   2021/12/27 21:19:56
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
from collections import Counter
from math import ceil
# here put the import lib
from typing import List

'''
在社交媒体网站上有 n 个用户。给你一个整数数组 ages ，其中 ages[i] 是第 i 个用户的年龄。

如果下述任意一个条件为真，那么用户 x 将不会向用户 y（x != y）发送好友请求：

age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
否则，x 将会向 y 发送一条好友请求。

注意，如果 x 向 y 发送一条好友请求，y 不必也向 x 发送一条好友请求。另外，用户不会向自己发送好友请求。

返回在该社交媒体网站上产生的好友请求总数。


示例 1：

输入：ages = [16,16]
输出：2
解释：2 人互发好友请求。
示例 2：

输入：ages = [16,17,18]
输出：2
解释：产生的好友请求为 17 -> 16 ，18 -> 17 。
示例 3：

输入：ages = [20,30,100,110,120]
输出：3
解释：产生的好友请求为 110 -> 100 ，120 -> 110 ，120 -> 100 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/friends-of-appropriate-ages
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路:
根据题目描述和测试用例可知答案要的是 最大总数, 故忽略题干中的注意部分。

条件三已由条件二过滤，忽略。

由条件一和二联立, 很容易得到给定年龄的交友年龄范围: age-ceil((age-14)/2)+1 到 age.
其中 ceil((age-14)/2) 为可交友的年龄的总数。

'''


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def friendsage(x): return set(range(age+1-ceil(0.5*age-7), age+1))
        aC, ans = Counter(ages), 0
        for age in aC.keys():
            if age > 14:
                inS = (aC.keys() & friendsage(age))  # 交集
                ans += (sum(aC[k] for k in inS) - 1)*aC[age]
        return ans


obj = Solution()
ages = [20, 30, 100, 110, 120]
print(obj.numFriendRequests(ages))
