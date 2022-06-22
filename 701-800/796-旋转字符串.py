'''
给定两个字符串, s 和 goal。如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true 。

s 的 旋转操作 就是将 s 最左边的字符移动到最右边。 

例如, 若 s = 'abcde'，在旋转一次之后结果就是'bcdea' 。
 

示例 1:

输入: s = "abcde", goal = "cdeab"
输出: true
示例 2:

输入: s = "abcde", goal = "abced"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/rotate-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 解题思路
# 所谓的旋转其实就是以任意位置开始，到转回来自己结束。
# 即为两个原字符串拼接的子串

# PS:
# 在很多尾和头相连的数组题目中，都常使用两倍数组的小技巧


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s


obj = Solution()
s = "abcde"
goal = "cdeab"
print(obj.rotateString(s, goal))
