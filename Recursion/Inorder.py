class Node:
    def __init__(self,val) -> None:
        self.left = None
        self.right = None
        self.val = val

def inorder(root):
    if root is None:
        return None
    ans = []
    def helper(root,ans):
        if root == None:
            return root
        helper(root.left,ans)
        ans.append(root.val)
        helper(root.right,ans)
    helper(root,ans)
    return ans

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left = Node(6)
print(inorder(node))