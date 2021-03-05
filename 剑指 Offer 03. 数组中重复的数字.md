### [剑指 Offer 03. 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)

找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 


限制：

2 <= n <= 100000

### 自己的代码

```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        if n > 1:
            for i in range(n-1):
                if nums[i] == nums[i+1]:
                    return nums[i]
                    break
        
        return []

               
```

复杂度高

### 官方题解

### 思路一：哈希表

1. 用哈希表记录已经出现过的数字
2. 一旦遍历到的当前数字已经在哈希表中出现过，说明是重复数字，返回该数字

```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                return num
            hashmap[num] = 1

```



**复杂度分析**

- 时间复杂度：O(n)
- 空间复杂度：O(n)

作者：edelweisskoko
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/solution/jian-zhi-offer-03-shu-zu-zhong-zhong-fu-lehnz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。