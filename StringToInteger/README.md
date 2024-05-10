# Problem Description

The `myAtoi` function converts a given string to a 32-bit signed integer based on the following algorithm:

1. Whitespace: Ignore any leading whitespace (" ").
2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
4. Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. Specifically, integers less than -2^31 should be rounded to -2^31, and integers greater than 2^31 - 1 should be rounded to 2^31 - 1.
5. Return the integer as the final result.

## Example:

Input: "42"
Output: 42

Input: " -042"
Output: -42

Input: "1337c0d3"
Output: 1337

Input: "0-1"
Output: 0

Input: "words and 987"
Output: 0

## Constraints:

- 0 <= s.length <= 200
- s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

# Solutions Implemented

1. **Python**:

   - A Python implementation that follows the provided algorithm. It iterates through the string, skipping leading whitespace and determining the sign if present. Then, it reads digits until a non-digit character is encountered or the end of the string is reached. It checks for overflow during the conversion and returns the result accordingly, taking into account the sign.

2. **C++**:

   - A C++ implementation that directly manipulates characters in the string and performs integer conversion without the overhead of Python's dynamic typing and memory management. As a result, it is likely to be faster for large inputs.

3. **C#**:

   - A C# implementation that follows a similar approach to the Python version but is written in C#. It should provide similar performance characteristics but in the context of the C# language.

4. **Rust**:
   - A Rust implementation that follows the same logic as the Python and C++ versions but is written in Rust. It should provide similar performance characteristics but in the context of the Rust language.

## Running Tests

To run the test file execute the following command:

```bash
python3 test_longest_sub_str.py
```
