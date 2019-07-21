"""
File: house_robber_3.py
Author: huangxiang
Email: ferdinandhx@gmail.com
Github: https://github.com/yourname
Description: leetcode 337：打家劫舍3

题目描述：
        在上一次打劫完一条街道之后和一圈房屋后，小偷又发现一个新的可行窃的地方，
        这个地区只有一个入口，我们称之为根，除了根之外，每栋房子有且只有一个父房子
        与之相连，一番侦查之后，聪明的小偷意识到这个地方所有的房屋的排列都类似与
        一颗二叉树，如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

        计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例：输入 [3,2,3,null,3,null,1]
      输出 3 + 3 + 1 = 7

思路：

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        pass


def main():
    pass


if __name__ == "__main__":
    main()
