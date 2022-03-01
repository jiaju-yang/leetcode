#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
from typing import List
from collections import deque

# @lc code=start


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        maximums = []
        for i in range(len(nums)):
            while q and q[-1][1] <= nums[i]:
                q.pop()
            q.append((i, nums[i]))
            if q[0][0] <= i - k:
                q.popleft()
            if i >= k - 1:
                maximums.append(q[0][1])
        return maximums


# @lc code=end
solve = Solution().maxSlidingWindow


def test_default():
    assert solve([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_corner_cases():
    assert solve([1], 1) == [1]
    assert solve([1, 2], 1) == [1, 2]
    assert solve([2, 1], 1) == [2, 1]
    assert solve([2, 1], 2) == [2]
    assert solve([1, 2], 2) == [2]
    assert solve([1, 2, 3], 2) == [2, 3]
    assert solve([3, 2, 1], 2) == [3, 2]
