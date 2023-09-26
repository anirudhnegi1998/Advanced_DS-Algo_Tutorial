from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val< root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
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
tree = list_to_tree([6,2,8,0,4,7,9,None,None,3,5])
print(s.lowestCommonAncestor(tree,2,8))

