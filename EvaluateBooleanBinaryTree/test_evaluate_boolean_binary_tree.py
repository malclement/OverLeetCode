import unittest

from evaluate_boolean_binary_tree import Solution


class TestEvaluateTree(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_single_leaf_true(self):
        root = TreeNode(1)
        self.assertTrue(self.solution.evaluateTree(root))
    
    def test_single_leaf_false(self):
        root = TreeNode(0)
        self.assertFalse(self.solution.evaluateTree(root))
    
    def test_simple_or_true(self):
        root = TreeNode(2, TreeNode(1), TreeNode(0))
        self.assertTrue(self.solution.evaluateTree(root))
    
    def test_simple_or_false(self):
        root = TreeNode(2, TreeNode(0), TreeNode(0))
        self.assertFalse(self.solution.evaluateTree(root))
    
    def test_simple_and_true(self):
        root = TreeNode(3, TreeNode(1), TreeNode(1))
        self.assertTrue(self.solution.evaluateTree(root))
    
    def test_simple_and_false(self):
        root = TreeNode(3, TreeNode(1), TreeNode(0))
        self.assertFalse(self.solution.evaluateTree(root))
    
    def test_complex_tree(self):
        # Tree structure:
        #        2
        #       / \
        #      3   0
        #     / \
        #    1   0
        root = TreeNode(2, 
                        TreeNode(3, TreeNode(1), TreeNode(0)), 
                        TreeNode(0))
        self.assertFalse(self.solution.evaluateTree(root))
    
    def test_complex_tree_with_all_true(self):
        # Tree structure:
        #        2
        #       / \
        #      3   1
        #     / \
        #    1   1
        root = TreeNode(2, 
                        TreeNode(3, TreeNode(1), TreeNode(1)), 
                        TreeNode(1))
        self.assertTrue(self.solution.evaluateTree(root))

if __name__ == '__main__':
    unittest.main()