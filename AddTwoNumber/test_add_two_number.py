import unittest

from add_two_number import ListNode
from add_two_number import Solution


class TestAddTwoNumbers(unittest.TestCase):
    def test_addTwoNumbers(self):
        # Test case 1: 342 + 465 = 807
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        solution = Solution()
        result = solution.addTwoNumbers(l1, l2)

        self.assertEqual(result.val, 7)
        self.assertEqual(result.next.val, 0)
        self.assertEqual(result.next.next.val, 8)
        self.assertIsNone(result.next.next.next)

        # Test case 2: 0 + 0 = 0
        l1 = ListNode(0)
        l2 = ListNode(0)

        result = solution.addTwoNumbers(l1, l2)

        self.assertEqual(result.val, 0)
        self.assertIsNone(result.next)


if __name__ == "__main__":
    unittest.main()
