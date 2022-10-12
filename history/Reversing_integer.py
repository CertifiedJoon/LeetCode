class Solution(object):
    def reverse(self, x):
        s = str(abs(x)) [::-1]
        if (int(s).bit_length() > 31):
            return 0
        else:
            return(int(s) if x > 0 else (-int(s)))
