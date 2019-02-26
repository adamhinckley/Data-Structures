class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # If value is greater than self.value and self.right is empty,
        # self.right becomes the passed in value
        if value > self.value and self.right is None:
            self.right = BinarySearchTree(value)
#
        # if value is less than self.value and self.left is empty,
        # self.left becomes the passed in value
        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
#
        # if either self.left or self.right have an existing value,
        # insert the passed in value based on if left or right is greater
        if value > self.value:
            self.right.insert(value)

        if value < self.value:
            self.left.insert(value)

    def contains(self, target):
        # check if self.value is equal to target
        if self.value == target:
            return True
        # check if there is an existing value in left or right
        elif not self.left and not self.right:
            return False
        # if target is greater than self.value; self.right contains the target
        elif target > self.value:
            return self.right.contains(target)
        # if targer us less than self.value; self.left contains the target
        elif target < self.value:
            return self.left.contains(target)

    def get_max(self):
        pass
