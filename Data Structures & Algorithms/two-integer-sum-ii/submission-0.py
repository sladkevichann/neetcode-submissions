class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numdict = {}
        for i in range(len(numbers)):
            if target - numbers[i] in numdict:
                return [min(i, numdict[target - numbers[i]]) + 1, max(i, numdict[target - numbers[i]]) + 1]
            numdict[numbers[i]] = i
            