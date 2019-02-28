Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

    O(1) because it only ever has to do one thing and doesn't have to loop over anything

2. What is the runtime complexity of `dequeue`?

    O(1) because it only ever has to do one thing and doesn't have to loop over anything

3. What is the runtime complexity of `len`?

    O(1) because it only ever has to do one thing and doesn't have to loop over anything

## Binary Search Tree

1. What is the runtime complexity of `insert`?

    O( log n) because it uses recursion and binary search is always log n

2. What is the runtime complexity of `contains`?

    O( log n) because it uses recursion and binary search is always log n

3. What is the runtime complexity of `get_max`?

    O(log n) because it has to iterate to find the max and uses recursion

## Heap

1. What is the runtime complexity of `_bubble_up`?

    O(log n) because it uses a while loop(n) then an if statement(1)

2. What is the runtime complexity of `_sift_down`?

    O(log n) because it uses a while loop(n) then an if statement(1)

3. What is the runtime complexity of `insert`?

    inserting along is O(1) because there is no need to iterate over the value,
    but calling `_bubble_up` makes it O(log n + 1) because it uses a while loop.

4. What is the runtime complexity of `delete`?

    O(1) if it didn't use `_sift_down` but it's o(log n + 1) because of that.

5. What is the runtime complexity of `get_max`?

    O(1) because it only has to look at the fist character of the array then it's done.

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

    O(1) because no iteration is required

2. What is the runtime complexity of `ListNode.insert_before`?

    O(1) because no iteration is required

3. What is the runtime complexity of `ListNode.delete`?

    O(1) because no iteration is required

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

    O(1) because no iteration is required

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

    O(1) because no iteration is required

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

    O(1) because no iteration is required

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

    O(1) because no iteration is required

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

    O(1) because no iteration is required

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

    O(1) because no iteration is required

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    O(1) because no iteration is required

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    `worst case of array.splice is O(n) it would have to copy all of the elements to a new array`

<!-- I added this one because it was left out -->

11. What is the runtime complexity of `DoublyLinkedList.get_max`?
    o(n) because it uses a while loop to find the max
