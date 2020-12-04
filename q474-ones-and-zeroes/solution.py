#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
from typing import List
from collections import Counter


class BruteForceSolution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def find_max_in_subset(start, target_m, target_n, curr_size):
            nonlocal max_size
            if target_m == 0 and target_n == 0 and curr_size > max_size:
                max_size = curr_size
            if target_m < 0 or target_n < 0:
                return
            if start >= len(strs):
                return
            curr_m, curr_n = self.count_01s(strs[start])
            find_max_in_subset(start + 1, target_m - curr_m,
                               target_n - curr_n, curr_size + 1)
            find_max_in_subset(start + 1, target_m, target_n, curr_size)
        max_size = 0
        find_max_in_subset(0, m, n, 0)
        return max_size

    def count_01s(self, seq):
        counter = Counter(seq)
        return (counter['0'] if '0' in counter else 0,
                counter['1'] if '1' in counter else 0)


class DPSolution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[None] * (n+1) for i in range(m+1)]
              for i in range(len(strs) + 1)]
        dp[0][0][0] = 0
        for start in range(1, len(strs)+1):
            curr_m, curr_n = self.count_01s(strs[start-1])
            for i in range(m+1):
                for j in range(n+1):
                    if i-curr_m >= 0 and j-curr_n >= 0 and dp[start-1][i-curr_m][j-curr_n] is not None:
                        dp[start][i][j] = dp[start-1][i-curr_m][j-curr_n] + 1
                    if dp[start-1][i][j] is not None:
                        dp[start][i][j] = max(
                            dp[start-1][i][j], dp[start][i][j] or 0)
        return max(dp[-1][i][j] or 0 for i in range(m+1) for j in range(n+1))

    def count_01s(self, seq):
        counter = Counter(seq)
        return (counter['0'] if '0' in counter else 0,
                counter['1'] if '1' in counter else 0)


class AnotherDPSolution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[None] * (n+1) for i in range(m+1)]
        dp[0][0] = 0
        for curr_str in strs:
            curr_m, curr_n = self.count_01s(curr_str)
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i-curr_m >= 0 and j-curr_n >= 0 and dp[i-curr_m][j-curr_n] is not None:
                        dp[i][j] = max(
                            dp[i-curr_m][j-curr_n] + 1, dp[i][j] or 0)
        return max(dp[i][j] or 0 for i in range(m+1) for j in range(n+1))

    def count_01s(self, seq):
        counter = Counter(seq)
        return (counter['0'] if '0' in counter else 0,
                counter['1'] if '1' in counter else 0)


Solution = AnotherDPSolution
# @lc code=end
