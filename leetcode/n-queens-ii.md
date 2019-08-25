# 52. N-Queens II

* *Difficulty: Hard*

* *Topics: Backtracking*

* *Similar Questions:*

  * [N-Queens](n-queens.md)

## Problem:

<p>The <em>n</em>-queens puzzle is the problem of placing <em>n</em> queens on an <em>n</em>&times;<em>n</em> chessboard such that no two queens attack each other.</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/8-queens.png" style="width: 258px; height: 276px;" /></p>

<p>Given an integer&nbsp;<em>n</em>, return the number of&nbsp;distinct solutions to the&nbsp;<em>n</em>-queens puzzle.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two distinct solutions to the 4-queens puzzle as shown below.
[
&nbsp;[&quot;.Q..&quot;, &nbsp;// Solution 1
&nbsp; &quot;...Q&quot;,
&nbsp; &quot;Q...&quot;,
&nbsp; &quot;..Q.&quot;],

&nbsp;[&quot;..Q.&quot;, &nbsp;// Solution 2
&nbsp; &quot;Q...&quot;,
&nbsp; &quot;...Q&quot;,
&nbsp; &quot;.Q..&quot;]
]
</pre>

## Solutions:

```c++
class Solution {
public:
    int totalNQueens(int n) {
        int ret = 0;
        vector<int> path;
        vector<bool> colVisited (n, false);
        helper(n, 0, path, colVisited, ret);
        return ret;
    }
    
    bool diagonal(int row, int col, vector<int>& path) {
        int n = path.size();
        for (int i = 0; i < n; ++i) {
            if (abs(row - i) == abs(col - path[i])) return true;
        }
        return false;
    }
    
    void helper(int n, int pos, vector<int>& path, vector<bool>& colVisited, int& ret) {
        if (n == pos) {
            ++ret;
            return;
        }
        
        for (int i = 0; i < n; ++i) {
            if (colVisited[i] || diagonal(pos, i, path)) continue;
            path.push_back(i);
            colVisited[i] = true;
            helper(n, pos + 1, path, colVisited, ret);
            colVisited[i] = false;
            path.pop_back();
        }
    }
};
```
