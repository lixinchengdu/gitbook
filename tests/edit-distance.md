# 72. Edit Distance

* *Difficulty: Hard*

* *Topics: String, Dynamic Programming*

* *Similar Questions:*

  * [One Edit Distance](./tests/edit-distance.md)

  * [Delete Operation for Two Strings](./tests/edit-distance.md)

  * [Minimum ASCII Delete Sum for Two Strings](./tests/edit-distance.md)

  * [Uncrossed Lines](./tests/edit-distance.md)

## Problem:

<p>Given two words <em>word1</em> and <em>word2</em>, find the minimum number of operations required to convert <em>word1</em> to <em>word2</em>.</p>

<p>You have the following 3 operations permitted on a word:</p>

<ol>
	<li>Insert a character</li>
	<li>Delete a character</li>
	<li>Replace a character</li>
</ol>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;horse&quot;, word2 = &quot;ros&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
horse -&gt; rorse (replace &#39;h&#39; with &#39;r&#39;)
rorse -&gt; rose (remove &#39;r&#39;)
rose -&gt; ros (remove &#39;e&#39;)
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;intention&quot;, word2 = &quot;execution&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
intention -&gt; inention (remove &#39;t&#39;)
inention -&gt; enention (replace &#39;i&#39; with &#39;e&#39;)
enention -&gt; exention (replace &#39;n&#39; with &#39;x&#39;)
exention -&gt; exection (replace &#39;n&#39; with &#39;c&#39;)
exection -&gt; execution (insert &#39;u&#39;)
</pre>

## Solutions:

```c++
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.length();
        int n = word2.length();
        if (n == 0) return m;
        if (m == 0) return n;
        vector <vector <int> > dp (m, vector <int>(n,0) );
        if (word1[0] != word2[0])   dp[0][0] = 1; 
        else dp[0][0] = 0;
        bool flag = (word1[0] == word2[0]);
        for (int i = 1; i< n; i++)
        {
            if (flag)   dp[0][i] = dp[0][i-1] + 1;
            else
            {
                if (word1[0] == word2[i])
                {
                    dp[0][i] = dp[0][i-1] ;
                    flag = true;
                }
                else dp[0][i] = dp[0][i-1] +1;
            }
        }
           // dp[0][i] = (word1[0] == word2[i]? dp[0][i-1]: dp[0][i-1] + 1);
        flag = (word1[0] == word2[0]);
       for (int i = 1; i< m; i++)
        {
            if (flag)   dp[i][0] = dp[i-1][0] + 1;
            else
            {
                if (word1[i] == word2[0])
                {
                    dp[i][0] = dp[i-1][0] ;
                    flag = true;
                }
                else dp[i][0] = dp[i-1][0] +1;
            }
        }
            
        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                if (word1[i] == word2[j])   dp[i][j] = dp[i-1][j-1];
                else
                {
                    dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1;
                }
            }
        }
        return dp[m-1][n-1];
    }
};
```
