# 505. The Maze II

* *Difficulty: Medium*

* *Topics: Depth-first Search, Breadth-first Search*

* *Similar Questions:*

  * [The Maze](the-maze.md)

  * [The Maze III](the-maze-iii.md)

## Problem:

<p>There is a <b>ball</b> in a maze with empty spaces and walls. The ball can go through empty spaces by rolling <b>up</b>, <b>down</b>, <b>left</b> or <b>right</b>, but it won&#39;t stop rolling until hitting a wall. When the ball stops, it could choose the next direction.</p>

<p>Given the ball&#39;s <b>start position</b>, the <b>destination</b> and the <b>maze</b>, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of <b>empty spaces</b> traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.</p>

<p>The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input 1:</b> a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

<b>Input 2:</b> start coordinate (rowStart, colStart) = (0, 4)
<b>Input 3:</b> destination coordinate (rowDest, colDest) = (4, 4)

<b>Output:</b> 12

<b>Explanation:</b> One shortest way is : left -&gt; down -&gt; left -&gt; down -&gt; right -&gt; down -&gt; right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
<img src="https://assets.leetcode.com/uploads/2018/10/12/maze_1_example_1.png" style="width: 100%; max-width:350px;" />
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input 1:</b> a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

<b>Input 2:</b> start coordinate (rowStart, colStart) = (0, 4)
<b>Input 3:</b> destination coordinate (rowDest, colDest) = (3, 2)

<b>Output:</b> -1

<b>Explanation:</b> There is no way for the ball to stop at the destination.
<img src="https://assets.leetcode.com/uploads/2018/10/13/maze_1_example_2.png" style="width: 100%; max-width:350px;" />
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>There is only one ball and one destination in the maze.</li>
	<li>Both the ball and the destination exist on an empty space, and they will not be at the same position initially.</li>
	<li>The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.</li>
	<li>The maze contains at least 2 empty spaces, and both the width and height of the maze won&#39;t exceed 100.</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    int shortestDistance(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
        int m = maze.size();
        if (m == 0) return 0;
        int n = maze[0].size();
        if (n == 0) return 0;
        vector<vector<int>> dists(m, vector<int>(n, INT_MAX)); // dist is important
        priority_queue<pair<int, vector<int>>, vector<pair<int, vector<int>>>, greater<pair<int, vector<int>>>> q;
        if (start == destination)   return 0;
        
        q.push({0, start});
        dists[start[0]][start[1]] = 0;
        maze[start[0]][start[1]] = -1;
        
        while (!q.empty()) {
            
            auto coord = q.top(); q.pop();
            for (int d = 0; d < 4; ++d) {
                int x = coord.second[0], y = coord.second[1], dist = dists[x][y];
                auto newCoord = reachEnd(maze, m, n, coord.second[0], coord.second[1], directions[d][0], directions[d][1], dist);
                
                if (dists[newCoord[0]][newCoord[1]] > dist) {
                    dists[newCoord[0]][newCoord[1]] = dist;
                    if (newCoord[0] != destination[0] || newCoord[1] != destination[1]) q.push({dist, {newCoord[0], newCoord[1]}});
                }
            }
            
        }
        
        int res = dists[destination[0]][destination[1]];
        return (res == INT_MAX) ? -1 : res;
    }
    
private:
    vector<int> reachEnd(vector<vector<int>>& maze, int m, int n, int x, int y, int deltaX, int deltaY, int& dist) {
        do {
            x += deltaX;
            y += deltaY;
            ++dist;
        } while (x >= 0 && x < m && y >= 0 && y < n && maze[x][y] != 1);
        
        --dist;
        return {x - deltaX, y - deltaY};
    }
    
    int directions[4][2] {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1}
    };
    
};
```
