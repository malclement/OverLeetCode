# Binary Tree Evaluation

## Problem Description

You are given the root of a full binary tree with the following properties:

- Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
- Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
- The evaluation of a node is as follows:
  - If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
  - Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.

A full binary tree is a binary tree where each node has either 0 or 2 children. A leaf node is a node that has zero children.

The goal is to return the boolean result of evaluating the root node.

## Solution Description

The solution involves creating a binary tree and a method to evaluate the tree according to the described rules. Here's the breakdown:

1. **TreeNode Class**: This class represents a node in the binary tree. It has attributes for the value of the node (`val`), the left child (`left`), and the right child (`right`).

2. **Solution Class**: This class contains the `evaluateTree` method which performs the tree evaluation.

### `evaluateTree` Method

- **Input**: The root of the binary tree.
- **Output**: A boolean value representing the result of evaluating the tree.

The method works as follows:

- If the current node is a leaf node (both left and right children are `None`), it returns the boolean value of the node (`True` for 1, `False` for 0).
- If the node is not a leaf node, it recursively evaluates the left and right children.
- Based on the value of the current node (2 for OR, 3 for AND), it combines the results of the left and right children using the appropriate boolean operation.

## Running Tests

To run the test file execute the following command:

```bash
python3 test_longest_sub_str.py
```
