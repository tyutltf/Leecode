# -*- encoding: utf-8 -*-
'''
@File    :   997-找到小镇的法官.py
@Time    :   2021/12/21 21:04:21
@Author  :   TYUT ltf
@Version :   v1.0
@Contact :   18235121656@163.com
@License :   (C)Copyright 2020-2030, GNU General Public License
'''
# here put the import lib
from typing import List
'''
小镇里有 n 个人，按从 1 到 n 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。

如果小镇法官真的存在，那么：

小镇法官不会信任任何人。
每个人（除了小镇法官）都信任这位小镇法官。
只有一个人同时满足属性 1 和属性 2 。
给你一个数组 trust ，其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。

如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 -1 。

 

示例 1：

输入：n = 2, trust = [[1,2]]
输出：2
示例 2：

输入：n = 3, trust = [[1,3],[2,3]]
输出：3
示例 3：

输入：n = 3, trust = [[1,3],[2,3],[3,1]]
输出：-1
 
提示：

1 <= n <= 1000
0 <= trust.length <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-town-judge
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 错误题解
        # people = [i[0] for i in trust]
        # judge = list(set([i[1] for i in trust]))
        # is_judge = [i for i in judge if i not in people]
        # if len(is_judge) == 1:
        #     return is_judge[0]
        # else:
        #     return -1
        '''
        解题思路
        法官不相信任何人，
        相信法官的人为 n - 1
        只需要分别统计出，每个人相信了多少，每个人被多少人相信即可，同时满足上述条件的计委法官
        '''
        cnt1 = [0]*(n + 1)
        cnt2 = [0]*(n + 1)
        for x, y in trust:
            cnt1[y] += 1
            cnt2[x] += 1
        for i in range(1, n + 1):
            if cnt1[i] == n - 1 and cnt2[i] == 0:
                return i
        return -1


obj = Solution()
n = 3
trust = [[1, 2], [2, 3]]
print(obj.findJudge(n, trust))
