import unittest

from merge_two_sorted_list import Solution


class TestMergeTwoLists(unittest.TestCase):
    def list_to_nodes(self, lst):
        # Helper function to convert a list to ListNode
        dummy = ListNode()
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    def nodes_to_list(self, node):
        # Helper function to convert ListNode to a list
        result = []
        current = node
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_merge_two_empty_lists(self):
        sol = Solution()
        self.assertIsNone(sol.mergeTwoLists(None, None))

    def test_merge_one_empty_list_and_one_non_empty_list(self):
        sol = Solution()
        list1 = self.list_to_nodes([1, 2, 4])
        self.assertEqual(self.nodes_to_list(sol.mergeTwoLists(None, list1)), [1, 2, 4])
        self.assertEqual(self.nodes_to_list(sol.mergeTwoLists(list1, None)), [1, 2, 4])

    def test_merge_two_non_empty_lists(self):
        sol = Solution()
        list1 = self.list_to_nodes([1, 2, 4])
        list2 = self.list_to_nodes([1, 3, 4])
        self.assertEqual(
            self.nodes_to_list(sol.mergeTwoLists(list1, list2)), [1, 1, 2, 3, 4, 4]
        )

    def test_merge_with_one_element_each(self):
        sol = Solution()
        list1 = self.list_to_nodes([2])
        list2 = self.list_to_nodes([1])
        self.assertEqual(self.nodes_to_list(sol.mergeTwoLists(list1, list2)), [1, 2])

    def test_merge_with_different_length_lists(self):
        sol = Solution()
        list1 = self.list_to_nodes([1, 3, 5, 7])
        list2 = self.list_to_nodes([2, 4, 6, 8, 10])
        self.assertEqual(
            self.nodes_to_list(sol.mergeTwoLists(list1, list2)),
            [1, 2, 3, 4, 5, 6, 7, 8, 10],
        )


if __name__ == "__main__":
    unittest.main()
