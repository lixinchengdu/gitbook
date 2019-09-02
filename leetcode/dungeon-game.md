# 174. Dungeon Game

* *Difficulty: Hard*

* *Topics: Binary Search, Dynamic Programming*

* *Similar Questions:*

  * [Unique Paths](unique-paths.md)

  * [Minimum Path Sum](minimum-path-sum.md)

  * [Cherry Pickup](cherry-pickup.md)

## Problem:

<style type="text/css">table.dungeon, .dungeon th, .dungeon td {
  border:3px solid black;
}

 .dungeon th, .dungeon td {
    text-align: center;
    height: 70px;
    width: 70px;
}
</style>
<p>The demons had captured the princess (<strong>P</strong>) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (<strong>K</strong>) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.</p>

<p>The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.</p>

<p>Some of the rooms are guarded by demons, so the knight loses health (<em>negative</em> integers) upon entering these rooms; other rooms are either empty (<em>0&#39;s</em>) or contain magic orbs that increase the knight&#39;s health (<em>positive</em> integers).</p>

<p>In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.</p>

<p>&nbsp;</p>

<p><strong>Write a function to determine the knight&#39;s minimum initial health so that he is able to rescue the princess.</strong></p>

<p>For example, given the dungeon below, the initial health of the knight must be at least <strong>7</strong> if he follows the optimal path <code>RIGHT-&gt; RIGHT -&gt; DOWN -&gt; DOWN</code>.</p>

<table class="dungeon">
	<tbody>
		<tr>
			<td>-2 (K)</td>
			<td>-3</td>
			<td>3</td>
		</tr>
		<tr>
			<td>-5</td>
			<td>-10</td>
			<td>1</td>
		</tr>
		<tr>
			<td>10</td>
			<td>30</td>
			<td>-5 (P)</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The knight&#39;s health has no upper bound.</li>
	<li>Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int m = dungeon.size();
        if (m == 0) return 0;
        int n = dungeon[0].size();
        if (n == 0) return 0;
        
        vector<vector<int>> dp (m, vector<int> (n, 0));
        
        //dp[m - 1][n - 1] = dungeon[m - 1][n - 1];
        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                if (i == m - 1 && j == n - 1) {
                    dp[i][j] = max(-dungeon[i][j], 0);
                    continue;
                }
                dp[i][j] = max(-dungeon[i][j] + min(i + 1 < m ? dp[i+1][j] : INT_MAX, j + 1 < n ? dp[i][j+1] : INT_MAX), 0);
            }
        }
        
        return dp[0][0] + 1;
    }
};
```
