class Solution(object):
    def plusOne(self, digits):
        carry = 0
        digits.reverse()

        digits[0] += 1
        for i in range(len(digits)):
            carry, digits[i] = divmod((digits[i] + carry), 10)
            print(carry, digits[i])

        if(carry):
            digits.append(1)
        digits.reverse()
        return digits

sl = Solution()
print(sl.plusOne([1,2,9]))
