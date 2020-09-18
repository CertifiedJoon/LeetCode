class Solution(object):
    def maxArea(self, height):
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        maxA = 0

        while (left < right):
            maxA = max(maxA,(right-left) * min(height[left], height[right]))
            if (height[left] > height[right]):
                right -= 1
            elif (height[left] < height[right]):
                left += 1
            else:
                if (height[left+1] > height[right-1]):
                    left += 1
                elif (height[left+1] < height[right-1]):
                    right -= 1
                else:
                    right -= 1
                    left += 1
        return maxA

sl = Solution()
print(sl.maxArea([1,8,6,2,5,8,3,7,9]))
