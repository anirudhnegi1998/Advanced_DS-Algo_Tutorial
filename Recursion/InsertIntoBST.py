from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right,val)
        return root


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
tree = list_to_tree([4,2,7,1,3])
print(s.insertIntoBST(tree, 5))

