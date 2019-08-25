# 84. Largest Rectangle in Histogram

* *Difficulty: Hard*

* *Topics: Array, Stack*

* *Similar Questions:*

  * [Maximal Rectangle](maximal-rectangle.md)

## Problem:

<p>Given <em>n</em> non-negative integers representing the histogram&#39;s bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/histogram.png" style="width: 188px; height: 204px;" /><br />
<small>Above is a histogram where width of each bar is 1, given height = <code>[2,1,5,6,2,3]</code>.</small></p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png" style="width: 188px; height: 204px;" /><br />
<small>The largest rectangle is shown in the shaded area, which has area = <code>10</code> unit.</small></p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [2,1,5,6,2,3]
<strong>Output:</strong> 10
</pre>

## Solutions:

```c++
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.push_back(0);
        stack<int> stk;
        int area = 0;
        
        for (int i = 0; i < heights.size(); ++i) {
            while (!stk.empty() && heights[stk.top()] > heights[i]) {
                int topIndex = stk.top();
                stk.pop();
                area = max(area, heights[topIndex] * (i - (stk.empty() ? 0 : stk.top() + 1)));
                //cout << area << endl;
            }
            
            stk.push(i);
        }
        
        return area;
    }
};
```
