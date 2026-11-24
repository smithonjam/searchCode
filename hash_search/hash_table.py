"""哈希表查找实现。

使用 Python 内置 dict 封装键值存储，冲突处理由 Python 内部机制负责。
"""

from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class HashTable(Generic[K, V]):
    """支持插入、查找、删除和更新的哈希表。"""

    def __init__(self) -> None:
        self._storage: dict[K, V] = {}

    def put(self, key: K, value: V) -> None:
        """插入或更新键值对。

        Time Complexity:
            平均 O(1)，最坏 O(n)。

        Space Complexity:
            O(n)。
        """
        self._storage[key] = value

    def get(self, key: K, default: V | None = None) -> V | None:
        """查找指定键对应的值。

        Args:
            key: 要查找的键。
            default: 键不存在时的默认值。

        Returns:
            找到时返回值；未找到时返回 default。

        Time Complexity:
            平均 O(1)，最坏 O(n)。

        Space Complexity:
            O(1)。
        """
        return self._storage.get(key, default)

    def delete(self, key: K) -> bool:
        """删除指定键。

        Returns:
            成功删除时返回 True；键不存在时返回 False。

        Time Complexity:
            平均 O(1)，最坏 O(n)。

        Space Complexity:
            O(1)。
        """
        if key not in self._storage:
            return False
        del self._storage[key]
        return True

    def __contains__(self, key: object) -> bool:
        """判断键是否存在。"""
        return key in self._storage

    def __len__(self) -> int:
        """返回表中键值对数量。"""
        return len(self._storage)


if __name__ == "__main__":
    table: HashTable[str, int] = HashTable()

    table.put("Alice", 20)
    table.put("Bob", 25)
    table.put("Alice", 21)

    print(table.get("Alice"))  # 输出：21
    print(table.get("Tom", -1))  # 输出：-1
    print("Bob" in table)       # 输出：True

    print(table.delete("Bob"))  # 输出：True
    print(len(table))           # 输出：2
