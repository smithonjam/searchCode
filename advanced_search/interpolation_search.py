"""插值查找算法实现。

适用于分布比较均匀的升序数值序列。
"""

from collections.abc import Sequence


def interpolation_search(values: Sequence[int], target: int) -> int:
    """使用插值公式在均匀分布的升序数组中查找目标值。

    Args:
        values: 已升序排列且数值分布均匀的整数序列。
        target: 要查找的目标值。

    Returns:
        目标值的索引；未找到时返回 -1。

    Time Complexity:
        平均 O(log log n)，最坏 O(n)。

    Space Complexity:
        O(1)。
    """
    left: int = 0
    right: int = len(values) - 1

    while left <= right and values[left] <= target <= values[right]:
        if values[left] == values[right]:
            if values[left] == target:
                return left
            break

        position: int = left + (
            (target - values[left])
            * (right - left)
            // (values[right] - values[left])
        )

        if position < left or position > right:
            break

        if values[position] == target:
            return position
        if values[position] < target:
            left = position + 1
        else:
            right = position - 1

    return -1


if __name__ == "__main__":
    uniform_data: list[int] = [10, 20, 30, 40, 50, 60, 70, 80]

    print(interpolation_search(uniform_data, 50))  # 输出：4
    print(interpolation_search(uniform_data, 35))  # 输出：-1
