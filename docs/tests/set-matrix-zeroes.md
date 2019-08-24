# 73. Set Matrix Zeroes

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [Game of Life](./tests/set-matrix-zeroes.md)

## Problem:

<p>Given a <em>m</em> x <em>n</em> matrix, if an element is 0, set its entire row and column to 0. Do it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
[
&nbsp; [1,1,1],
&nbsp; [1,0,1],
&nbsp; [1,1,1]
]
<strong>Output:</strong> 
[
&nbsp; [1,0,1],
&nbsp; [0,0,0],
&nbsp; [1,0,1]
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 
[
&nbsp; [0,1,2,0],
&nbsp; [3,4,5,2],
&nbsp; [1,3,1,5]
]
<strong>Output:</strong> 
[
&nbsp; [0,0,0,0],
&nbsp; [0,4,5,0],
&nbsp; [0,3,1,0]
]
</pre>

<p><strong>Follow up:</strong></p>

<ul>
	<li>A straight forward solution using O(<em>m</em><em>n</em>) space is probably a bad idea.</li>
	<li>A simple improvement uses O(<em>m</em> + <em>n</em>) space, but still not the best solution.</li>
	<li>Could you devise a constant space solution?</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        set<int> rowIndexDel;
        set<int> colIndexDel;
        for (int i = 0 ; i < m ; i++)
        {
            for (int j = 0 ; j < n; j++)
                if (!matrix[i][j])
                {
                    rowIndexDel.insert(i);
                    colIndexDel.insert(j);
                }
        }
        for (auto elem: rowIndexDel)
        {
            for (int j = 0; j < n; j++)
                matrix[elem][j] = 0;
        }
        for (auto elem: colIndexDel)
        {
            for (int i = 0; i < m; i++)
                matrix[i][elem] = 0;
        }
        
    }
};
```
