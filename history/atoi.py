class Solution:
    def myAtoi(self, s):
        i= 0; res = 0; sign = 1; n = len(s)
        INT_MAX = pow(2,31) - 1
        INT_MIN = - pow(2,31)

        while (i < n and (s[i] == ' ' or s[i] == '+' or s[i] == '-')):
            if s[i] == '-':
                sign = -1
                i += 1
                break
            elif s[i] == '+':
                i += 1
                break
            i += 1
        
        while (i < len(s) and ord(s[i]) >= 48 and ord(s[i]) <= 57):
            res = res * 10 + int(s[i])
            i += 1
        res *= sign

        if (res > INT_MAX):
            return INT_MAX
        elif (res < INT_MIN):
            return INT_MIN
        else:
            return res

sl = Solution()
print(sl.myAtoi(" "))