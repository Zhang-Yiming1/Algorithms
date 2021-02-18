## [18. 四数之和](https://leetcode-cn.com/problems/4sum/)

给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。



注意：

答案中不可以包含重复的四元组。



示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

## 官方题解

方法一：排序 + 双指针


最朴素的方法是使用四重循环枚举所有的四元组，然后使用哈希表进行去重操作，得到不包含重复四元组的最终答案。假设数组的长度是 $n$，则该方法中，枚举的时间复杂度为$ O(n^4)$，去重操作的时间复杂度和空间复杂度也很高，因此需要换一种思路。

为了避免枚举到重复四元组，则需要保证每一重循环枚举到的元素不小于其上一重循环枚举到的元素，且在同一重循环中不能多次枚举到相同的元素。

为了实现上述要求，可以对数组进行排序，并且在循环过程中遵循以下两点：

- 每一种循环枚举到的下标必须大于上一重循环枚举到的下标；

- 同一重循环中，如果当前元素与上一个元素相同，则跳过当前元素。

使用上述方法，可以避免枚举到重复四元组，但是由于仍使用四重循环，时间复杂度仍是 $O(n^4)$。注意到数组已经被排序，因此可以使用双指针的方法去掉一重循环。

## 以下思路是没有想到的

使用两重循环分别枚举前两个数，然后在两重循环枚举到的数之后使用双指针枚举剩下的两个数。假设两重循环枚举到的前两个数分别位于下标$i$ 和 $j$，其中 $i<j$。初始时，左右指针分别指向下标 $j+1$ 和下标 $n-1$。每次计算四个数的和，并进行如下操作：

如果和等于 $\textit{target}$，则将枚举到的四个数加到答案中，然后将左指针右移直到遇到不同的数，将右指针左移直到遇到不同的数；

- 如果和小于 $\textit{target}$，则将左指针右移一位；

- 如果和大于$ \textit{target}$，则将右指针左移一位。

使用双指针枚举剩下的两个数的时间复杂度是 $O(n)$，因此总时间复杂度是 $O(n^3)$，低于 $O(n^4)$。

**具体实现时，还可以进行一些剪枝操作：**

- 在确定第一个数之后，如果$ \textit{nums}[i]+\textit{nums}[i+1]+\textit{nums}[i+2]+\textit{nums}[i+3]>\textit{target}$，说明此时剩下的三个数无论取什么值，四数之和一定大于 $\textit{target}$，因此退出第一重循环；
- 在确定第一个数之后，如果 $\textit{nums}[i]+\textit{nums}[n-3]+\textit{nums}[n-2]+\textit{nums}[n-1]<\textit{target}$，说明此时剩下的三个数无论取什么值，四数之和一定小于 $\textit{target}$，因此第一重循环直接进入下一轮，枚举$ \textit{nums}[i+1]$；
- 在确定前两个数之后，如果 $\textit{nums}[i]+\textit{nums}[j]+\textit{nums}[j+1]+\textit{nums}[j+2]>\textit{target}$，说明此时剩下的两个数无论取什么值，四数之和一定大于$ \textit{target}$，因此退出第二重循环；
- 在确定前两个数之后，如果$ \textit{nums}[i]+\textit{nums}[j]+\textit{nums}[n-2]+\textit{nums}[n-1]<\textit{target}$，说明此时剩下的两个数无论取什么值，四数之和一定小于$ \textit{target}$，因此第二重循环直接进入下一轮，枚举 $\textit{nums}[j+1]$。

## 官方代码

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = list()
        if not nums or len(nums) < 4:
            return quadruplets
        
        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return quadruplets

```

