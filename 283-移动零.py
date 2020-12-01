'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # l = len(nums)  #原始数组长度
        # while True:   #删除数组中的所有0
        #     try:
        #         nums.remove(0)
        #     except:
        #         break   
        # nums += [0]*(l-len(nums)) #数组长度减少的就是删除的0的个数
        # return nums

        i = -1
        for j in range(len(nums)):
            print(j)
            if nums[j]!=0:
                i+=1
                nums[i],nums[j]= nums[j], nums[i]
        return nums

obj=Solution()
print(obj.moveZeroes([0,1,0,3,12]))