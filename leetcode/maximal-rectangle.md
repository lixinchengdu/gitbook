# 85. Maximal Rectangle

* *Difficulty: Hard*

* *Topics: Array, Hash Table, Dynamic Programming, Stack*

* *Similar Questions:*

  * [Largest Rectangle in Histogram](largest-rectangle-in-histogram.md)

  * [Maximal Square](maximal-square.md)

## Problem:

<p>Given a 2D binary matrix filled with 0&#39;s and 1&#39;s, find the largest rectangle containing only 1&#39;s and return its area.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>
[
  [&quot;1&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;0&quot;,&quot;<strong>1</strong>&quot;,&quot;<strong>1</strong>&quot;,&quot;<strong>1</strong>&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;<strong>1</strong>&quot;,&quot;<strong>1</strong>&quot;,&quot;<strong>1</strong>&quot;],
  [&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;]
]
<strong>Output:</strong> 6
</pre>

## Solutions:

```c++
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int m = matrix.size();
        if (m == 0) return 0;
        int n = matrix[0].size();
        if (n == 0) return 0;
        
        vector<int> heights (n + 1, 0);
        int ret = 0;
        
        for (int row = 0; row < m; ++row) {
            for (int col = 0; col < n; ++col) {
                if (matrix[row][col] == '0') {
                    heights[col] = 0;
                } else {
                    ++heights[col];
                }
            }
            ret = max(ret, barMaxArea(heights));
        }
        
        return ret;
    }
    
    int barMaxArea(vector<int>& heights) {
        heights.back() = 0;
        stack<int> stk;
        int area = 0;
        
        for (int i = 0; i < heights.size(); ++i) {
            while (!stk.empty() && heights[stk.top()] > heights[i]) {
                int topIndex = stk.top();
                stk.pop();
               area = max(area, heights[topIndex] * (i - (stk.empty() ? 0 : (stk.top() + 1))));
            }
            
            stk.push(i);
            
        }
        
        return area;
    }
};
```
