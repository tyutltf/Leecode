'''

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
'''


class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        n = len(numbers)
        i = 0
        j = n - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return False


numbers = [2, 7, 11, 15]
target = 9
object = Solution()
print(object.twoSum(numbers, target))

'''
解题思路
i 用来指向列表的头
j 用来指向列表的尾
当他们两个相加的时候要大于target的时候，那么问题就 j 了，要减小
当他们两个相加的时候要小于target的时候，那么问题就 i 了，要增大

解决办法
https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/solution/yi-zhang-tu-gao-su-ni-on-de-shuang-zhi-zhen-jie-fa/
'''
