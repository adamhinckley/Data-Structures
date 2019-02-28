class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        # check to see if the item is in the queue
        if item not in self.storage:
            # add item to queue
            self.storage.insert(0, item)
            return True
        return False

    def dequeue(self):
        # check to see if anything is in the queue
        if len(self.storage) > 0:
            return self.storage.pop()
        return None

    def len(self):
        return len(self.storage)
