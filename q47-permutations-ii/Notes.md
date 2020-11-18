# Observation

The key is to notice that when we insert the next element into the existed permutations, there are two types: insert duplicate or not. When we are inserting a duplicate, we cannot insert it into every index `[0, n]` because that will cause duplicate permutations. The only indices we can insert it into are the indices preceding the index that the duplicate element exists.
