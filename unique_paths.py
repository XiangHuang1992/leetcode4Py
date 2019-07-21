class Solution:
    """
    一个机器人位于一个m x n 的网格的左上角，机器人每次只能向下或者向右移动一步。
    机器人试图到达网格的右下角。
    问总共右多少条不同的路径。
    """

    def uniquePaths(self, m: int, n: int):
        # 递归
        if m < 0 or n < 0:
            return 0
        if m == 1 and n == 1:
            return 1

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    def uniquePaths_2(self, m: int, n: int):

        # dp
        if m < 0 or n < 0:
            return 0
        if m == 1 and n == 1:
            return 1

        temp = [[1] * m for i in range(n)]
        print(temp)

        for i in range(1, n):
            for j in range(1, m):
                temp[i][j] = temp[i - 1][j] + temp[i][j - 1]
                print(temp[i][j])
        return temp[n - 1][m - 1]

    def uniquePaths_3(self, m: int, n: int):

        # dp 优化
        if m < 0 or n < 0:
            return 0
        if m == 1 or n == 1:
            return 1

        prev = [1] * m
        curr = [1] * m

        for i in range(1, n):
            for j in range(1, m):
                curr[j] = prev[j] + curr[j - 1]
            prev, curr = curr, prev
        return prev[m - 1]

    def uniquePaths_4(self, m: int, n: int):
        # dp优化

        if m < 0 or n < 0:
            return 0
        if m == 1 or n == 1:
            return 1

        curr = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                curr[j] += curr[j - 1]
        return curr[m - 1]


def main(m: int, n: int):
    s = Solution()
    # print(s.uniquePaths(m, n))
    # print(s.uniquePaths_2(m, n))
    # print(s.uniquePaths_3(m, n))
    print(s.uniquePaths_4(m, n))


if __name__ == "__main__":
    main(7, 5)
