# 576. Out of Boundary Paths

* *Difficulty: Medium*

* *Topics: Dynamic Programming, Depth-first Search*

* *Similar Questions:*

  * [Knight Probability in Chessboard](knight-probability-in-chessboard.md)

## Problem:

<p>There is an <b>m</b> by <b>n</b> grid with a ball. Given the start coordinate <b>(i,j)</b> of the ball, you can move the ball to <b>adjacent</b> cell or cross the grid boundary in four directions (up, down, left, right). However, you can <b>at most</b> move <b>N</b> times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 10<sup>9</sup> + 7.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input: </b>m = 2, n = 2, N = 2, i = 0, j = 0
<b>Output:</b> 6
<b>Explanation:</b>
<img src="https://assets.leetcode.com/uploads/2018/10/13/out_of_boundary_paths_1.png" style="width: 100%; max-width: 400px" />
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input: </b>m = 1, n = 3, N = 3, i = 0, j = 1
<b>Output:</b> 12
<b>Explanation:</b>
<img src="https://assets.leetcode.com/uploads/2018/10/12/out_of_boundary_paths_2.png" style="width: 100%; max-width: 400px" />
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>Once you move the ball out of boundary, you cannot move it back.</li>
	<li>The length and height of the grid is in range [1,50].</li>
	<li>N is in range [0,50].</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    int findPaths(int m, int n, int N, int i, int j) {
        map<pair<int, int>, int> cache;
        return helper(m, n, N, i, j, cache);
    }

private:
    int helper(int m, int n, int N, int i, int j, map<pair<int, int>, int>& cache) {
        if (i < 0 || i >= m || j < 0 || j >= n) return 1;
        int position = getPosition(m, n, i, j);
        if (cache.count({position, N}) > 0) return cache[{position, N}];
        
        if (N == 0) return 0;
        
        int ret = 0;
        for (int k = 0; k < 4; ++k) {
            ret = (ret + helper(m, n, N - 1, i + directions[k][0], j + directions[k][1], cache)) % MOD;
        }
       
        cache[{position, N}] = ret;
        return ret;
    }
    
    inline int getPosition(int m, int n, int i, int j) {
        return n * i + j;
    }
    
    int directions[4][2] = {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1}
    };
    
    int MOD = 1e9 + 7;
};
```
