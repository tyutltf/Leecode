'''
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

 

示例：

输入：19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isHappy(self, n: int) -> bool:
        # 初始化 visited
        visited = set()
        # 当 n != 1，并且没见过 n 时进行判断
        while n != 1 and n not in visited:
            # 把 n 放入 visited
            visited.add(n)
            # 计算下一轮的数字
            nxt = 0
            # 计算 n 的各位数字平方和
            while n != 0:
                nxt += (n % 10) ** 2
                n //= 10
            # 把下一轮的数字设定为 n
            n = nxt
        # 判断 n 的最终结果是否为 1
        return n == 1


obj = Solution()
print(obj.isHappy(19))
