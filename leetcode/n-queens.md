# 51. N-Queens

* *Difficulty: Hard*

* *Topics: Backtracking*

* *Similar Questions:*

  * [N-Queens II](n-queens-ii.md)

  * [Grid Illumination](grid-illumination.md)

## Problem:

<p>The <em>n</em>-queens puzzle is the problem of placing <em>n</em> queens on an <em>n</em>&times;<em>n</em> chessboard such that no two queens attack each other.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2018/10/12/8-queens.png" style="width: 258px; height: 276px;" /></p>

<p>Given an integer <em>n</em>, return all distinct solutions to the <em>n</em>-queens puzzle.</p>

<p>Each solution contains a distinct board configuration of the <em>n</em>-queens&#39; placement, where <code>&#39;Q&#39;</code> and <code>&#39;.&#39;</code> both indicate a queen and an empty space respectively.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 4
<strong>Output:</strong> [
 [&quot;.Q..&quot;,  // Solution 1
  &quot;...Q&quot;,
  &quot;Q...&quot;,
  &quot;..Q.&quot;],

 [&quot;..Q.&quot;,  // Solution 2
  &quot;Q...&quot;,
  &quot;...Q&quot;,
  &quot;.Q..&quot;]
]
<strong>Explanation:</strong> There exist two distinct solutions to the 4-queens puzzle as shown above.
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ret;
        vector<int> path;
        vector<bool> colVisited (n, false);
        helper(n, 0, path, colVisited, ret);
        return ret;
    }
    
    vector<string> generateSolution(vector<int>& path) {
        int n = path.size();
        string row = string(n, '.');
        vector<string> solution;
        for (int i = 0; i < n; ++i) {
            solution.push_back(row);
            solution.back()[path[i]] = 'Q';
        }
        return solution;
    }
    
    bool diagonal(int row, int col, vector<int>& path) {
        int n = path.size();
        for (int i = 0; i < n; ++i) {
            if (abs(row - i) == abs(col - path[i])) return true;
        }
        return false;
    }
    
    void helper(int n, int pos, vector<int>& path, vector<bool>& colVisited, vector<vector<string>>& ret) {
        if (n == pos) {
            ret.push_back(generateSolution(path));
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
