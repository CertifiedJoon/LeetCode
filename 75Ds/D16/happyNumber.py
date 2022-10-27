class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        if n <= 0:
            return False

        while n != 1:
            seen.add(n)
            n = sum([pow(int(c),2) for c in str(n)])
            if n in seen:
                return False
        
        return True

    def getNext(slef, n):
        next = 0
        while n > 0:
            d = n % 10
            n //= 10
            next += d * d 
        return next

    def isHappy_floyed(self, n):
        if n <= 0:
            return False
        
        fast = slow = n 
        while fast != 1 and slow != fast:
            slow = self.getNext(n)
            fast = self.getNext(self.getNext(fast))
        
        return fast == 1