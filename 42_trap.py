class Solution:
    def trap(height):
        #  height: List[int]
        # return
        n = len(height)
        result = 0
        for i in range(1, n - 1):
            left = 0
            right = n - 1
            max_left = max(height[left: i])
            max_right = max(height[i + 1: right + 1])

            if max_left > height[i] and max_right > height[i]:
                min_ = min(max_left, max_right)
                result = result + (min_ - height[i])

        return result


if __name__ == '__main__':
    height = [4,2,0,3,2,5]
    print(Solution.trap(height))