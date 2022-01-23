#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
from typing import List

# @lc code=start


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            self.extend(i, i, s, dp)
            self.extend(i, i+1, s, dp)
        prev_partitions = [[(0, 0)]]
        for i in range(1, n):
            cur_partitions = []
            for p in prev_partitions:
                n1 = p + [(i, i)]
                if dp[n1[-2][0]][n1[-2][1]]:
                    cur_partitions.append(n1)
                n2 = p[:-1] + [(p[-1][0], i)]
                if len(n2) == 1 or dp[n2[-2][0]][n2[-2][1]]:
                    cur_partitions.append(n2)
            prev_partitions = cur_partitions
        ret = []
        for p in prev_partitions:
            if dp[p[-1][0]][p[-1][1]]:
                ret.append([s[i:j+1] for i, j in p if dp[i][j]])
        return ret

    def extend(self, i, j, s, dp):
        while i >= 0 and j < len(s):
            if s[i] == s[j]:
                dp[i][j] = True
                i -= 1
                j += 1
            else:
                break

# @lc code=end


solve = Solution().partition


def test_default():
    assert solve('aab') == [['a', 'a', 'b'], ['aa', 'b']]
    assert solve('aaba') == [['a', 'a', 'b', 'a'],
                             ['a', 'aba'], ['aa', 'b', 'a']]


def test_corner_cases():
    assert solve('a') == [['a']]
    assert solve('ab') == [['a', 'b']]
    assert solve('aa') == [['a', 'a'], ['aa']]
