"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        # init a new node
        new_node = ListNode(value)
        # check to see if anything is in the list
        if not self.head:
            # hey, we're in an empty linked list situation
            self.head = new_node
            # add the value to the head of the doubly linked list
        else:
            # add the new node before the current head
            self.head.insert_before(value)
            self.head = self.head.prev

    def remove_from_head(self):
        # check to see if anything is in the list
        if not self.head:
            return None
        else:
            self.head.delete()

    def add_to_tail(self, value):
        # init a new node
        new_node = ListNode(value)
        # check to see if anything is in the list
        if not self.tail:
            # hey, we're in an empty linked list situation
            # set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # add new node after current tail
            self.tail.insert_after(new_node)
            self.tail = new_node

    def remove_from_tail(self):
        # check to see if linked list is empty
        if not self.tail:
            return None
        else:
            # delete the current tail
            self.tail.delete()

    def move_to_front(self, node):
        pass

    def move_to_end(self, node):
        pass

    def delete(self, node):
        pass

    def get_max(self):
        pass
