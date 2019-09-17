# 694. Number of Distinct Islands

* *Difficulty: Medium*

* *Topics: Hash Table, Depth-first Search*

* *Similar Questions:*

  * [Number of Islands](number-of-islands.md)

  * [Number of Distinct Islands II](number-of-distinct-islands-ii.md)

## Problem:

<p>Given a non-empty 2D array <code>grid</code> of 0's and 1's, an <b>island</b> is a group of <code>1</code>'s (representing land) connected 4-directionally (horizontal or vertical.)  You may assume all four edges of the grid are surrounded by water.</p>

<p>Count the number of <b>distinct</b> islands.  An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.</p>

<p><b>Example 1:</b><br />
<pre>
11000
11000
00011
00011
</pre>
Given the above grid map, return <code>1</code>.
</p>

<p><b>Example 2:</b><br />
<pre>11011
10000
00001
11011</pre>
Given the above grid map, return <code>3</code>.<br /><br />
Notice that:
<pre>
11
1
</pre>
and
<pre>
 1
11
</pre>
are considered different island shapes, because we do not consider reflection / rotation.
</p>

<p><b>Note:</b>
The length of each dimension in the given <code>grid</code> does not exceed 50.
</p>
## Solutions:

```c++
class Solution {
public:
    int numDistinctIslands(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        if (n == 0) return 0;
        
        vector<vector<bool>> visited (m, vector<bool>(n, false));
        unordered_set<string> islands;
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] && !visited[i][j]) {
                    string digest;
                    dfs(grid, visited, i, j, digest);
                    islands.insert(digest);
                }
            }
        }
        
        return islands.size();
    }
    
private:
     void dfs(const vector<vector<int>>& grid, vector<vector<bool>>& visited, int row, int col, string& digest) {
         int m = grid.size();
         int n = grid[0].size();
         
         if (row < 0 || row >= m || col < 0 || col >= n || !grid[row][col] || visited[row][col]) {
             digest.push_back('e'); // empty
             return;
         }
         
         visited[row][col] = true;
         digest.push_back('d'); dfs(grid, visited, row + 1, col, digest); // down
         digest.push_back('u'); dfs(grid, visited, row - 1, col, digest); // up
         digest.push_back('r'); dfs(grid, visited, row, col + 1, digest); // right
         digest.push_back('l'); dfs(grid, visited, row, col - 1, digest); // left
     }
    
};
```
