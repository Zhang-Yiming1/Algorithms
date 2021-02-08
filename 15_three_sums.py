# author : zhang yiming
'''
        1、数组的长度要大于2
        2、数组循环的遍历是第一位和倒数第三位
        3、数组从小到大排序，第一位大于0，就直接跳出循环
        4、第一个数选择第一个位置的时候，i=0
        5、第一个数选择第二位置的时候，要判断第二个数有没有跟第一个数重复
        6、第二个从左边开始选择，第三个从最右边开始选择
        7、三个数之和S
            7.1、当s < 0时，i += 1并跳过所有重复的nums[i]；
            7.2、当s > 0时，j -= 1并跳过所有重复的nums[j]；
            7.3、当s == 0时，记录组合[k, i, j]至res，执行i += 1和j -= 1并跳过所有重复的nums[i]和nums[j]，防止记录到重复组合。
'''
def threeSum(nums):
    n = len(nums)
    answer = []
    if n < 3:
        return answer
    else:
        nums.sort()
        print('nums_sort: ', nums)
        for i in range(n - 2):
            first = nums[i]
            print('first: ', first)
            if first > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, n-1
            while left < right:
                second = nums[left]
                third = nums[right]
                print('second: ',second)
                print('third: ', third)

                third = nums[right]
                three_sum = first + second + third
                if three_sum > 0:
                    right -= 1
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1
                elif three_sum <0:
                    left += 1
                    while right > left and nums[left] == nums[left-1]:
                        left += 1
                else:
                    answer.append([first, second, third])
                    right -= 1
                    left += 1
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1
                    while right > left and nums[left] == nums[left-1]:
                        left += 1
    return answer

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    print(threeSum(nums))

# [-1,0,1,2,-1,-4]