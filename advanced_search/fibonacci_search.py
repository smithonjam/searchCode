"""斐波那契查找算法实现。

要求输入序列按升序排列。
"""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def fibonacci_search(values: Sequence[T], target: T) -> int:
    """使用斐波那契数列将查找区间不断缩小。

    Args:
        values: 已按升序排列的序列。
        target: 要查找的目标值。

    Returns:
        目标值的索引；未找到时返回 -1。

    Time Complexity:
        平均 O(log n)，最坏 O(log n)。

    Space Complexity:
        O(1)。
    """
    length: int = len(values)
    if length == 0:
        return -1

    fib_m_minus_two: int = 0
    fib_m_minus_one: int = 1
    fib_m: int = fib_m_minus_two + fib_m_minus_one

    while fib_m < length:
        fib_m_minus_two = fib_m_minus_one
        fib_m_minus_one = fib_m
        fib_m = fib_m_minus_two + fib_m_minus_one

    offset: int = -1

    while fib_m > 1:
        probe: int = min(offset + fib_m_minus_two, length - 1)

        if values[probe] < target:
            fib_m = fib_m_minus_one
            fib_m_minus_one = fib_m_minus_two
            fib_m_minus_two = fib_m - fib_m_minus_one
            offset = probe
        elif values[probe] > target:
            fib_m = fib_m_minus_two
            fib_m_minus_one = fib_m_minus_one - fib_m_minus_two
            fib_m_minus_two = fib_m - fib_m_minus_one
        else:
            return probe

    if fib_m_minus_one == 1 and offset + 1 < length:
        if values[offset + 1] == target:
            return offset + 1

    return -1


if __name__ == "__main__":
    ordered_data: list[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    print(fibonacci_search(ordered_data, 13))  # 输出：5
    print(fibonacci_search(ordered_data, 12))  # 输出：-1
