class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # inserts at beginning
    def push(self, node):
        node.next = self.head
        self.head = node

    # inserts at end
    def append(self, node):
        if not self.head:
            self.head = node
            return
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = node

    # removes and returns last node
    def pop(self):
        curr = self.head
        if curr.next == None:
            tmp = curr
            self.head = None
            return curr
        while curr.next:
            if curr.next.next == None:
                tmp = curr.next
                curr.next = None
                return tmp
            else:
                curr = curr.next

    # swaps two nodes
    def swap(self, val1, val2):
        if not self.head or not self.head.next:
            return None

        if val1 == val2:
            return None

        # keep track of nodes _previous_ to val1 and val2
        prev_left = None
        curr_left = self.head
        while curr_left and curr_left.val != val1:
            prev_left = curr_left
            curr_left = curr_left.next

        prev_right = None
        curr_right = self.head
        while curr_right and curr_right.val != val2:
            prev_right = curr_right
            curr_right = curr_right.next

        # if either val1 or val2 isn't found, exit
        if not curr_left or not curr_right:
            return None

        # check if val1 is head
        if not prev_left:
            self.head = curr_right
        # if not, adjust prev_left.next pointer
        else:
            prev_left.next = curr_right

        # check if val2 is head
        if not prev_right:
            self.head = curr_left
        # if not, adjust prev_left.next pointer
        else:
            prev_right.next = curr_left

        # fix pointers
        tmp = curr_left.next
        curr_left.next = curr_right.next
        curr_right.next = tmp

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.val)
            tmp = tmp.next


my_list = LinkedList()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

my_list.append(node1)
my_list.append(node2)
my_list.append(node3)

my_list.print_list()

my_list.swap(1, 2)

my_list.print_list()
