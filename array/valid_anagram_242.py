# Counter is a useful data structure to use, makes it much simpler, basicaally counter is just set + number of instances which can be used to verify if anagram is correct
# Time complexity: O(n) where n is the length of the string, we have to iterate through the string to count the characters
# Space complexity: O(1) because the number of characters is limited (assuming we are

from collections import Counter

def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        