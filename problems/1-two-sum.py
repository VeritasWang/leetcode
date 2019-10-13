"""
Success
Runtime: 308 ms, faster than 41.50% of Python online submissions for Two Sum.
Memory Usage: 12.5 MB, less than 94.86% of Python online submissions for Two Sum.

"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lenth = range(len(nums))
        nums_s = [x for x in nums]
        nums_s.sort()
        for i in lenth:
            for j in lenth:
                print(i, j, nums_s[i], nums_s[j])
                if i == j:
                    continue
                sum = nums_s[i] + nums_s[j]
                if sum == target:
                    if nums_s[i] == nums_s[j]:
                        i_i = nums.index(nums_s[i])
                        i_j = nums[i_i+1:].index(nums_s[j]) + i_i + 1
                        re = [i_i, i_j]
                    else:
                        re = [nums.index(nums_s[i]), nums.index(nums_s[j])]
                        re.sort()
                    return re
                if sum > target:
                    break
                j += 1
            i += 1

"""
Best Pratice
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i:
                targetind = nums.index(diff)
                ind.append(i)
                ind.append(targetind)
                break
        ind.sort()
        return ind
"""
