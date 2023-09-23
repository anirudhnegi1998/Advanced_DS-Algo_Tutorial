from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            if root.val>=low and root.val<=high:
                self.sum+= root.val
            inorder(root.right)
        inorder(root)
        return self.sum


# Ignore this part as this would be given in question itself
def list_to_tree(data: List[Optional[int]]) -> Optional[TreeNode]:
    if not data:
        return None
    
    root = TreeNode(data[0])
    queue = [root]
    front = 0
    index = 1
    
    while index < len(data):
        node = queue[front]
        front = front + 1
        
        item = data[index]
        index = index + 1
        if item is not None:
            left_child = TreeNode(item)
            node.left = left_child
            queue.append(left_child)
        
        if index >= len(data):
            break

        item = data[index]
        index = index + 1
        if item is not None:
            right_child = TreeNode(item)
            node.right = right_child
            queue.append(right_child)
    
    return root

s = Solution()
tree = list_to_tree([10,5,15,3,7,None,18])
print(s.rangeSumBST(tree, 7,15))