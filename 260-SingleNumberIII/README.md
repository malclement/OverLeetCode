# Single Number III - Python Project

## Overview

This project implements a solution to the "Single Number III" problem, where we are given an integer array in which exactly two elements appear only once and all the other elements appear exactly twice. The goal is to find the two elements that appear only once, using an algorithm with linear runtime complexity and constant extra space.

## Solution

The solution uses the XOR operation to find the two unique numbers. The main steps are:

1. XOR all numbers in the array to get the XOR of the two unique numbers.
2. Identify a bit that is set in the XOR result, which can be used to differentiate between the two unique numbers.
3. Divide the numbers into two groups based on the identified bit and XOR each group to find the unique numbers.
