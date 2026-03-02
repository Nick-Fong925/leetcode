"""
This is a sliding window problem, initially felt a little unintuitive to code, but good to know
Basically process is like this:
[a, b, c, a, b, c]

you have a set of like [a,b,c] -> basically constantly adding to the set until you find a duplicate
then you save the length of the set as like a potential answer
then you keep popping values from the left side, until you pop the duplicate

[b,c]

then you keep adding

[b,c,a]

then you find a duplicate again, so you save the length of the set as a potential answer, then you keep popping values from the left side until you pop the duplicate

[c,a,b]

then you then hit another

[a,b,c]

Time complexity: O(n) where n is the length of the string, we have to iterate through the string once
Space complexity: O(min(m,n)) where m is the size of the character set and n is the length of the string, in the worst case we have to store all characters in the string in the set
"""




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()
        l = 0
        res = 0

        for i in range(len(s)):

            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[i])

            res = max(res, i - l + 1)

        return res