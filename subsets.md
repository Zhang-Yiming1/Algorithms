#### [78. 子集](https://leetcode-cn.com/problems/subsets/)

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

```
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```


示例 2：

```
输入：nums = [0]
输出：[[],[0]]
```

**提示**：

- $1 <= nums.length <= 10$
- $-10 <= nums[i] <= 10$
- $nums$ 中的所有元素 互不相同

#### 官方代码

思路一:  库函数

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res
```


思路二:  迭代

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res    
```



#### 解析迭代

刚开始只有

```python
res = [[]]
```

遍历$nums$

```python
示例：nums = [1,2,3]
res = [[]]
i = 1
[i] + num :[[1] + []] = [[1]]
res = [[]] + [[1]] = [[], [1]]
i = 2
[i] + num : [[2]] + [[], [1]] = [[2], [1, 2]]
res = [[], [1]] + [[2], [1, 2]] = [[], [1], [2], [1, 2]]
```



