## [42. 接雨水](https://leetcode-cn.com/problems/trapping-rain-water/)

给定 *n* 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png)

```
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

```

**示例 2：**

```
输入：height = [4,2,0,3,2,5]
输出：9
```

**提示：**

```
n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105
```



## 官方题解（自己完全没有思路）

**暴力法最直白**

对于第i个柱子，其左边柱子最高为left_max​，右边柱子最高为$right_max，则第i个柱子能接的雨水量为min(left_max-right_max) - height[i]。

遍历所有柱子，分别计算每个柱子能接收的雨水量，做累加即可。

**双指针法：暴力法进一步优化**

暴力法中，遍历每个柱子，对每个柱子都计算了其左边和右边的最高柱子的高度，这个计算最高柱子的高度的过程存在冗余，可优化。

双指针法，初始时，令left、right分别指向左、右两端的柱子，left、right指向的是当前要计算容量的柱子。在移动left、right的过程中，实时left_max和right_max，left_max和right_max代表的是height[0..left]和height[right..end]的最高柱子高度。

如果left_max < right_max，则计算left指向柱子的接水量；
否则，计算right指向柱子的接水量。

注意，此时的left_max是left指针左边的最高柱子，但是right_max并不一定是left指针右边最高的柱子。但是，这样也可以得出正确的结果。因为我们关注的是min(left_max, right_max)，对于上图情况，已经知道了left_max < right_max，至于这个right_max是不是右边最大的，不重要。重要的是height[i]能够装的水只和较低的left_max之差有关。

## 双指针官方代码

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        res = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[0], height[-1]
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
        return res

```

