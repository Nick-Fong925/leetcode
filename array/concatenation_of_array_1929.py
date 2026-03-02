# Intuition is that you can just use concatentation, but for an interview, they may want another solution so you can go with the Option 2
# Time complexity: O(n) where n is the length of the input list, as we need to iterate through the list once.
# Space complexity: O(n) as we are creating a new list that is twice the size of the input list.


# Option 1: Concatenation
def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
    

# Options 2: Using a loop to fill in the new list        
def getConcatenation(self, nums: List[int]) -> List[int]:
        
        arr = [0 * 2 * len(nums)]
        
        for i in range(len(nums)):
            arr[i] = nums[i]
            arr[i + len(nums)] = nums[i]
        
        return arr
        