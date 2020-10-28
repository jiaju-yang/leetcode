#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class DPSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        current_longest = ''
        for i, c in enumerate(s):
            found_index = current_longest.find(c)
            if found_index < 0:
                current_longest = current_longest + c
                if maximum < len(current_longest):
                    maximum = len(current_longest)
            else:
                current_longest = current_longest[found_index+1:] + c
        return maximum


class OptimalDPSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_length = 0
        currently_used = {}
        for i, c in enumerate(s):
            if c in currently_used and currently_used[c] >= start:
                start = currently_used[c] + 1
            max_length = max(max_length, i - start + 1)
            currently_used[c] = i
        return max_length


Solution = OptimalDPSolution
# @lc code=end

