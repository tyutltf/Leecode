# -*- encoding: utf-8 -*-
'''
@File    :   846-一手顺子.py
@Time    :   2021/12/30 20:51:50
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
from collections import Counter
'''
Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。

给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。如果她可能重新排列这些牌，返回 true ；否则，返回 false 。

示例 1：

输入：hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
输出：true
解释：Alice 手中的牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
示例 2：

输入：hand = [1,2,3,4,5], groupSize = 4
输出：false
解释：Alice 手中的牌无法被重新排列成几个大小为 4 的组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hand-of-straights
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

"""
用哈希表来记录所有数字出现的次数，然后从最小的值开始往上遍历（贪心），每次key+1，并且让字典中对应的牌数-1

因为顺子必定是连续而且大小为groupSize的，所以如果遍历过程中发现需要的牌不在字典里，那就可以直接返回False了

如果凑完顺子时刚好cnt为空，那就说明hand中的牌可以凑成一个顺子，返回True
"""


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 先判断列表长度是否可以整除groupsize
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        cnt = Counter(hand)
        for x in hand:
            if cnt[x] == 0:
                continue
            for num in range(x, x + groupSize):
                if cnt[num] == 0:
                    return False
                cnt[num] -= 1
        return True


obj = Solution()
hand, groupSize = [1, 2, 3, 6, 2, 3, 4, 7, 8], 3
print(obj.isNStraightHand(hand, groupSize))
