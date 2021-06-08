'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。输出下标

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

'''

nums = [3, 2, 4]
target = 6
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == target-nums[j]:
            a = [i, j]
            print(a)
            print(nums[i], nums[j])
