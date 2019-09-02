# 688. Knight Probability in Chessboard

* *Difficulty: Medium*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Out of Boundary Paths](out-of-boundary-paths.md)

## Problem:

<p>On an <code>N</code>x<code>N</code> chessboard, a knight starts at the <code>r</code>-th row and <code>c</code>-th column and attempts to make exactly <code>K</code> moves. The rows and columns are 0 indexed, so the top-left square is <code>(0, 0)</code>, and the bottom-right square is <code>(N-1, N-1)</code>.</p>

<p>A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/knight.png" style="width: 200px; height: 200px;" /></p>

<p>&nbsp;</p>

<p>Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.</p>

<p>The knight continues moving until it has made exactly <code>K</code> moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.</p>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> 3, 2, 0, 0
<b>Output:</b> 0.0625
<b>Explanation:</b> There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ul>
	<li><code>N</code> will be between 1 and 25.</li>
	<li><code>K</code> will be between 0 and 100.</li>
	<li>The knight always initially starts on the board.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    double knightProbability(int N, int K, int r, int c) {
        map<pair<int, int>, double> cache;
        return helper(N, K, r, c, cache);
    }
    
private:
    double helper(int N, int K, int r, int c, map<pair<int, int>, double>& cache) {
        if (!(r >= 0 && r < N && c >= 0 && c < N)) { // this check should put before getPosition!!!!
            return 0.0;
        }
        int position = getPosition(N, r, c);
        if (cache.count({position, K}) > 0) {
            return cache[{position, K}];
        }
        
        
        if (K == 0) {
            return 1.0;
        }
        
        double prob = 0;
        for (int i = 0; i < 8; ++i) {
            prob += helper(N, K - 1, r + directions[i][0], c + directions[i][1], cache);
        }
        
        
        prob /= 8;
        
        cache[{position, K}] = prob;
        return prob;
    }
    
    inline int getPosition(int N, int r, int c) {
        return N * r + c;
    }
    
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
