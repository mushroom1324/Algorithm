class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newNums = list()
        index = 0
        for i in nums:
            newNums.append((i, index))
            index += 1

        index1 = 0
        index2 = len(nums) - 1

        newNums.sort()
        while newNums[index1][0] + newNums[index2][0] != target:
            if newNums[index1][0] + newNums[index2][0] < target:
                index1 += 1
            else:
                index2 -= 1
        return [newNums[index1][1], newNums[index2][1]]
