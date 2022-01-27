#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.getMin():
            self.min_stack.append(val)

    def pop(self) -> None:
        top = self.stack.pop()
        if top == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# @lc code=end


def test_default():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    stack.push(-3)
    assert stack.getMin() == -3
    stack.pop()
    assert stack.top() == -3
    assert stack.getMin() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.getMin() == -2
