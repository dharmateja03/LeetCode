class Node:
    def __init__(self, lower, upper, val):
        self.lower = lower
        self.upper = upper
        self.left = None
        self.right = None
        self.val = val
        
class CountIntervals:

    def __init__(self):
        self.root = Node(0, 1000000000, 0)

    def _set_range(self, node, left, right): 
        # print(left, right, node.lower, node.upper)
        if left <= node.lower and node.upper <= right: 
            node.val = node.upper - node.lower + 1
            node.left = node.right = None
            return 
        mid = (node.upper + node.lower) // 2
        if not node.left and not node.right:
            node.left = Node(node.lower, mid, mid - node.lower + 1 if node.val else 0)
            node.right = Node(mid + 1, node.upper, node.upper - (mid + 1) + 1 if node.val else 0)
        if left <= mid: 
            self._set_range(node.left, left, right)
        if right > mid: 
            self._set_range(node.right, left, right)
        node.val = node.left.val + node.right.val
        
    def add(self, left: int, right: int) -> None:
        self._set_range(self.root, left, right)

    def count(self) -> int:
        return self.root.val