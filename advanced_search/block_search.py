"""分块查找算法实现。

将升序数组划分为固定大小的块，每个块记录最大值。
"""

from bisect import bisect_right
from collections.abc import Sequence
from typing import NamedTuple


class Block(NamedTuple):
    """表示一个分块中的起止范围与最大值。"""

    start: int
    end: int
    maximum: int


def build_block_index(values: Sequence[int], block_size: int) -> list[Block]:
    """构建分块索引。

    Args:
        values: 已按升序排列的整数序列。
        block_size: 每个块包含的元素数量。

    Returns:
        每个块的起止索引及最大值。

    Time Complexity:
        O(n)。

    Space Complexity:
        O(n / block_size)。

    Raises:
        ValueError: block_size 小于等于 0 时抛出。
    """
    if block_size <= 0:
        raise ValueError("block_size must be greater than 0")

    blocks: list[Block] = []

    for start in range(0, len(values), block_size):
        end: int = min(start + block_size - 1, len(values) - 1)
        blocks.append(Block(start=start, end=end, maximum=values[end]))

    return blocks


def block_search(values: Sequence[int], target: int, block_size: int = 4) -> int:
    """在分块索引中查找目标值。

    Args:
        values: 已按升序排列的整数序列。
        target: 要查找的目标值。
        block_size: 每个块包含的元素数量。

    Returns:
        目标值的索引；未找到时返回 -1。

    Time Complexity:
        索引查找使用二分搜索，块内使用顺序查找：
        平均和最坏时间均为 O(n / block_size + block_size)。

    Space Complexity:
        O(n / block_size)。

    Raises:
        ValueError: block_size 小于等于 0 时抛出。
    """
    if block_size <= 0:
        raise ValueError("block_size must be greater than 0")
    if not values:
        return -1

    blocks: list[Block] = build_block_index(values, block_size)
    maxima: list[int] = [block.maximum for block in blocks]

    block_position: int = bisect_right(maxima, target)
    if block_position >= len(blocks):
        return -1

    selected_block: Block = blocks[block_position]

    for index in range(selected_block.start, selected_block.end + 1):
        if values[index] == target:
            return index
        if values[index] > target:
            break

    return -1


if __name__ == "__main__":
    sorted_data: list[int] = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

    print(block_search(sorted_data, 18, block_size=3))  # 输出：5
    print(block_search(sorted_data, 20, block_size=3))  # 输出：-1
