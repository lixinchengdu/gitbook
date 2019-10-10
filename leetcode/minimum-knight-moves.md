# 1142. Minimum Knight Moves

* *Difficulty: Medium*

* *Topics: Breadth-first Search*

* *Similar Questions:*

## Problem:

<p>In an <strong>infinite</strong> chess board with coordinates from <code>-infinity</code>&nbsp;to <code>+infinity</code>, you have a <strong>knight</strong> at square&nbsp;<code>[0, 0]</code>.</p>

<p>A&nbsp;knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/knight.png" style="height: 200px; width: 200px;" /></p>

<p>Return the&nbsp;minimum number of steps needed to move the knight to the square <code>[x, y]</code>.&nbsp; It is guaranteed the answer exists.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 2, y = 1
<strong>Output:</strong> 1
<strong>Explanation: </strong>[0, 0] &rarr; [2, 1]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 5, y = 5
<strong>Output:</strong> 4
<strong>Explanation: </strong>[0, 0] &rarr; [2, 1] &rarr; [4, 2] &rarr; [3, 4] &rarr; [5, 5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>|x| + |y| &lt;= 300</code></li>
</ul>

## Solutions:

```c++
class Solution {
public:
    int minKnightMoves(int x, int y) {
        set<pair<int, int>> visited;
        queue<pair<int, int>> q;
        q.push({0, 0});
        
        int level = 0;
        while (!q.empty()) {
            int size = q.size();
            for (int n = 0; n < size; ++n) {
                auto pos = q.front(); q.pop();
                if (abs(pos.first) == abs(x) && abs(pos.second) == abs(y))  return level;
                if (visited.count({abs(pos.first), abs(pos.second)})) continue;
                visited.insert({abs(pos.first), abs(pos.second)});
                for (int i = 0; i < 8; ++i) {
                    q.push({pos.first + directions[i][0], pos.second + directions[i][1]});
                }
            }
            ++level;
        }
        return -1;
    }
    
    
private:
    int directions[8][2] = {
        {1, 2}, 
        {2, 1},
        {2, -1},
        {1, -2},
        {-1, -2},
        {-2, -1},
        {-2, 1},
        {-1, 2}
    };
};
```
