# 656. Coin Path

* *Difficulty: Hard*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [House Robber](house-robber.md)

  * [House Robber II](house-robber-ii.md)

## Problem:

<p>Given an array <code>A</code> (index starts at <code>1</code>) consisting of N integers: A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>&nbsp;and an integer <code>B</code>. The integer <code>B</code> denotes that from any place (suppose the index is <code>i</code>) in the array <code>A</code>, you can jump to any one of the place in the array <code>A</code> indexed <code>i+1</code>, <code>i+2</code>, &hellip;, <code>i+B</code> if this place can be jumped to. Also, if you step on the index <code>i</code>, you have to pay A<sub>i</sub>&nbsp;coins. If A<sub>i</sub>&nbsp;is -1, it means you can&rsquo;t jump to the place indexed <code>i</code> in the array.</p>

<p>Now, you start from the place indexed <code>1</code> in the array <code>A</code>, and your aim is to reach the place indexed <code>N</code> using the minimum coins. You need to return the path of indexes (starting from 1 to N) in the array you should take to get to the place indexed <code>N</code> using minimum coins.</p>

<p>If there are multiple paths with the same cost, return the lexicographically smallest such path.</p>

<p>If it&#39;s not possible to reach the place indexed N then you need to return an empty array.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [1,2,4,-1,2], 2
<b>Output:</b> [1,3,5]
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [1,2,4,-1,2], 1
<b>Output:</b> []
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>Path Pa<sub>1</sub>, Pa<sub>2</sub>, ..., Pa<sub>n</sub>&nbsp;is lexicographically smaller than Pb<sub>1</sub>, Pb<sub>2</sub>, ..., Pb<sub>m</sub>, if and only if at the first <code>i</code> where Pa<sub>i</sub>&nbsp;and Pb<sub>i</sub>&nbsp;differ, Pa<sub>i</sub>&nbsp;&lt; Pb<sub>i</sub>; when no such&nbsp;<code>i</code>&nbsp;exists, then&nbsp;<code>n</code> &lt; <code>m</code>.</li>
	<li>A<sub>1</sub> &gt;= 0. A<sub>2</sub>, ..., A<sub>N</sub> (if exist) will in the range of [-1, 100].</li>
	<li>Length of A is in the range of [1, 1000].</li>
	<li>B is in the range of [1, 100].</li>
</ol>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    vector<int> cheapestJump(vector<int>& A, int B) { // reverse order to get lexical smaller result
        int n = A.size();
        if (n == 0) return {};
        if (A[0] == -1 || A[n-1] == -1) return {}; // this check is essential if we reverse the order of A
        reverse(A.begin(), A.end());
        vector<int> dp(n, INT_MAX);
        vector<int> prev(n, 0);
        
        dp[0] = A[0];
        prev[0] = -1;
        
        for (int i= 1; i < n; ++i) {
            if (A[i] == -1) continue;
            for (int j = -1; j >= -B; --j) {
                if (i + j < 0)  break;
                if (dp[i+j] < dp[i]) {
                    dp[i] = dp[i+j];
                    prev[i] = i + j;
                }
            }
            if (dp[i] != INT_MAX)
                dp[i] += A[i];
        }
        
        vector<int> ret;
        int i = n - 1;
        while (i >= 0 && dp[i] != INT_MAX) {
            ret.push_back(n - i);
            i = prev[i];
        }
        
        if (i >= 0) return {};
        return ret;
    }
};
```
