# 289. Game of Life

from typing import List
import copy

example1_arg1 = [[1, 1], [1, 0]]
example1_out = [[1, 1], [1, 1]]

example2_arg1 = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
example2_out = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]


class Solution:
    m = 0  # board rows
    n = 0  # board columns

    def gameOfLife(self, board: List[List[int]]) -> None:
        self.m = len(board)
        self.n = len(board[0])
        board_copy = copy.deepcopy(board)
        for i in range(0, self.m):
            for j in range(0, self.n):
                if board[i][j] == 0:
                    if self.__countNeighbors(board_copy, i, j) == 3:
                        board[i][j] = 1
                else:
                    neighbors = self.__countNeighbors(board_copy, i, j)
                    if neighbors < 2 or neighbors > 3:
                        board[i][j] = 0
                    else:
                        board[i][j] = 1
        print(board)
        return board

    def __countNeighbors(self, board: List[List[int]], i, j):
        neighbors = 0
        for row in range(i - 1, i + 2):
            for col in range(j - 1, j + 2):
                if row == i and col == j:
                    continue
                if row >= 0 and col >= 0 and row < self.m and col < self.n:
                    neighbors += board[row][col]
        return neighbors


print(Solution().gameOfLife(example1_arg1) == example1_out)
print(Solution().gameOfLife(example2_arg1) == example2_out)
