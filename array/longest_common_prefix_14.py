# Longest Common Prefix is a common problem where we are given a list of strings and we need to find the longest common prefix among them. The approach we can take is to start with the first string as the prefix and then compare it with each subsequent string in the list. We can iterate through the characters of the strings and keep updating the prefix until we find a mismatch or reach the end of one of the strings.
# Time complexity: O(n+m) where n is the length of the shortest string in the list, we have to iterate through the characters of the strings to find the common prefix
# Space complexity: O(1) because we are only storing the prefix which can be at most the length of the shortest string in the list

def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix