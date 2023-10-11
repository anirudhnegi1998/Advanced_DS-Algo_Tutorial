class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def reverseboundaries(head,left,right):
    if head is None or head.next is None:
        return head 
    if left == right:
        return head
    curr_head = head
    prev_head = None
    while(left>1):
        prev_head = curr_head
        curr_head = curr_head.next
        left -=1
    curr_tail = head
    next_tail = None
    while(right>1):
        curr_tail = curr_tail.next
        right-=1
    next_tail = curr_tail.next

    def helper(curr_head, curr_tail):
        if curr_head == curr_tail:
            return curr_head
        new_head = helper(curr_head.next,curr_tail)
        curr_head.next.next = curr_head
        curr_head.next = None
        return new_head
    
    if curr_head == head:
        head = helper(curr_head, curr_tail)
        curr_head.next=next_tail
        return head
    else:
        prev_head.next = helper(curr_head, curr_tail)
        curr_head.next = next_tail
        return head

def print_ll(head):
    dummy = head
    while dummy:
        print(dummy.val, end ="->")
        dummy = dummy.next
    print(None)
    
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print_ll(head)
reverseboundaries(head,2,4)
print_ll(head)