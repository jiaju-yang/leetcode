#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = self.normalize_pattern(p)
        n, m = len(s), len(pattern)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i, sub_p in enumerate(pattern, start=1):
            if len(sub_p) == 2:
                dp[i][0] = dp[i-1][0]
            for j, c in enumerate(s, start=1):
                if len(sub_p) == 2:
                    if sub_p[0] == '.':
                        dp[i][j] = dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]
                    else:
                        if c == sub_p[0]:
                            dp[i][j] = dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]
                        else:
                            dp[i][j] = dp[i-1][j]
                elif sub_p == '.':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if sub_p == c:
                        dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]

    def normalize_pattern(self, p):
        result = []
        for c in p:
            if c == '*':
                result[-1] = result[-1] + c
            else:
                result.append(c)
        return result
# @lc code=end


solve = Solution().isMatch


def test_default():
    assert not solve('aa', 'a')
    assert solve('aa', 'a*')
    assert solve('abcd', 'a.*d')
    assert solve('ab', '.*')
    assert solve('aab', 'c*a*b')
    assert solve('aaa', 'ab*ac*a')
    assert solve('aasdfasdfasdfasdfas', 'aasdf.*asdf.*asdf.*asdf.*s')
    assert solve('baabbbaccbccacacc', 'c*..b*a*a.*a..*c')


def test_corner_cases():
    assert solve('a', 'a')
    assert not solve('a', 'b')
    assert solve('a', '.')
    assert solve('a', '.*')
