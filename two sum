class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        nums_with_index.sort(key=lambda x: x[0])
        l, r = 0, len(nums) - 1
        while l < r:
            if nums_with_index[l][0] + nums_with_index[r][0] > target:
                r -= 1
            elif nums_with_index[l][0] + nums_with_index[r][0] < target:
                l += 1
            else:
                return [nums_with_index[l][1], nums_with_index[r][1]]
        return False
