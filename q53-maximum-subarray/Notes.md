# Brute Force

Calculate all the sums of intervals `[i, j]`.

Time complexity: $O(n^3)$

# DP

There are many repeated computations so the first idea came into my mind is to use DP to avoid the repeated computations. That's because the sum of interval `[i, j]` depends on the sum of `[i, j-1]`.

Subproblem:

```python
def sum(nums, i, j):
	return sum(nums, i, j-1) + nums[j]
```

Time complexity: $O(n^2)$

# Another DP

Three ways of defining the interval of subproblem of DP in string: `[i,j]`, `[i, 0]`, `[0, i]`. Thus, if I can change the subproblem slightly to define the subproblem in `[i, 0]` or `[0, i]` instead of `[i, j]`, the performance will be improved dramatically.

So the trick is to define the subproblem as 'the maximum sum of the suffixes of the array `nums[:j]`'.

```python
def max_suffix_sum(nums, i):
	return max(max_suffix_sum(nums, i-1) + nums[i], nums[i])
```

Time complexity: $O(n)$

# Divide And Conquer

A little redundant cause the code is a little complicated. The difficulty is how to define the subproblem if we wanna get the maximum continuous sum from subproblems in $O(1)$.

Time complexity: $T(n)=2T(\frac n2)+O(1) \implies O(n)$