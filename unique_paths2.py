#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
    leetcode4Py.unique_paths2
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    leetcode 63 不同路径二

    输入：
    [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    输出：2

    说明：
    3*3网格的正中间有一个障碍物。
    从左上角到右下角一共有两条不同到路径：
    1. 向右-向右-向下-向下
    2. 向下-向下-向右-向右

    :copyright: (c) 2019 by huangxiang.
    :license: one line to give the program's name and a brief description
    Copyright © 2019 huangxiang

    Permission is hereby granted, free of charge, to any person obtaining
    a copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included
    in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
    OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
    OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    , see LICENSE for more details.
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or obstacleGrid is None:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [[0] * (m + 1) for i in range(n + 1)]
        dp[0][1] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if obstacleGrid[i - 1][j - 1] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n][m]

    def uniquePathsWithObstacles_2(self, obstacleGrid):

        if not obstacleGrid or obstacleGrid is None:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        prev = curr = [1] + [0] * (m - 1)

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                elif j > 0:
                    curr[j] = prev[j] + curr[j - 1]
            prev, curr = curr, prev

        return prev[m - 1]

    def uniquePathsWithObstacles_3(self, obstacleGrid):
        if not obstacleGrid or obstacleGrid is None:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        curr = [1] + [0] * (m - 1)

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                elif j > 0:
                    curr[j] += curr[j - 1]
        return curr[m - 1]


def main(obstacleGrid):
    s = Solution()
    print(s.uniquePathsWithObstacles(obstacleGrid))
    print(s.uniquePathsWithObstacles_2(obstacleGrid))
    print(s.uniquePathsWithObstacles_3(obstacleGrid))


if __name__ == "__main__":
    obs = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    main(obs)
