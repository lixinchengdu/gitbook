# 754. Cracking the Safe

* *Difficulty: Hard*

* *Topics: Math, Depth-first Search*

* *Similar Questions:*

## Problem:

<p>There is a box protected by a password. The password is a sequence of&nbsp;<code>n</code> digits&nbsp;where each digit can be one of the first <code>k</code> digits <code>0, 1, ..., k-1</code>.</p>

<p>While entering a password,&nbsp;the last <code>n</code> digits entered will automatically be matched against the correct password.</p>

<p>For example, assuming the correct password is <code>&quot;345&quot;</code>,&nbsp;if you type <code>&quot;012345&quot;</code>, the box will open because the correct password matches the suffix of the entered password.</p>

<p>Return any password of <strong>minimum length</strong> that is guaranteed to open the box at some point of entering it.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> n = 1, k = 2
<b>Output:</b> &quot;01&quot;
<b>Note:</b> &quot;10&quot; will be accepted too.
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> n = 2, k = 2
<b>Output:</b> &quot;00110&quot;
<b>Note:</b> &quot;01100&quot;, &quot;10011&quot;, &quot;11001&quot; will be accepted too.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li><code>n</code> will be in the range <code>[1, 4]</code>.</li>
	<li><code>k</code> will be in the range <code>[1, 10]</code>.</li>
	<li><code>k^n</code> will be at most <code>4096</code>.</li>
</ol>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    string crackSafe(int n, int k) {
        const int total_len = pow(k, n) + n - 1;
        string ans(n, '0');
        unordered_set<string> visited{ans};
        if (dfs(ans, total_len, n, k, visited))
            return ans;
        return "";
    }
private:
    bool dfs(string& ans, const int total_len, const int n, const int k, unordered_set<string>& visited) { // return bool
        if (visited.size() == pow(k,n))
            return true;
        
        string node = ans.substr(ans.length() - n + 1, n - 1);
        for (char c = '0'; c < '0' + k; ++c) {
            node.push_back(c);
            if (!visited.count(node)) {
                ans.push_back(c);
                visited.insert(node);
                if (dfs(ans, total_len, n, k, visited)) return true;
                visited.erase(node);
                ans.pop_back();
            }
            node.pop_back();
        }
        
        return false;
    }
};
```
