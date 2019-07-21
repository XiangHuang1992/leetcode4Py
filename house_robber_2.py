# -*- coding: utf-8 -*-
"""
    leetcode4Py.house_robber_2
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    leetcode 213: House Robber 2
    在house robber 1 的基础上添加了一个条件，房屋首尾相连。

    思路： 跟1的思路一样。只不过这次要分两种条件来算：一种是偷第1个的，一种是不偷第
           1个的，最后统计中两者的最大值。

    :copyright: (c) 2019 by YOUR_NAME.
    :license: LICENSE_NAME, see LICENSE for more details.
"""


class Solution:
    def rob(self, nums):
        length = len(nums)

        if not nums:
            return 0

        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums)
        if length == 3:
            return max(nums)

        nums1 = nums[1:]
        nums2 = nums[:-1]

        dp1 = [0] * len(nums1)
        dp2 = [0] * len(nums2)

        dp1[0] = nums1[0]
        dp1[1] = max(nums1[0], nums1[1])

        dp2[0] = nums2[0]
        dp2[1] = max(nums2[0], nums2[1])

        for i in range(2, length - 1):
            dp1[i] = max((nums1[i] + dp1[i - 2]), dp1[i - 1])
            dp2[i] = max((nums2[i] + dp2[i - 2]), dp2[i - 1])

        return max(dp1[-1], dp2[-1])

    def rob_2(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(
            self.rob_helper(nums, 0, len(nums) - 2),
            self.rob_helper(nums, 1, len(nums) - 1),
        )

    def rob_helper(self, nums, low, high):
        prevMax = currMax = 0
        for i in range(low, high + 1):
            temp = currMax
            currMax = max(prevMax + nums[i], currMax)
            prevMax = temp
        return currMax


def main(nums):
    s = Solution()

    print(s.rob(nums))
    print(s.rob_2(nums))


if __name__ == "__main__":
    main([2, 3, 4])
