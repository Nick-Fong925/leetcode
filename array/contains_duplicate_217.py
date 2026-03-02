# Overall  pretty easy, it may be intuitive to use a hash, but in this case a set works well as well" 
# Time complexity: O(n) where n is the length of the input list, as we need to iterate through the list once.
# Space complexity: O(n) in the worst case, if all elements in the input list


def containsDuplicate(self, nums: List[int]) -> bool:
        
        duplicatelist = set()

        for i in nums:
            if i in duplicatelist:
                return True
            duplicatelist.add(i)
        return False