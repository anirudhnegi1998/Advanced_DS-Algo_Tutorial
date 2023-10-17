from collections import deque
class Node:
    def __init__(self,val) -> None:
        self.left = None
        self.right = None
        self.val  = val

def bfs(root):
    if root == None:
        return None
    
    queue = deque([root])
    while queue:
        node = queue.popleft()

        print(node.val,end=' ')

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
bfs(root)