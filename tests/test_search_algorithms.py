import unittest

from advanced_search.block_search import block_search
from advanced_search.fibonacci_search import fibonacci_search
from advanced_search.interpolation_search import interpolation_search
from basic_search.binary_search import binary_search_iterative, binary_search_recursive
from basic_search.sequential_search import sequential_search
from hash_search.hash_table import HashTable
from tree_search.bst_search import BST


class SearchAlgorithmTests(unittest.TestCase):
    def test_sequential_search(self) -> None:
        data: list[int] = [64, 25, 12, 22, 11]

        self.assertEqual(sequential_search(data, 22), 3)
        self.assertEqual(sequential_search(data, 99), -1)

    def test_binary_search(self) -> None:
        data: list[int] = [1, 3, 5, 7, 9, 11]

        self.assertEqual(binary_search_iterative(data, 7), 3)
        self.assertEqual(binary_search_recursive(data, 11), 5)
        self.assertEqual(binary_search_iterative(data, 8), -1)

    def test_interpolation_search(self) -> None:
        data: list[int] = [10, 20, 30, 40, 50, 60]

        self.assertEqual(interpolation_search(data, 40), 3)
        self.assertEqual(interpolation_search(data, 45), -1)

    def test_fibonacci_search(self) -> None:
        data: list[int] = [2, 3, 5, 7, 11, 13, 17]

        self.assertEqual(fibonacci_search(data, 13), 5)
        self.assertEqual(fibonacci_search(data, 12), -1)

    def test_block_search(self) -> None:
        data: list[int] = [3, 6, 9, 12, 15, 18, 21, 24]

        self.assertEqual(block_search(data, 18, block_size=3), 5)
        self.assertEqual(block_search(data, 20, block_size=3), -1)

    def test_bst_search(self) -> None:
        bst: BST[int] = BST()

        for value in (50, 30, 70, 20, 40):
            bst.insert(value)

        self.assertIsNotNone(bst.search(40))
        self.assertIsNone(bst.search(100))
        self.assertEqual(list(bst.inorder()), [20, 30, 40, 50, 70])

    def test_hash_table(self) -> None:
        table: HashTable[str, int] = HashTable()

        table.put("Alice", 20)
        table.put("Bob", 25)

        self.assertEqual(table.get("Alice"), 20)
        self.assertEqual(table.get("Missing", -1), -1)
        self.assertTrue(table.delete("Bob"))
        self.assertEqual(len(table), 1)


if __name__ == "__main__":
    unittest.main()
