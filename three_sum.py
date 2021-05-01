class Solution:
    def threeSum(self, nums):
        ret = list()
        nums.sort()
        i = 0
        while(i < len(nums)):
            target = -nums[i]
            front = i + 1
            back = len(nums) - 1
            
            while(front < back):
                summed = nums[front] + nums[back]
                if summed < target:
                    front += 1
                elif summed > target:
                    back -= 1
                else:
                    temp = [nums[i], nums[front], nums[back]]
                    ret.append(temp)
                    while(front < back and nums[front] == temp[1]):
                        front += 1
                    while(front < back and nums[back] == temp[2]):
                        back -= 1
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                  i += 1
            i += 1
        return ret
    
print(Solution().threeSum([-10,-7,-3,-9,-8,-9,-5,6,0,6,4,-15,-12,3,-12,-10,-5,-5,2,-4,13,8,-9,6,-11,11,3,-13,-3,14,-9,2,14,-5,8,-9,-7,-12,5,1,2,-6,1,5,4,-4,3,7,-2,12,10,-3,6,-14,-12,10,12,7,12,-14,-2,11,4,-10,13,-11,-4,-8,-15,-14,8,-6,-12,-14,6,7,-3,-14,-1,11,14,-6,-15,5,-13,-12,0,14,2,-11,-14,8,-15,-3,13,14,-7,-14,13,-15,10,-2,-14,13]))