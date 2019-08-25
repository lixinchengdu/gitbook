# 131. Palindrome Partitioning

* *Difficulty: Medium*

* *Topics: Backtracking*

* *Similar Questions:*

  * [Palindrome Partitioning II](palindrome-partitioning-ii.md)

## Problem:

<p>Given a string <em>s</em>, partition <em>s</em> such that every substring of the partition is a palindrome.</p>

<p>Return all possible palindrome partitioning of <em>s</em>.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;&quot;aab&quot;
<strong>Output:</strong>
[
  [&quot;aa&quot;,&quot;b&quot;],
  [&quot;a&quot;,&quot;a&quot;,&quot;b&quot;]
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<string>> partition(string s) {
        int len = s.length();
        vector<vector<string>> ret;
        vector<string> path;
        vector<vector<bool>> dp(len, vector<bool>(len, false));
        
        helper(s, 0, 0, dp, path, ret);
        return ret;
    }
    
    void helper(string& s, int start, int pos, vector<vector<bool>>& dp, vector<string>& path,                  vector<vector<string>>& ret) {
        
        if (pos == s.length()) {
            if (start == s.length()) {
                ret.push_back(path);
            }
            return;
        }
        
        if (s[pos] == s[start]) {
            if (start + 1 == pos || start == pos) {
                dp[start][pos] = true;
            } else {
                dp[start][pos] = dp[start + 1][pos - 1]; // it works because another branch has compute dp[start+1][pos-1]. However, it is not a good idea to compute dp inside helper function.
            }
        }
        
        if (dp[start][pos] == false) {
            helper(s, start, pos + 1, dp, path, ret);
            return;
        } 
        
        path.push_back(s.substr(start, pos - start + 1));
        helper(s, pos + 1, pos + 1, dp, path, ret);
        path.pop_back();
        helper(s, start, pos + 1, dp, path, ret);
    }
};
```
