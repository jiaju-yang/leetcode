class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_tree(values):
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    last_level = [root]
    curr_level = []
    while last_level:
        for node in last_level:
            try:
                val = next(it)
                node.left = TreeNode(val) if val is not None else None
                val = next(it)
                node.right = TreeNode(val) if val is not None else None
                curr_level.append(node.left)
                curr_level.append(node.right)
            except StopIteration:
                break
        last_level = curr_level
        curr_level = []
    return root
