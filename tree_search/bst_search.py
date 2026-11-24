"""二叉搜索树查找实现。

左子树节点值小于当前节点值，右子树节点值大于当前节点值。
"""

from collections.abc import Iterator
from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    """二叉搜索树节点。"""

    def __init__(self, value: T) -> None:
        self.value: T = value
        self.left: Node[T] | None = None
        self.right: Node[T] | None = None


class BST(Generic[T]):
    """支持插入、查找和中序遍历的二叉搜索树。"""

    def __init__(self) -> None:
        self.root: Node[T] | None = None
        self._size: int = 0

    def insert(self, value: T) -> None:
        """插入一个值。

        Time Complexity:
            平均 O(log n)，最坏 O(n)。

        Space Complexity:
            O(h)，h 为树高度。
        """
        if self.root is None:
            self.root = Node(value)
            self._size = 1
            return

        current: Node[T] = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    break
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    break
                current = current.right
            else:
                return

        self._size += 1

    def search(self, target: T) -> Node[T] | None:
        """查找目标值对应的节点。

        Returns:
            找到时返回节点；未找到时返回 None。

        Time Complexity:
            平均 O(log n)，最坏 O(n)。

        Space Complexity:
            O(1)。
        """
        current: Node[T] | None = self.root

        while current is not None:
            if target == current.value:
                return current
            if target < current.value:
                current = current.left
            else:
                current = current.right

        return None

    def inorder(self) -> Iterator[T]:
        """按升序生成所有节点值。"""
        stack: list[Node[T]] = []
        current: Node[T] | None = self.root

        while stack or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            yield current.value
            current = current.right

    @property
    def size(self) -> int:
        """返回树中元素数量。"""
        return self._size


if __name__ == "__main__":
    bst: BST[int] = BST()

    for value in (50, 30, 70, 20, 40, 60, 80):
        bst.insert(value)

    print(bst.search(60) is not None)  # True
    print(bst.search(25) is not None)  # False
    print(list(bst.inorder()))          # [20, 30, 40, 50, 60, 70, 80]
