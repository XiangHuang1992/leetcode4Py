"""
@Author: huangxiang
@Email: ferdinandhx@gmail.com
@Date: 2019-05-31 18:15
@Desc: leetcode 198题：打家劫舍
"""

"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都有一定的现金，影响你偷窃的
唯一制约因素就是相邻的房屋内装有相互连通的防盗系统，如果两间相邻的房屋在同一个
晚上被小偷进入，系统就会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，
能够偷窃到的最高金额。
示例一：
    输入: [1, 2, 3, 1]
    输出: 4
    解释: 偷窃1号房屋和3号房屋，得到最高金额 1 + 3 = 4

思路:
    只偷1号   fn(1) = val(1) = 1
    只偷2号   fn(2) = val(2) = 2
    偷3号     fn(3) = val(3) + val(1) = 4   不偷3号  fn(3) = fn(2) = 2
    偷4号     fn(4) = val(4) + fn(2) = 3    不偷4号  fn(4) = fn(3) = 4 or 2

    ....

    到第i间房为止的最大偷取额opt(i) = val(i) + opt(i) （选i）或 opt(i) = opt(i-1) （不选i）
"""


class Solution:
    def rob(self, nums):

        # 递归做法，会超时

        length = len(nums)
        if nums is None or length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return nums[1]

        return max((nums[-1] + self.rob(nums[0:-2]), self.rob(nums[0:-1])))

    def rob2(self, nums):
        # dp
        length = len(nums)

        if not nums:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums)
        elif length == 3:
            return max(nums[0] + nums[2], nums[1])

        opt = [0] * length  # 初始化一个长度为length的数组
        opt[0] = nums[0]
        opt[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            opt[i] = max((nums[i] + opt[i - 2]), opt[i - 1])

        return opt[-1]


def main(nums):
    s = Solution()
    print(s.rob(nums))
    print(s.rob2(nums))


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    main(nums)
