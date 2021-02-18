class Solution:
    def threeSumClosest(nums, target):
        # nums: List[int], target: int
        # return  best -> int
        # author : zhang yiming
        n = len(nums)
        best = 10 ** 5
        nums.sort()

        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ == target:
                    return target

                if abs(sum_ - target) < abs(best - target):
                    best = sum_

                if sum_ > target:
                    k -= 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
        return best

if __name__ == '__main__':
    nums = [1, 1, 1, 0]
    target = 100
    print(Solution.threeSumClosest(nums, target))





