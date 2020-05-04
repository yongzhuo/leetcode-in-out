# !/usr/bin/python
# -*- coding: utf-8 -*-
# @time    : 2020/3/31 19:19
# @author  : Mo
# @function: 37. Sudoku Solver


"""37. 解数独
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。



一个数独。



答案被标成红色。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
通过次数22,896提交次数37,798"""

"""37. Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
通过次数22,896提交次数37,798"""


from collections import defaultdict, Counter
from typing import List


class Solution:
    def solveSudokumy(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        gg = 0
    """算法
        现在准备好写回溯函数了
        backtrack(row = 0, col = 0)。
        从最左上角的方格开始 row = 0, col = 0。直到到达一个空方格。
        
        从1 到 9 迭代循环数组，尝试放置数字 d 进入 (row, col) 的格子。
            如果数字 d 还没有出现在当前行，列和子方块中：
                将 d 放入 (row, col) 格子中。
                记录下 d 已经出现在当前行，列和子方块中。
                如果这是最后一个格子row == 8, col == 8 ：
                    意味着已经找出了数独的解。
                否则
                    放置接下来的数字。
                如果数独的解还没找到：
                将最后的数从 (row, col) 移除。
        作者：LeetCode
        链接：https://leetcode-cn.com/problems/sudoku-solver/solution/jie-shu-du-by-leetcode/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""
    def solveSudoku1(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def could_place(d, row, col):
            """
            所有数据在行、列、以及3*3中
            Check if one could place a number d in (row, col) cell
            """
            return not (d in rows[row] or d in columns[col] or \
                        d in boxes[box_index(row, col)])

        def place_number(d, row, col):
            """
            行/列/3*3最初存在的数字dict
            Place a number d in (row, col) cell
            """
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            """
            删除(回退的时候)
            Remove a number which didn't lead 
            to a solution
            """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'

        def place_next_numbers(row, col):
            """
            
            Call backtrack function in recursion
            to continue to place numbers
            till the moment we have a solution
            """
            # if we're in the last cell
            # that means we have the solution
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            # if not yet
            else:
                # if we're in the end of the row
                # go to the next row
                if col == N - 1:
                    backtrack(row + 1, 0)
                # go to the next column
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            """
            Backtracking
            """
            # if the cell is empty
            if board[row][col] == '.':
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)

        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        box_index = lambda row, col: (row // n) * n + col // n

        # init rows, columns and boxes
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)

        sudoku_solved = False
        backtrack()
    """set+回溯, 存放可用数字"""
    def solveSudoku2(self, board: List[List[str]]) -> None:
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

        empty = []  # 收集需填数位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  # 更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3) * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        def backtrack(iter=0):
            if iter == len(empty):  # 处理完empty代表找到了答案
                return True
            i, j = empty[iter]
            b = (i // 3) * 3 + j // 3
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter + 1):
                    return True
                row[i].add(val)  # 回溯
                col[j].add(val)
                block[b].add(val)
            return False

        backtrack()
    """递归+回溯, 在数独I的基础上，采用递归+回溯的方式进行探测求解，用三个字典列表对填充数字进行标记。处理好尝试失败后的状态回溯即可。
        因为最多也就只有81个空位，所以递归深度不会溢出。
        作者：luanz
        链接：https://leetcode-cn.com/problems/sudoku-solver/solution/pythondi-gui-hui-su-xiao-lu-yi-ban-dan-tong-su-yi-/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""
    def solveSudoku3(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def getLocs(board):  # 初始化，获取需要填充的位置，记录为一个栈
            locs = []
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        locs.append((row, col))
            return locs

        def getMaps(board):  # 定义三个字典，跟踪9行、9列和9块的已填充数字，采用数据结构为defaultdict
            from collections import defaultdict as dd
            rowMap = [dd(int) for _ in range(9)]
            colMap = [dd(int) for _ in range(9)]
            blockMap = [dd(int) for _ in range(9)]
            for row in range(9):
                for col in range(9):
                    if board[row][col] != '.':
                        num = int(board[row][col])
                        rowMap[row][num] += 1
                        colMap[col][num] += 1
                        bolckIndex = int(row / 3) * 3 + int(col / 3)
                        blockMap[bolckIndex][num] += 1
            return rowMap, colMap, blockMap

        def fillBoard(board, locs):  # 递归填充剩余的数独空位置
            if not locs:
                return True
            row, col = locs.pop()  # 弹出一个待填充位置
            bolckIndex = int(row / 3) * 3 + int(col / 3)
            found = False
            for num in range(1, 10):
                if found:
                    break
                if not rowMap[row][num] and not colMap[col][num] and not blockMap[bolckIndex][num]:
                    ##如果当前行、当前列和当前块均不存在该数字，则将数字更新到相应行、列、块，并尝试填充
                    rowMap[row][num] = 1
                    colMap[col][num] = 1
                    blockMap[bolckIndex][num] = 1
                    board[row][col] = str(num)
                    found = fillBoard(board, locs)  # 递归到下一层填充
                    rowMap[row][num] = 0  ##状态回溯，将填充的位置清空
                    colMap[col][num] = 0
                    blockMap[bolckIndex][num] = 0
            if not found:  ##如果本轮都无法求解，则回溯到初始状态，继续从前面再填充
                locs.append((row, col))
                board[row][col] = '.'
            return found

        rowMap, colMap, blockMap = getMaps(board)
        locs = getLocs(board)
        fillBoard(board, locs)


if __name__ == '__main__':
    sol = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    sol.solveSudoku2(board)
    print(board)
    gg = 0


















