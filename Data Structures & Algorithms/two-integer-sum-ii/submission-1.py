class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, back = 0, len(numbers) - 1
        while start < back:
            if (numbers[start] + numbers[back]) == target:
                return [start + 1, back + 1]
            elif (numbers[start] + numbers[back]) < target:
                start += 1
            elif (numbers[start] + numbers[back]) > target:
                back -= 1
            