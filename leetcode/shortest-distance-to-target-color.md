# 1134. Shortest Distance to Target Color

* *Difficulty: Medium*

* *Topics: Binary Search*

* *Similar Questions:*

## Problem:

<p>You are given an array <code>colors</code>, in which there are three colors: <code>1</code>, <code>2</code> and&nbsp;<code>3</code>.</p>

<p>You are also given some queries. Each query consists of two integers <code>i</code>&nbsp;and <code>c</code>, return&nbsp;the shortest distance between the given index&nbsp;<code>i</code> and the target color <code>c</code>. If there is no solution return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
<strong>Output:</strong> [3,0,3]
<strong>Explanation: </strong>
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> colors = [1,2], queries = [[0,3]]
<strong>Output:</strong> [-1]
<strong>Explanation: </strong>There is no 3 in the array.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= colors.length &lt;= 5*10^4</code></li>
	<li><code>1 &lt;= colors[i] &lt;= 3</code></li>
	<li><code>1&nbsp;&lt;= queries.length &lt;= 5*10^4</code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>0 &lt;= queries[i][0] &lt;&nbsp;colors.length</code></li>
	<li><code>1 &lt;= queries[i][1] &lt;= 3</code></li>
</ul>

## Solutions:

```c++
class Solution {
public:
    vector<int> shortestDistanceColor(vector<int>& colors, vector<vector<int>>& queries) {
        unordered_map<int, vector<int>> positions;
        for (int i= 0; i < colors.size(); ++i) {
            positions[colors[i]].push_back(i);
        }
        
        vector<int> ret;
        for (auto& query : queries) {
            int index = query[0];
            int color = query[1];
            
            if (positions[color].empty()) {
                ret.push_back(-1);
            } else {
                auto upperBound = upper_bound(positions[color].begin(), positions[color].end(), index);
                auto prevIt = prev(upperBound);
                if (upperBound == positions[color].end()) {
                    ret.push_back(abs(index - *prevIt));
                } else if (upperBound == positions[color].begin()) {
                    ret.push_back(abs(index - *upperBound));
                }
                else {
                     ret.push_back(min(abs(index - *prevIt), abs(index - *upperBound)));
                }
            }
        }
        
        return ret;
    }
};
```
