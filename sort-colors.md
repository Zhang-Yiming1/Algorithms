# [75. 颜色分类](https://leetcode-cn.com/problems/sort-colors/)

# 题目描述

给定一个包含红色、白色和蓝色，一共 $n$ 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。



示例 1：

```
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
```


示例 2：

```
输入：nums = [2,0,1]
输出：[0,1,2]
```


示例 3：

```
输入：nums = [0]
输出：[0]
```


示例 4：

```
输入：nums = [1]
输出：[1]
```


提示：

- $n == nums.length$
- $1 <= n <= 300$
- $nums[i]$ 为$ 0$、$1$ 或$ 2$





# 官方题解

**循环不变量定义** 1
**循环不变量**：声明的变量在遍历的过程中需要保持定义不变。

设计循环不变量的原则
**说明：设计循环不变量的原则是 不重不漏。**

- len 是数组的长度；

- 变量 zero 是前两个子区间的分界点，一个是闭区间，另一个就必须是开区间；

- 变量 i 是循环变量，一般设置为开区间，表示 i 之前的元素是遍历过的；

- two 是另一个分界线，我设计成闭区间。

  

  如果循环不变量定义如下：

- 所有在子区间 [0, zero) 的元素都等于 0；

- 所有在子区间 [zero, i) 的元素都等于 1；

- 所有在子区间 [two, len - 1] 的元素都等于 2。

  

  于是编码要解决以下三个问题：

- 变量初始化应该如何定义；

- 在遍历的时候，是先加减还是先交换；

- 什么时候循环终止。

  

  处理这三个问题，完全看循环不变量的定义。

- 编码的时候，zero 和 two 初始化的值就应该保证上面的三个子区间全为空；

- 在遍历的过程中，「下标先加减再交换」、还是「先交换再加减」就看初始化的时候变量在哪里；

- 退出循环的条件也看上面定义的循环不变量，在 i == two 成立的时候，上面的三个子区间就正好 不重不漏 地覆盖了整个数组，并且给出的性质成立，题目的任务也就完成了。

  

  # 参考代码 1：

```python
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # all in [0, zero) = 0
        # all in [zero, i) = 1
        # all in [two, len - 1] = 2

        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        size = len(nums)
        if size < 2:
            return

        zero = 0
        two = size

        i = 0

        while i < two:
            if nums[i] == 0:
                swap(nums, i, zero)
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            else:
                two -= 1
                swap(nums, i, two)

作者：liweiwei1419
链接：https://leetcode-cn.com/problems/sort-colors/solution/kuai-su-pai-xu-partition-guo-cheng-she-ji-xun-huan/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

