# BST

This method is very interesting. In a BST, we use a pointer pointing to the median. So the median value is either the value pointed to or the average of the value and its successor. The key is how to maintain the pointer. This depends on the value of the inserted num. If the inserted value is less than the value pointed to, then we might find its predecessor and set the predecessor as the new median. That is symmetric when the inserted value is larger than the current median.
