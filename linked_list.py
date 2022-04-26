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
            print(tmp.val, end='->')
            tmp = tmp.next


# only works on sorted lists
def recursive_merge(list1, list2):
    # Create a temp node
    temp = None

    # Base Cases: list1 or list2 are empty
    if not list1:
        return list2

    if not list2:
        return list1

    # compare data and recurse
    if list1.val <= list2.val:
        # assign temp to smaller value
        temp = list1
        # and recurse
        temp.next = recursive_merge(list1.next, list2)
    else:
        # assign temp to smaller value
        temp = list2
        temp.next = recursive_merge(list1, list2.next)

    # return full list
    return temp


my_list = LinkedList()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

my_list.append(node1)
my_list.append(node2)
my_list.append(node3)

my_list.print_list()
print('\n')

my_list.swap(1, 2)

my_list.print_list()
print('\n')

# Sort my_list
my_list.swap(1, 2)

my_list.print_list()
print('\n')

# Merge!

my_list2 = LinkedList()
node4 = ListNode(4)
node5 = ListNode(5)
node2_2 = ListNode(2)
node3_3 = ListNode(3)

my_list2.append(node2_2)
my_list2.append(node3_3)
my_list2.append(node4)
my_list2.append(node5)

my_list2.print_list()
print('\n')

# create new merged_lists as a LinkedList()
merged_lists = LinkedList()

# Must supply list.head (LinkedList obj has no 'val' attribute)
# that is, we're merging the nodes b/c merged_lists() has no concept
# of the LinkedList object. We fill merged_lists with the nodes
merged_lists.head = recursive_merge(my_list.head, my_list2.head)

# can print list b/c merged_lists is a LinkedList object
merged_lists.print_list()
print('\n')

