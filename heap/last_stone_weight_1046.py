'''
lowkey unc for this, heapq now has max heap so no need for that negative stuff in the beggining

Potential optimization that I did not do was compare the values first and see if the same lol

O(n log n) time complexity because we are doing n iterations and each iteration is log n because of the heap
O(n) space complexity because we are storing the entire list in the heap
'''


import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones.copy()
        heapq.heapify_max(heap)

        while len(heap) > 1:
            bigger = heapq.heappop_max(heap)
            smaller = heapq.heappop_max(heap)
            
            if smaller == bigger:
                continue
            else:
                heapq.heappush_max(heap, bigger - smaller)
        return heap[0] if heap else 0