# DP

The only difficulty is tracking remaining uncovered chars and recomputing the start index. Recomputing is expensive so do this operation only after the start index changed.

# Another DP

This algorithm gets rid of the lists in the Counter so it has to recompute the start by the string itself. Move the start index to the right until the char cannot be excluded. Weirdly, this algorithm is slower than the previous one. 😂