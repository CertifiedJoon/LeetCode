class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        stack = [(sr, sc)] # stores the next pixel to colour
        original_color = image[sr][sc]
        rl = len(image)
        cl = len(image[0])

        if color == original_color:
            return image

        while stack:
            ri, ci = stack.pop()
            print(ri, ci, original_color)
            image[ri][ci] = color
            
            if 0 <= ri - 1 and image[ri - 1][ci] == original_color:
                stack.append((ri - 1, ci))
            if ri + 1 < rl and image[ri + 1][ci] == original_color:
                stack.append((ri + 1, ci))
            if ci - 1 >= 0 and image[ri][ci - 1] == original_color:
                stack.append((ri, ci - 1))
            if ci + 1 < cl and image[ri][ci + 1] == original_color:
                stack.append((ri, ci + 1))

        return image