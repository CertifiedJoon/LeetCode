nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = "1213123adf ad"
print(s.find("3", 2))
print(s.isalnum())
print(s.isalpha())
print(s.isascii())
print(s.isdecimal())
print(s.isdigit())
print(s.islower())
print(s.isupper())
print(s.lower())
print(s.upper())
print(s.lstrip())
print(s.removeprefix("12"))
print(s.removesuffix("ad"))
print(s.replace("adf", "joon"))
print(s.rindex("d"))
print(s.split())
print(s.splitlines())
print(s.strip("wcm"))

import re

reg = r"[-/!@#$ ]{1,}"

print(re.search(reg, "Joonyoung Moon"))
print(re.split(reg, "adfadf asdflj ali 23-123//123"))
print(re.findall(reg, "asdfa23//1341!@#$019832 2341"))


print(int("0x00fa", 16))
