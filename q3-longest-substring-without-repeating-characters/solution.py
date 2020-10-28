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


Solution = DPSolution
# @lc code=end

