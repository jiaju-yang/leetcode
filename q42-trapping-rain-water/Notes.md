# Find Highest First

If we use Brute Force, for each element, we must find its maximum height of bars on both sides. This is $O(n^2)$. But if we already know the maximum height of bar on one side for each element, then we could iterate the array from the other side such that we can find the water it can trap through just one loop. The natural way is to find the maximum height of bar first, and then iterate from left to the highest bar and from right to the highest bar respectively.

Time complexity: $O(n)$

Space complexity: $O(1)$

# Stack

This method is very cunning and full of wisdom but hard to coding.😂 The basic idea is to use a stack to keep track of all the bars. And when the heights become shorter, it turned out that we are at the left side of a bowl, just add the bar to the stack. But when the heights become higher, then we know we are at the right side of the bowl so now we can collect water between previous bars and current bar.

Time complexity: $O(n)$

Space complexity: $O(n)$

# Two Pointers

This is a variation of the Find Highest First solution. At each index, the water trapped is bounded by the minimum of its highest bars on both sides instead of the maximum so we don't need to find the highest. The code is self explained.

Time complexity: $O(n)$

Space complexity: $O(1)$

Cache Oblivious: $\frac MB$ better than Find Highest First $\frac {2M}B$