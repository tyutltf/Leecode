'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''

def searchRange(nums, target):
    if len(nums) == 0:
        return [-1,-1]
    elif target < nums[0] or target > nums[-1]:
        return [-1,-1]
    else:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            elif target == nums[mid]:
                l = r = mid
                while l-1 >= 0 and nums[l-1] == target:
                    l -= 1
                while r+1 <= len(nums)-1 and nums[r+1] == target:
                    r += 1
                return [l,r]
    return [-1,-1]

nums = [1,3,4,6,8,8,9,10]
a = searchRange(nums,5)
print(a)