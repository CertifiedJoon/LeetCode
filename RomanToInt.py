class Solution(object):
    def romanToInt(self, s):
        subtraction = {"IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90, "CD" : 400, "CM" : 900}
        sum = 0

        for k,v in subtraction.items():
            if k in s:
                sum += subtraction[k]
                s = s[:s.find(k)] + s[s.find(k)+2:]

        sum += (s.count("I")) + (s.count("V"))*5  + (s.count("X"))*10 + (s.count("L"))*50 + (s.count("C"))*100 + (s.count("D"))*500 + (s.count("M"))*1000
        return sum
