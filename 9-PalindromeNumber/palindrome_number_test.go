package main

import (
	"testing"
)

func TestIsPalindrome(t *testing.T) {
	tests := []struct {
		input    int
		expected bool
	}{
		{input: 121, expected: true},
		{input: -121, expected: false},
		{input: 10, expected: false},
		// Add more test cases as needed
	}

	for _, test := range tests {
		result := isPalindrome(test.input)
		if result != test.expected {
			t.Errorf("For %d, expected %t but got %t", test.input, test.expected, result)
		}
	}
}
