class Solution:
    def fourSum(nums, target):
        # nums: List[int]  target: int
        # return  -> List[List[int]
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                first = nums[i]
                second = nums[j]
                k = j + 1
                q = n - 1
                while k < q:
                    third = nums[k]
                    fourth = nums[q]
                    sum_ = first + second + third + fourth
                    if sum_ == target:
                        result.append([first, second, third, fourth])
                        q -= 1
                        while k < q and nums[q] == nums[q + 1]:
                            q -= 1
                        k += 1
                        while k < q and nums[k] == nums[k - 1]:
                            k += 1
                    if sum_ > target:
                        q -= 1
                        while k < q and nums[q] == nums[q + 1]:
                            q -= 1
                    if sum_ < target:
                        k += 1
                        while k < q and nums[k] == nums[k - 1]:
                            k += 1
        return result

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(Solution.fourSum(nums, target))