'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def majorityElement(self, nums) -> int:
        count = len(nums)/2
        nums_set = list(set(nums))
        for i in nums_set:
            sum = 0
            for j in nums:
                if j == i:
                    sum += 1
            if sum >= count:
                return i
            else:
                pass

    def majorityElement_good(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = 0
        count = 0

        for n in nums:
            if count == 0:
                major = n
            if n == major:
                count = count + 1
            else:
                count = count - 1

        return major


obj = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
print(obj.majorityElement_good(nums))
