# Common Characters in All Strings

## Problem Statement

Given a string array `words`, return an array of all characters that show up in all strings within the `words` (including duplicates). You may return the answer in any order.

### Example 1:

- **Input:** `words = ["bella","label","roller"]`
- **Output:** `["e","l","l"]`

### Example 2:

- **Input:** `words = ["cool","lock","cook"]`
- **Output:** `["c","o"]`

### Constraints:

- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of lowercase English letters.

## Solution

The solution involves finding the common characters that appear in all the strings in the array, including duplicates. The approach uses the `Counter` class from the `collections` module to keep track of the frequency of characters.

### Steps:

1. Initialize the common frequency counter with the first word's frequency counter.
2. Intersect the frequency counter with the frequency counters of the remaining words.
3. Expand the elements based on their frequency in the common frequency counter to get the result.

### Implementation

The implementation is provided in `solution.py` file.

## Running Tests

To run the tests, you can use the `unittest` framework. The test cases are provided in the `test_solution.py` file.

```sh
python -m unittest test_solution.py
```
