# Linked List Addition

This project provides a solution to the problem of adding two numbers represented by non-empty linked lists, where each node contains a single digit. The digits are stored in reverse order, and the goal is to return the sum as a linked list.

## Solution Overview

The solution is implemented in Python and includes a `ListNode` class representing a node in a singly-linked list and a `Solution` class with a method `addTwoNumbers` to add two numbers represented by linked lists.

## File Structure

- `solution.py`: Contains the implementation of the `Solution` class.
- `test_solution.py`: Includes unit tests for the `addTwoNumbers` method using the `unittest` framework.

## Usage

To use the solution, you can create instances of the `ListNode` class to represent the input numbers and call the `addTwoNumbers` method of the `Solution` class to get the sum as a linked list.

Example usage:

```python
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Traverse and print the result linked list
while result:
    print(result.val, end=" ")
    result = result.next
```
