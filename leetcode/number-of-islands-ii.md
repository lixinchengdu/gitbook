# 305. Number of Islands II

* *Difficulty: Hard*

* *Topics: Union Find*

* *Similar Questions:*

  * [Number of Islands](number-of-islands.md)

## Problem:

<p>A 2d grid map of <code>m</code> rows and <code>n</code> columns is initially filled with water. We may perform an <i>addLand</i> operation which turns the water at position (row, col) into a land. Given a list of positions to operate, <b>count the number of islands after each <i>addLand</i> operation</b>. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
<b>Output:</b> [1,1,2,3]
</pre>

<p><b>Explanation:</b></p>

<p>Initially, the 2d grid <code>grid</code> is filled with water. (Assume 0 represents water and 1 represents land).</p>

<pre>
0 0 0
0 0 0
0 0 0
</pre>

<p>Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.</p>

<pre>
1 0 0
0 0 0   Number of islands = 1
0 0 0
</pre>

<p>Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.</p>

<pre>
1 1 0
0 0 0   Number of islands = 1
0 0 0
</pre>

<p>Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.</p>

<pre>
1 1 0
0 0 1   Number of islands = 2
0 0 0
</pre>

<p>Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.</p>

<pre>
1 1 0
0 0 1   Number of islands = 3
0 1 0
</pre>

<p><b>Follow up:</b></p>

<p>Can you do it in time complexity O(k log mn), where k is the length of the <code>positions</code>?</p>

## Solutions:

```c++
class Solution {
public:
    vector<int> numIslands2(int m, int n, vector<vector<int>>& positions) {
        UF uf;
        vector<int> ret;
        vector<vector<bool>> grid (m, vector<bool> (n, false));
        
        for (auto& position : positions) {
            int row = position[0];
            int col = position[1];
            if (grid[row][col]) {
                ret.push_back(uf.getSize());
                continue;
            }
            
            grid[row][col] = true;
            uf.add(row * n + col);
            if (row + 1 < m && grid[row + 1][col]) {
                uf.connect(row * n + col, (row + 1) * n + col);
            }
            if (row - 1 >= 0 && grid[row - 1][col]) {
                uf.connect(row * n + col, (row - 1) * n + col);
            }
            if (col + 1 < n && grid[row][col + 1]) {
                uf.connect(row * n + col, row * n + col + 1);
            }
            if (col - 1 >= 0 && grid[row][col - 1]) {
                uf.connect(row * n + col, row * n + col - 1);
            }
            
            ret.push_back(uf.getSize());
        }
        
        return ret;
    }
    
    class UF {
    public:
        int getSize() {
            return size;
        }
        
        void add(int a) {
            parents[a] = a;
            ++size;
        }
        
        void connect(int a, int b) {
            int rootA = find(a);
            int rootB = find(b);
            
            if (rootA != rootB) {
                parents[rootA] = rootB;
                --size;
            }
        }
            
        int find(int x) {
            if (parents[x] != x) {
                parents[x] = find(parents[x]);
            }
            return parents[x];
        }
    private:
        map<int, int> parents;
        int size = 0;
    };
};
```
