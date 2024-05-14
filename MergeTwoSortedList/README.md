# Merge Two Sorted Linked Lists

## Problem Description

Given the heads of two sorted linked lists `list1` and `list2`, merge the two lists into one sorted list. The merged list should be created by splicing together the nodes of the first two lists. The function should return the head of the merged linked list.

## Solution

The solution involves merging two sorted linked lists into a single sorted linked list. The approach we take is to use a dummy node to simplify the merging process. We then iterate through both input lists, selecting the smaller node at each step and appending it to the merged list. If one of the lists is exhausted before the other, we directly append the remaining nodes of the other list to the merged list.

## Running Tests

To run the test file execute the following command:

```bash
python3 test_longest_sub_str.py
```
