"""顺序查找算法实现。

适用于无序或少量元素的序列。
"""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def sequential_search(values: Sequence[T], target: T) -> int:
    """从头到尾查找目标值。

    Args:
        values: 待查找的序列。
        target: 需要查找的目标值。

    Returns:
        第一次出现目标值的索引；未找到时返回 -1。

    Time Complexity:
        平均 O(n)，最坏 O(n)。

    Space Complexity:
        O(1)。
    """
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    data: list[int] = [64, 25, 12, 22, 11, 64]

    print(sequential_search(data, 22))  # 输出：3
    print(sequential_search(data, 99))  # 输出：-1
