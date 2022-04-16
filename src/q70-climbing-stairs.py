#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        n_minus_1, cur_n = 1, 1
        for _ in range(n-1):
            n_minus_1, cur_n = cur_n, n_minus_1 + cur_n
        return cur_n


class MatrixSolution:
    def climbStairs(self, n: int) -> int:
        result = self.matrix_multiply(
            self.logorithm_matrix_multiply(n), [[1], [1]])
        return result[1][0]

    def logorithm_matrix_multiply(self, n):
        start = [[1, 1],
                 [1, 0]]
        if n == 1:
            return start
        if n % 2 == 0:
            half = self.logorithm_matrix_multiply(n / 2)
            return self.matrix_multiply(half, half)
        else:
            return self.matrix_multiply(self.logorithm_matrix_multiply(n-1), start)

    def matrix_multiply(self, m1, m2):
        result = [[0]*len(m2[0]) for _ in range(len(m1))]
        for i in range(len(result)):
            for j in range(len(result[0])):
                for k in range(len(m1[0])):
                    result[i][j] += (m1[i][k] * m2[k][j])
        return result

# @lc code=end


solve = Solution().climbStairs


def test_matrix_multiply():
    assert MatrixSolution().matrix_multiply(
        [[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]


def test_default():
    assert solve(2) == 2
    assert solve(3) == 3
    assert solve(4) == 5


def test_corner_cases():
    assert solve(1) == 1
