# 417. Pacific Atlantic Water Flow

* *Difficulty: Medium*

* *Topics: Depth-first Search, Breadth-first Search*

* *Similar Questions:*

## Problem:

<p>Given an <code>m x n</code> matrix of non-negative integers representing the height of each unit cell in a continent, the &quot;Pacific ocean&quot; touches the left and top edges of the matrix and the &quot;Atlantic ocean&quot; touches the right and bottom edges.</p>

<p>Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.</p>

<p>Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.</p>

<p><b>Note:</b></p>

<ol>
	<li>The order of returned grid coordinates does not matter.</li>
	<li>Both <i>m</i> and <i>n</i> are less than 150.</li>
</ol>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
</pre>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    vector<pair<int, int>> pacificAtlantic(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = m? matrix[0].size(): 0;
        vector <pair <int, int> >   result;
        if (!m || !n)   return result;
        vector < vector <bool> > pVisited(m, vector <bool>(n, false));
        vector < vector <bool> > aVisited(m, vector <bool>(n, false));
        for (int i = 0; i < m; ++i)
        {
            BFS(matrix, pVisited, i, 0, m, n);
            BFS(matrix, aVisited, i, n-1, m, n);
        }
        for (int j = 0; j < n; ++j)
        {
            BFS(matrix, pVisited, 0, j, m, n);
            BFS(matrix, aVisited, m-1, j, m, n);
        }
        
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                if (pVisited[i][j] && aVisited[i][j])
                    result.push_back(make_pair(i,j));
        
        return result;
        
    }
        
private:
    static const int DIRECTNUM = 4;
    static const int direction[DIRECTNUM][2]; 
    void BFS(vector <vector <int>>& matrix, vector <vector <bool>>& visited, int row, int col, int m, int n)
    {
       // cout << row << " " << col << endl;
        if (row < 0 || row >= m || col < 0 || col >= n) return;
        if (visited[row][col])  return;
        visited[row][col] = true;
        int newRow;
        int newCol;
        for (int i = 0; i < DIRECTNUM; ++i)
        {
            newRow = row + direction[i][0];
            newCol = col + direction[i][1];
            if (newRow < 0 || newRow >= m || newCol < 0 || newCol >= n) continue; 
            if (matrix[row][col] <= matrix[newRow][newCol]) BFS(matrix, visited, newRow, newCol, m, n);
        }
        
    }
        
};

const int Solution::direction[Solution::DIRECTNUM][2] = {{-1,0}, {1,0}, {0, 1}, {0,-1}};
```
