# 1143. Find Smallest Common Element in All Rows

* *Difficulty: Medium*

* *Topics: Hash Table, Binary Search*

* *Similar Questions:*

## Problem:

<p>Given a matrix <code>mat</code>&nbsp;where every row is sorted in <strong>increasing</strong> order, return&nbsp;the <strong>smallest common element</strong> in all rows.</p>

<p>If there is no common element, return&nbsp;<code>-1</code>.</p>


<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
<strong>Output:</strong> 5
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= mat.length, mat[i].length &lt;= 500</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 10^4</code></li>
	<li><code>mat[i]</code> is sorted in increasing order.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    int smallestCommonElement(vector<vector<int>>& mat) {
        int m = mat.size();
        if (m == 0) return -1;
        int n = mat[0].size();
        if (n == 0) return -1;
        
        for (auto& num : mat[0]) {
            bool found = true;
            for (int i = 1; i < m; ++i) {
                if (find(mat[i].begin(), mat[i].end(), num) == mat[i].end()) {
                    found = false;
                    break;
                }
            }
            if (found) return num;
        }
        
        return -1;
        
    }
};
```
