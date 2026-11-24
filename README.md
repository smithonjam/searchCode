# Search-Algorithms

使用 Python 3.12 实现的常用查找算法与数据结构示例。

## 算法复杂度

| 算法/数据结构 | 平均时间复杂度 | 最坏时间复杂度 | 空间复杂度 |适用场景 |
|---|---:|---:|---:|---|
| 顺序查找 | O(n) | O(n) | O(1) | 无序或很小的数组 |
| 二分查找（递归） | O(log n) | O(log n) | O(log n) | 有序数组；递归调用场景 |
| 二分查找（迭代） | O(log n) | O(log n) | O(1) | 有序数组；生产环境首选 |
| 插值查找 | O(log log n) | O(n) | O(1) | 均匀分布的有序数值数组 |
| 斐波那契查找 | O(log n) | O(log n) | O(1) | 有序数组；仅涉及加减和指针移动时适用 |
| BST 查找 | O(log n) | O(n) | O(h) | 平衡或随机构造的二叉搜索树 |
| 哈希表查找 | O(1) | O(n) | O(n) | 键值快速查询 |
| 分块查找 | O(n/b + b) | O(n) | O(n/b) | 静态、有序或分块排序数据 |

## 项目结构

```text
basic_search/
├── __init__.py
├── sequential_search.py
└── binary_search.py
advanced_search/
├── __init__.py
├── interpolation_search.py
├── fibonacci_search.py
└── block_search.py
tree_search/
├── __init__.py
└── bst_search.py
hash_search/
├── __init__.py
└── hash_table.py
tests/
└── test_search_algorithms.py
```

## 运行测试

```bash
python3.12 -m unittest discover -s tests -p "test_*.py"
```
