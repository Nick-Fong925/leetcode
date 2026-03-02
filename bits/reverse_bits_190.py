'''
Didn't even know to start kind of need to brush up on bit stuff

Time complexity: O(1) we are doing a fixed number of operations regardless of the input size
Space complexity: O(1) we are using a constant amount of space to store the binary
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        for i in range(32):
            if n & (1 << i):
                binary += "1"
            else:
                binary += "0"

        res = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                res |= (1 << i)

        return res
        