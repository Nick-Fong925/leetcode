'''
Initial implementation was not optimal, I had the correct intuition to use the sliding window and Counter struct
but I was creating a new Counter for each window instead of proactively updating it with the window

The optimal solution is similar but uses that functionality
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Count = Counter(s1)
        diff = len(s1)

        if len(s2) < len(s1):
            return False
        
        for i in range(0, len(s2)-len(s1)+1):
            
            if s1Count == Counter(s2[i:i+diff]):
                return True
        return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
             
        if len(s2) < len(s1):
            return False

        s1Count = Counter(s1)
        window = Counter(s2[:len(s1)])

        if window == s1Count:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            window[s2[r]] += 1
            window[s2[l]] -= 1

            if window[s2[l]] == 0:
                del window[s2[l]]

            l += 1

            if window == s1Count:
                return True

        return False
