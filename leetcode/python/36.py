# 36. Valid Sudoku

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = 9

        def valid_squares() -> bool:
            for i in range(0, size, 3):
                for j in range(0, size, 3):
                    if not valid_square(i, j):
                        return False
            return True

        def valid_square(start_row: int, start_col: int) -> bool:
            count = set()
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j].isnumeric():
                        # print(board[i][j])
                        if board[i][j] in count:
                            return False
                        count.add(board[i][j])
            return True

        def valid_rows() -> bool:
            for i in range(size):
                count = set()
                for j in range(size):
                    if board[i][j].isnumeric():
                        # print(board[i][j])
                        if board[i][j] in count:
                            return False
                        count.add(board[i][j])
            return True

        def valid_columns() -> bool:
            for i in range(size):
                count = set()
                for j in range(size):
                    if board[j][i].isnumeric():
                        # print(board[j][i])
                        if board[j][i] in count:
                            return False
                        count.add(board[j][i])
            return True

        return all([valid_squares(), valid_rows(), valid_columns()])


def test():
    solver = Solution()

    example_1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert solver.isValidSudoku(example_1) == True

    example_2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert solver.isValidSudoku(example_2) == False

    print("All tests passed!")
