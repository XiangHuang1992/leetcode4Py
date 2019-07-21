class Solution:
    """
    给定一个整数数组nums，找到一个具有最大和的连续子数组(子数组最少包含一个元素)，返回其最大和。
    """

    def maxSubArray(self, nums) -> int:
        ret = dp = nums[0]

        for i in range(1, len(nums)):
            dp = max(dp + nums[i], nums[i])
            ret = max(dp, ret)

        return ret

    def maxSubArray2(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)

        return max(nums)


if __name__ == "__main__":

    s = Solution()
    l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray(l))
    print(s.maxSubArray2(l))
