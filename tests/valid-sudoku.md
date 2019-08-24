# 36. Valid Sudoku

* *Difficulty: Medium*

* *Topics: Hash Table*

* *Similar Questions:*

  * [Sudoku Solver](./tests/valid-sudoku.md)

## Problem:

<p>Determine if a&nbsp;9x9 Sudoku board&nbsp;is valid.&nbsp;Only the filled cells need to be validated&nbsp;<strong>according to the following rules</strong>:</p>

<ol>
	<li>Each row&nbsp;must contain the&nbsp;digits&nbsp;<code>1-9</code> without repetition.</li>
	<li>Each column must contain the digits&nbsp;<code>1-9</code>&nbsp;without repetition.</li>
	<li>Each of the 9 <code>3x3</code> sub-boxes of the grid must contain the digits&nbsp;<code>1-9</code>&nbsp;without repetition.</li>
</ol>

<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" style="height:250px; width:250px" /><br />
<small>A partially filled sudoku which is valid.</small></p>

<p>The Sudoku board could be partially filled, where empty cells are filled with the character <code>&#39;.&#39;</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
[
  [&quot;5&quot;,&quot;3&quot;,&quot;.&quot;,&quot;.&quot;,&quot;7&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],
  [&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;1&quot;,&quot;9&quot;,&quot;5&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],
  [&quot;.&quot;,&quot;9&quot;,&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;,&quot;.&quot;],
  [&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;3&quot;],
  [&quot;4&quot;,&quot;.&quot;,&quot;.&quot;,&quot;8&quot;,&quot;.&quot;,&quot;3&quot;,&quot;.&quot;,&quot;.&quot;,&quot;1&quot;],
  [&quot;7&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;2&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;],
  [&quot;.&quot;,&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;2&quot;,&quot;8&quot;,&quot;.&quot;],
  [&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;4&quot;,&quot;1&quot;,&quot;9&quot;,&quot;.&quot;,&quot;.&quot;,&quot;5&quot;],
  [&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;7&quot;,&quot;9&quot;]
]
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>
[
&nbsp; [&quot;8&quot;,&quot;3&quot;,&quot;.&quot;,&quot;.&quot;,&quot;7&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],
&nbsp; [&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;1&quot;,&quot;9&quot;,&quot;5&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],
&nbsp; [&quot;.&quot;,&quot;9&quot;,&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;,&quot;.&quot;],
&nbsp; [&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;3&quot;],
&nbsp; [&quot;4&quot;,&quot;.&quot;,&quot;.&quot;,&quot;8&quot;,&quot;.&quot;,&quot;3&quot;,&quot;.&quot;,&quot;.&quot;,&quot;1&quot;],
&nbsp; [&quot;7&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;2&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;],
&nbsp; [&quot;.&quot;,&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;2&quot;,&quot;8&quot;,&quot;.&quot;],
&nbsp; [&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;4&quot;,&quot;1&quot;,&quot;9&quot;,&quot;.&quot;,&quot;.&quot;,&quot;5&quot;],
&nbsp; [&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;7&quot;,&quot;9&quot;]
]
<strong>Output:</strong> false
<strong>Explanation:</strong> Same as Example 1, except with the <strong>5</strong> in the top left corner being 
    modified to <strong>8</strong>. Since there are two 8&#39;s in the top left 3x3 sub-box, it is invalid.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>A Sudoku board (partially filled) could be valid but is not necessarily solvable.</li>
	<li>Only the filled cells need to be validated according to the mentioned&nbsp;rules.</li>
	<li>The given board&nbsp;contain only digits <code>1-9</code> and the character <code>&#39;.&#39;</code>.</li>
	<li>The given board size is always <code>9x9</code>.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> hashset;
        // horizonally check
        for (int i = 0; i < 9; ++i) {
            hashset.clear();
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] == '.') {
                    continue;
                }
                if (hashset.count(board[i][j]) > 0) {
                    return false;
                }
                hashset.insert(board[i][j]);
            }
        }
        
        // vertically check
        for (int j = 0; j < 9; ++j) {
            hashset.clear();
            for (int i = 0; i < 9; ++i) {
                 if (board[i][j] == '.') {
                    continue;
                }
                if (hashset.count(board[i][j]) > 0) {
                    return false;
                }
                hashset.insert(board[i][j]);
            }
        }
        
        // check sub-boxes
        for (int m = 0; m < 3; ++m) {
            for (int n = 0; n < 3; ++n) {
                hashset.clear();
                for (int subi = 0; subi < 3; ++subi) {
                    for (int subj = 0; subj < 3; ++subj) {
                        char& cell = board[3*m + subi][3*n + subj];
                        if (cell == '.') {
                            continue;
                        }
                        if (hashset.count(cell) > 0) {
                            return false;
                        }
                        hashset.insert(cell);
                    }
                }
            }
        }
        
        return true;
        
    }
};
```
