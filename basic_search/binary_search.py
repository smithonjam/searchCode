"""二分查找算法实现。

要求输入序列必须已经按升序排列。
"""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def binary_search_iterative(values: Sequence[T], target: T) -> int:
    """使用迭代方式执行二分查找。

    Args:
        values: 已按升序排列的序列。
        target: 要查找的目标值。

    Returns:
        目标值对应的索引；未找到时返回 -1。

    Time Complexity:
        平均 O(log n)，最坏 O(log n)。

    Space Complexity:
        O(1)。
    """
    left: int = 0
    right: int = len(values) - 1

    while left <= right:
        middle: int = left + (right - left) // 2

        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def binary_search_recursive(
    values: Sequence[T],
    target: T,
    left: int = 0,
    right: int | None = None,
) -> int:
    """使用递归方式执行二分查找。

    Args:
        values: 已按升序排列的序列。
        target: 要查找的目标值。
        left: 当前查找区间的左边界。
        right: 当前查找区间的右边界；为 None 时使用序列末尾。

    Returns:
        目标值对应的索引；未找到时返回 -1。

    Time Complexity:
        平均 O(log n)，最坏 O(log n)。

    Space Complexity:
        O(log n)，主要由递归调用栈占用。
    """
    if right is None:
        right = len(values) - 1

    if left > right:
        return -1

    middle: int = left + (right - left) // 2

    if values[middle] == target:
        return middle
    if values[middle] < target:
        return binary_search_recursive(values, target, middle + 1, right)
    return binary_search_recursive(values, target, left, middle - 1)


if __name__ == "__main__":
    ordered_data: list[int] = [1, 3, 5, 7, 9, 11, 13]

    print(binary_search_iterative(ordered_data, 7))  # 输出：3
    print(binary_search_iterative(ordered_data, 6))  # 输出：-1
    print(binary_search_recursive(ordered_data, 11))  # 输出：5
    print(binary_search_recursive(ordered_data, 12))  # 输出：-1
