from collections import deque
class Node:
    def __init__(self,val) -> None:
        self.left = None
        self.right = None
        self.val = val


def leftview(root):
    if root == None:
        return None
    queue = deque([root])
    ans = []
    while queue:
        len_queue = len(queue)
        for i in range(len_queue):
            node = queue.popleft()
            if i == 0:
                ans.append(node.val)

            if node.left:
                queue.append(node.left)
            elif node.right:
                queue.append(node.right)
    return ans

def rightview(root):
    if root == None:
        return None
    queue = deque([root])
    ans = []
    while queue:
        len_queue = len(queue)
        for i in range(len_queue):
            node = queue.popleft()
            if i ==0:
                ans.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return ans

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(5)
#print(leftview(root))
print(rightview(root))


#      1
#     2  3
#   4
#  5 