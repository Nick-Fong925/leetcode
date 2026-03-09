'''
This one was pretty bad initially -> I did not have the intuitive that this needed a hash function
-> I first thought that it was going to be an array
-> Using this method makes alot of sense basically the has function manages the index for us
-> using like key % len(map)

-> for put operation just get too the last node and then add the new node at the end
-> for the get operations iterate until you can find it it not return -1
-> remove is self explanatory

time complexity is (n/k)
space complexity is O(k+m)

'''

class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):

        self.map = [ListNode() for _ in range(1000)]
    
    def hash(self, key: int) -> int:
        return key % len(self.map)
        
    def put(self, key: int, value: int) -> None:

        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:

        cur = self.map[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1
               
    def remove(self, key: int) -> None:

        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next