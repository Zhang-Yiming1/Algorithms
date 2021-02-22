class Solution:
    def sortColors(nums):
        """
        Do not return anything, modify nums in-place instead.
        nums: List[int]
        """
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        for i in range(j, n):
            if nums[i] == 1:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums
        # n = len(nums)
        # result0 = []
        # result1 = []
        # result2 = []

        # if n <= 1:
        #     return nums
        # else:
        #     for i in (nums):
        #         if i == 0:
        #             result0.append(i)
        #         if i == 1:
        #             result1.append(i)
        #         if i == 2:
        #             result2.append(i)
        # nums = result0 + result1 + result2
        # return nums

if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    print(Solution.sortColors(nums))