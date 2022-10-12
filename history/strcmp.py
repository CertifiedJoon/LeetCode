class Solution:
    def isMatch(self, s, p):
        si = pi = 0
        n = len(s); m = len(p)
        while(pi < m):
            if (s[si] == p[pi]):
                prev = p[si]
                si += 1; pi += 1
            
            elif (p[pi] == '.'):
                prev = '.'
                si += 1; pi += 1
            
            elif (p[pi] = '*'):
                pi -= 1
            
            else:
                if 
                

sl = Solution()
print(sl.isMatch("aa", "a"))