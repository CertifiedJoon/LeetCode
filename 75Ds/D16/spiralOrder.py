
class Solution:
    def spiralOrder(self, matrix):
        #matrix_size will store the boundaries for each side of the matrix
        matrix_size = {"leftmost" : 0, "rightmost" : len(matrix[0]) - 1, "highest" : 0, "lowest" : len(matrix) - 1}
        RIGHT = 1
        LEFT = 2
        UP = 3
        DOWN = 4
        direction = RIGHT
        spiral_ordered = []

        while matrix_size['leftmost'] <= matrix_size['rightmost'] and matrix_size['highest'] <= matrix_size['lowest']:
            direction = self.move(matrix, matrix_size, spiral_ordered, direction)
        
        return spiral_ordered
    
    def move(self, matrix, matrix_size, spiral_ordered, direction):
        match direction:
            case 1:
                spiral_ordered.extend(matrix[matrix_size['highest']][matrix_size['leftmost'] : matrix_size['rightmost'] + 1])
                matrix_size['highest'] += 1
                direction = 4
            case 2:
                spiral_ordered.extend(matrix[matrix_size['lowest']][matrix_size['leftmost'] : matrix_size['rightmost'] + 1][::-1])
                matrix_size['lowest'] -= 1
                direction = 3
            case 3:
                for i in range(matrix_size['lowest'], matrix_size['highest'] - 1, -1):
                    spiral_ordered.append(matrix[i][matrix_size['leftmost']])
                matrix_size['leftmost'] += 1
                direction = 1
            case 4:
                for i in range(matrix_size['highest'], matrix_size['lowest'] + 1):
                    spiral_ordered.append(matrix[i][matrix_size['rightmost']])
                matrix_size['rightmost'] -= 1
                direction = 2
        return direction


matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix.pop(0))

## AMAZING
print([*zip(*matrix[::-1])][::-1])