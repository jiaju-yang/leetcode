class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return other and other.val == self.val and other.left == self.left and other.right == self.right

    def __str__(self) -> str:
        return f'TreeNode({self.val})'

    def __repr__(self) -> str:
        return str(self)


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
