# https://leetcode.com/problems/spiral-matrix/

class Solution:
    # keep track of direction and traverse the matrix
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top = left = di = 0
        bot = len(matrix) - 1
        right = len(matrix[0]) - 1

        res = []

        while top <= bot and left <= right:
            if di == 0:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1
            elif di == 1:
                for i in range(top, bot + 1):
                    res.append(matrix[i][right])
                right -= 1
            elif di == 2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bot][i])
                bot -= 1
            elif di == 3:
                for i in range(bot, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
            di = (di + 1) % 4

        return res
