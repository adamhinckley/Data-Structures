class Heap:
    def __init__(self):
        self.storage = []

    # insert the value into the heap
    def insert(self, value):
        # add value the end of the array
        self.storage.append(value)
        # run bubble up
        self._bubble_up(len(self.storage) - 1)

    def delete(self):

        last_item = self.storage.pop()

        if self.storage:

            deleted = self.storage[0]

            self.storage[0] = last_item

            self._sift_down(0)

            return deleted
        else:
            return last_item

    # get the max element in constant time
    def get_max(self):
        # return whatever is at storage[0]
        if self.get_size() > 0:
            return self.storage[0]

    def get_size(self):
        return len(self.storage)

    # called as a helper function in insert
    # "bubble up" the newly inserted element to a valid spot in the heap

    def _bubble_up(self, index):
        # we'll use the child to parent formula here
        # loop while the parent index is a valid heap index
        while (index - 1) // 2 >= 0:
            # child has access to parent at this point with this formula
            # compare the child value against it's parent's value
            # if child's value > parent's value
            if self.storage[(index - 1) // 2] < self.storage[index]:
                # swap these two elements via their indices
                self.storage[index], self.storage[(
                    index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
        # repeat this process until child no longer needs to be swapped with parent
        # update the index to be the parent's index
            index = (index - 1) // 2


# called as a helper function in delete
# 'sifts down' the element at the top of the heap


    def _sift_down(self, index):
        while index * 2 + 1 <= len(self.storage) - 1:
            if index * 2 + 2 > len(self.storage) - 1:
                maxSize = index * 2 + 1
            elif self.storage[index * 2 + 1] > self.storage[index * 2 + 2]:
                maxSize = index * 2 + 1
            else:
                maxSize = index * 2 + 2

            if self.storage[maxSize] > self.storage[index]:
                self.storage[maxSize], self.storage[index] = self.storage[index], self.storage[maxSize]
            index = maxSize

            # left_child = (2 * index) + 1
            # right_child = (2 * index) + 2
            # parent_index = (index -1) // 2


# [10, 8, 7, 6, 5, 5, 2, 1]
