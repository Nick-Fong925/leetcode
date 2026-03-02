# Thought process here should be how can I make it O(n) -> single pass, if we subtract the value and know the difference then we can check it
# Time complexity: O(n) where n is the length of the array, we have to iterate through the array once
# Space complexity: O(n) because in the worst case we have to store all the elements


def twoSum(self, nums: List[int], target: int) -> List[int]:
    prevMap = {}  # val -> index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
                return [prevMap[diff], i]
        prevMap[n] = i