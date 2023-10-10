class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def append_at_last(self,data):
        new_node  = ListNode(data) 
        if self.head == None:
            self.head = new_node
            return
        traverse = self.head
        while(traverse.next is not None):
            traverse = traverse.next
        traverse.next = new_node
        return 

    def append_at_first(self, data):
        new_node = ListNode(data)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.val , end = " -> ")
            current_node = current_node.next
        print(None)

s = LinkList()
s.append_at_last(1)
s.append_at_last(2)
s.append_at_last(3)
s.append_at_last(4)
s.append_at_last(5)
s.print()


            
    
        
