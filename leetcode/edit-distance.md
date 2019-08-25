# 72. Edit Distance

* *Difficulty: Hard*

* *Topics: String, Dynamic Programming*

* *Similar Questions:*

  * [One Edit Distance](one-edit-distance.md)

  * [Delete Operation for Two Strings](delete-operation-for-two-strings.md)

  * [Minimum ASCII Delete Sum for Two Strings](minimum-ascii-delete-sum-for-two-strings.md)

  * [Uncrossed Lines](uncrossed-lines.md)

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
        int len1 = word1.length();
        int len2 = word2.length();
        
        vector<vector<int>> dp(1 + len1, vector<int> (1 + len2, 0));
        for (int i = 0 ; i <= len1; ++i) {
            dp[i][0] = i;
        }
        
        for (int j = 0; j <= len2; ++j) {
            dp[0][j] = j;
        }
        
        for (int i = 1; i <= len1; ++i) {
            for (int j = 1; j <= len2; ++j) {
                if (word1[i-1] == word2[j-1]) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    dp[i][j] = 1 + min(dp[i-1][j], min(dp[i][j-1],dp[i-1][j-1])); 
                }
            }
        }
        
        return dp[len1][len2];
    }
};
```
