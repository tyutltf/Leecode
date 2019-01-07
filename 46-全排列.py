'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return [nums]
        results=[]
        for index in range(len(nums)):
            for item in self.permute(nums[:index]+nums[index+1:]):
                results.append([nums[index]]+item)
        return results

object=Solution()
nums=[1,2,3]
results=object.permute(nums)
print(results)
