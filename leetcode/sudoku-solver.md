# 37. Sudoku Solver

* *Difficulty: Hard*

* *Topics: Hash Table, Backtracking*

* *Similar Questions:*

  * [Valid Sudoku](valid-sudoku.md)

  * [Unique Paths III](unique-paths-iii.md)

## Problem:

<p>Write a program to solve a Sudoku puzzle by filling the empty cells.</p>

<p>A&nbsp;sudoku solution must satisfy <strong>all of&nbsp;the following rules</strong>:</p>

<ol>
	<li>Each of the digits&nbsp;<code>1-9</code> must occur exactly&nbsp;once in each row.</li>
	<li>Each of the digits&nbsp;<code>1-9</code>&nbsp;must occur&nbsp;exactly once in each column.</li>
	<li>Each of the the digits&nbsp;<code>1-9</code> must occur exactly once in each of the 9 <code>3x3</code> sub-boxes of the grid.</li>
</ol>

<p>Empty cells are indicated by the character <code>&#39;.&#39;</code>.</p>

<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" style="height:250px; width:250px" /><br />
<small>A sudoku puzzle...</small></p>

<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png" style="height:250px; width:250px" /><br />
<small>...and its solution numbers marked in red.</small></p>

<p><strong>Note:</strong></p>

<ul>
	<li>The given board&nbsp;contain only digits <code>1-9</code> and the character <code>&#39;.&#39;</code>.</li>
	<li>You may assume that the given Sudoku puzzle will have a single unique solution.</li>
	<li>The given board size is always <code>9x9</code>.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        int n = 9;
        vector<vector<bool>> rows (n, vector<bool> (n, false));
        vector<vector<bool>> cols (n, vector<bool> (n, false));
        vector<vector<vector<bool>>> blocks (3, vector<vector<bool>>(3, vector<bool> (n, false)));
        
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == '.') continue;
                rows[i][board[i][j] - '1'] = true;
                cols[j][board[i][j] - '1'] = true;
                blocks[i/3][j/3][board[i][j] - '1'] = true;
            }
        }
        
        helper(board, n, 0, 0, rows, cols, blocks);
    }
    
    bool helper(vector<vector<char>>& board, int n, int row, int col, vector<vector<bool>>& rows, vector<vector<bool>>& cols, vector<vector<vector<bool>>>& blocks) {
        for (int i = row; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] != '.') continue;
                for (int val = 1; val <= 9; ++val) {
                    if (isValid(rows, cols, blocks, i, j, val)) {
                        board[i][j] = '0' + val;
                        rows[i][val-1] = true;
                        cols[j][val-1] = true;
                        blocks[i/3][j/3][val-1] = true;
                        if (helper(board, n, i, j, rows, cols, blocks))    return true;
                        blocks[i/3][j/3][val-1] = false;
                        cols[j][val-1] = false;
                        rows[i][val-1] = false;
                        board[i][j] = '.';
                    }
                }
                return false;
            }
        }
        return true;
    }
    
    bool isValid(vector<vector<bool>>& rows, vector<vector<bool>>& cols, vector<vector<vector<bool>>>& blocks, int row, int col, int val) {
        return rows[row][val-1] == false && cols[col][val-1] == false && blocks[row/3][col/3][val-1] == false;
    } 
};
```
