'''
给你一个字符串 jewels 代表石头中宝石的类型，另有一个字符串 stones 代表你拥有的石头。 stones 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。

字母区分大小写，因此 "a" 和 "A" 是不同类型的石头。

示例 1：

输入：jewels = "aA", stones = "aAAbbbb"
输出：3
示例 2：

输入：jewels = "z", stones = "ZZ"
输出：0

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/jewels-and-stones
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in jewels:
            temp = stones.count(i)
            count += temp
        return count

        # 哈希集合
        # jewelsSet = set(jewels)
        # return sum(s in jewelsSet for s in stones)


obj = Solution()
jewels = "aA"
stones = "aAAbbbb"
print(obj.numJewelsInStones(jewels, stones))
