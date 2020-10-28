# DP

The only difficulty is how to check whether the new char is already in current longest distinct suffix while getting the length of the new suffix in $O(1)$ time. The natural way is hashing, and we need some auxiliary variables to help calculating the new length and checking whether the new char is in the current longest suffix.

* Calculating needs two variables: current index and new start index
* Checking also needs two variables: previous start index and the char's previously seen index
