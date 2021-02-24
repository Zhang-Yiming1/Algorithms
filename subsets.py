class Solution:
    def subsets(nums):
        # nums: List[int]
        # return  -> List[List[int]]
        res  = [[]]

        for i in nums:
            for j in res:
                print(j)
                res = res + [j + [i]]
                #res.append(j + [i]) # 此处 res发生了变化,只是添加了元素，不是添加列表
        return res

# class Solution:
#     def subsets(nums):
#         res = [[]]
#         for i in nums:
#             res = res + [[i] + num for num in res] # 此处先变化 [i] + num
#         return res

# 【循环】与 for循环 在此处有区别 ！！！


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution.subsets(nums))
