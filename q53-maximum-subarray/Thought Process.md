# Brute Force

Calculate all the sums of intervals $(i,j)$

Time complexity: $O(n^3)$.

# DP

There are many repeated computations so we could use DP to avoid them. Use a 2-d array `sum[i][j]​` to store the sum of interval $(i,j)$, where $i$ is from $0$ to $n-1$, and $j$ is from $i$ to $n-1$. When we compute the interval $(i, j)$, we could reuse `sum[i][j-1]`.

Subproblem:

```python
def sum(A, i, j):
	return sum(A, i, j-1) + A[j]
```

Time complexity: $O(n^2)$

# Another DP

Three ways of defining the subproblem of DP in string: `(i,j)`, `(i, 0)`, `(0, i)`

Here, if we define the subproblem using `(0, i)`, then we can get a better time complexity.

```python
def max_suffix_sum(A, i):
	return max(max_suffix_sum(A, i-1) + A[i], A[i])
```

Time complexity: $O(n)$