# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/3/23 19:56
# @author  : Mo
# @function: 36. Valid Sudoku


"""36. Valid Sudoku
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
通过次数61,618提交次数104,834"""


from collections import Counter
from typing import List


class Solution:
    # 自己写的暴力法, Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    # 题目看错了......  数独:九宫格只计算9个3*3的
    def isValidSudokumy(self, board: List[List[str]]) -> bool:
        len_row = len(board[0]) # 行
        len_column= len(board) # 列
        for i in range(len_row):
            row_counter = dict(Counter(board[i]))
            if "." in row_counter: row_counter.pop(".")
            for rc in row_counter.values():
                if rc >= 2:
                    return False
        for j in range(len_column):
            column_list = []
            for k in range(len_row):
                column_list.append(board[k][j])
                column_counter = dict(Counter(column_list))
                if "." in column_counter: column_counter.pop(".")
                for rc in column_counter.values():
                    if rc >= 2:
                        return False
        for m in range(0, len_row-3+1, 3):
            for n in range(0, len_column-3+3, 3):
                col_row_list = [board[i][j] for i in range(m,m+3) for j in range(n, n+3)]
                column_counter = dict(Counter(col_row_list))
                if "." in column_counter: column_counter.pop(".")
                for rc in column_counter.values():
                    if rc >= 2:
                        return False

        return True


    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True




if __name__ == '__main__':
    sol = Solution()
    board = [[".",".",".",".",".",".","5",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".",".","."],
             ["9","3",".",".","2",".","4",".","."],
             [".",".","7",".",".",".","3",".","."],
             [".",".",".",".",".",".",".",".","."],
             [".",".",".","3","4",".",".",".","."],
             [".",".",".",".",".","3",".",".","."],
             [".",".",".",".",".","5","2",".","."]]
    res = sol.isValidSudokumy(board)
    print(res)
    gg = 0










