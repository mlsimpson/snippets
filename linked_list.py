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
        # In case of empty list
        if not self.head:
            self.head = node
            return

        tmp = self.head
        while tmp.next:
            tmp = tmp.next

        tmp.next = node

    # removes and returns last node
    def pop(self):
        # Handles empty list
        if not self.head:
            return None

        curr = self.head
        # Handles single node list
        if curr.next == None:
            self.head = None
            return curr

        while curr.next:
            # Check if next node is end of list
            if curr.next.next == None:
                tmp = curr.next
                curr.next = None
                return tmp
            # Keep iterating if not
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
        # aka make prev_left point to the 'right' node
        else:
            prev_left.next = curr_right

        # check if val2 is head
        if not prev_right:
            self.head = curr_left
        # if not, adjust prev_right.next pointer
        # aka make prev_right poitn to the 'left' node
        else:
            prev_right.next = curr_left

        # fix swapped 'next' pointers
        tmp = curr_left.next
        curr_left.next = curr_right.next
        curr_right.next = tmp

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.val, end='->')
            tmp = tmp.next

    # only works on sorted lists
    # this merges an external list with the internal one
    # this returns a 'new list', and also overwrites the current 'self' list
    # this is _in place_
    def iterative_merge(self, list2):
        # using a dummy node handles empty case
        # this will be constantly appended to create merged list
        dummy = ListNode()
        # track the tail
        tail = dummy

        curr = self.head

        while curr and list2:
            if curr.val <= list2.val:
                tail.next = curr
                curr = curr.next
            else:
                tail.next = list2
                list2 = list2.next

            # advance the tail
            tail = tail.next

        # if there's still curr or list2, add them to list
        if curr:
            tail.next = curr
        if list2:
            tail.next = list2

        # return full list
        return dummy.next

    # this takes 2 lists and merges them
    # at the end, self.head is updated to be new sorted list
    # basically the same as above, just with an extra externally passed list
    def sorted_merge(self, head1, head2):
        dummy = ListNode()
        tail = dummy

        while head1 and head2:
            if head1.val <= head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next

            tail = tail.next

        if head1:
            tail.next = head1
        if head2:
            tail.next = head2

        self.head = dummy.next
        return dummy.next

    # This only swaps values in nodes, not the links between nodes
    # this is O(n^2) tho :(
    def bad_sort(self):
        if not self.head:
            return None

        curr = self.head
        index = None

        while curr:
            index = curr.next

            while index:
                if curr.val > index.val:
                    tmp = curr.val
                    curr.val = index.val
                    index.val = tmp
                index = index.next
            curr = curr.next

    # utility function to get middle of linked list
    # uses 'slow'/'fast' method:
    # 'slow' pointer moves at one element at a time
    # 'fast' pointer moves at two elements at a time
    # when 'fast' is at end, 'slow' is halfway
    def get_middle(self, head):
        # In case of empty list
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next

        return slow

    # divide and conquer, baby!
    # uses existing "sorted_merge()" to perform merge after dividing
    def merge_sort(self, head):
        # base case if head is none, or only 1 element in list
        if not head or not head.next:
            return head

        # get the middle element of the list
        middle = self.get_middle(head)
        # divide on element next to middle
        next_middle = middle.next

        # set middle.next to None (end of left list)
        middle.next = None

        # divide...
        left = self.merge_sort(head)
        right = self.merge_sort(next_middle)

        # ... and conquer
        sorted_list = self.sorted_merge(left, right)

        return sorted_list


# only works on sorted lists
# takes stack space proportional to lenght of both lists
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

# Driver code

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

# try out iterative merge as method of LinkedList class

my_list3 = LinkedList()
nodea = ListNode(1)
nodeb = ListNode(2)
nodec = ListNode(3)

my_list3.append(nodea)
my_list3.append(nodeb)
my_list3.append(nodec)

my_list3.print_list()
print('\n')

my_list4 = LinkedList()
noded = ListNode(4)
nodee = ListNode(5)
nodef = ListNode(6)

my_list4.append(noded)
my_list4.append(nodee)
my_list4.append(nodef)

my_list4.print_list()
print('\n')

# my_list3.iterative_merge(my_list4.head)
my_list3.sorted_merge(my_list3.head, my_list4.head)
my_list3.print_list()
print('\n')

# okay, now try sorting list as LinkedList method
my_list5 = LinkedList()
nodew = ListNode(8)
nodex = ListNode(5)
nodey = ListNode(3)
nodez = ListNode(1)

my_list5.append(nodew)
my_list5.append(nodex)
my_list5.append(nodey)
my_list5.append(nodez)

my_list5.print_list()
print('\n')

# my_list5.bad_sort()
my_list5.merge_sort(my_list5.head)
my_list5.print_list()
print('\n')

