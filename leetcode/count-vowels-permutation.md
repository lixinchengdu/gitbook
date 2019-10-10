# 1332. Count Vowels Permutation

* *Difficulty: Hard*

* *Topics: Dynamic Programming*

* *Similar Questions:*

## Problem:

<p>Given an integer <code>n</code>, your task is to count how many strings of length <code>n</code> can be formed under the following rules:</p>

<ul>
	<li>Each character is a lower case vowel&nbsp;(<code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, <code>&#39;u&#39;</code>)</li>
	<li>Each vowel&nbsp;<code>&#39;a&#39;</code> may only be followed by an <code>&#39;e&#39;</code>.</li>
	<li>Each vowel&nbsp;<code>&#39;e&#39;</code> may only be followed by an <code>&#39;a&#39;</code>&nbsp;or an <code>&#39;i&#39;</code>.</li>
	<li>Each vowel&nbsp;<code>&#39;i&#39;</code> <strong>may not</strong> be followed by another <code>&#39;i&#39;</code>.</li>
	<li>Each vowel&nbsp;<code>&#39;o&#39;</code> may only be followed by an <code>&#39;i&#39;</code> or a&nbsp;<code>&#39;u&#39;</code>.</li>
	<li>Each vowel&nbsp;<code>&#39;u&#39;</code> may only be followed by an <code>&#39;a&#39;.</code></li>
</ul>

<p>Since the answer&nbsp;may be too large,&nbsp;return it modulo <code>10^9 + 7.</code></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> All possible strings are: &quot;a&quot;, &quot;e&quot;, &quot;i&quot; , &quot;o&quot; and &quot;u&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 10
<strong>Explanation:</strong> All possible strings are: &quot;ae&quot;, &quot;ea&quot;, &quot;ei&quot;, &quot;ia&quot;, &quot;ie&quot;, &quot;io&quot;, &quot;iu&quot;, &quot;oi&quot;, &quot;ou&quot; and &quot;ua&quot;.
</pre>

<p><strong>Example 3:&nbsp;</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 68</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2 * 10^4</code></li>
</ul>

## Solutions:

```c++
class Solution {
public:
    int countVowelPermutation(int n) {
        if (n == 0) return 1;
        if (n == 1) return 5;
        
        vector<unordered_map<char, int>> dp(n);
        
        dp[0] = {
            {'a', 1},
            {'e', 1},
            {'i', 1},
            {'o', 1},
            {'u', 1}
        };
        
        for (int i = 1; i < n; ++i) {
            unordered_map<char, int> charToCount;
            for (auto& entry : dp[i-1]) {
                char c = entry.first;
                int count = entry.second;
                for (auto& follower : followers[c]) {
                    charToCount[follower] = (charToCount[follower] + count) % MOD;
                }
            }
            
            dp[i] = charToCount;
        }
        
        int ret = 0;
        for (auto& entry : dp[n-1]) {
            ret = (ret + entry.second) % MOD;
        }
        
        return ret;
        
    }
    
private:
    const int MOD = 1e9 + 7;
    unordered_map<char, vector<char>> followers {
        {'a', {'e'}},
        {'e', {'a', 'i'}},
        {'i', {'a', 'e', 'o', 'u'}},
        {'o', {'i', 'u'}},
        {'u', {'a'}}
    };
    
};
```
