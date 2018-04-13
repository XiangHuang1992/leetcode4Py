 -*- coding: utf-8 -*-
"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且相同的元素不能重复利用。
nums = [2, 7, 11, 15] target= 9
因为nums[0] + num[1] = 9
所以返回[0, 1]
"""


class Solution(object):
    def twoSum(self, nums, target):
        # 暴力破解，效率十分低
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        # 第二种方法，可以先扫面一遍数组，然后将数组的值存入keys，在用target - nums[i]的值去查看keys中是否存在，存在则找到了。只需要遍历一次。效率比较高。
        keys = {}
        for i in range(len(nums)):
            if target - nums[i] in keys:
                return [keys[target - nums[i]], i]
            if nums[i] not in keys:
                keys[nums[i]] = i
