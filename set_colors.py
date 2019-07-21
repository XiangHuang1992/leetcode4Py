"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

"""
from collections import Counter


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return nums

        head = 0
        tail = len(nums) - 1

        i = 0

        while i <= tail:
            if nums[i] == 2:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail -= 1
            elif nums[i] == 0:
                nums[i], nums[head] = nums[head], nums[i]
                head += 1
                i += 1
            else:
                i += 1



if __name__ == "__main__":

    s = Solution()

    n = [2, 1, 2]

    s.sortColors(n)

    print(n)
