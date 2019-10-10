# 1306. Minimum Absolute Difference

* *Difficulty: Easy*

* *Topics: Array*

* *Similar Questions:*

## Problem:

<p>Given an&nbsp;array&nbsp;of <strong>distinct</strong>&nbsp;integers <code>arr</code>, find all pairs of elements with the minimum absolute difference of any two elements.&nbsp;</p>

<p>Return a list of pairs in ascending order(with respect to pairs), each pair <code>[a, b]</code> follows</p>

<ul>
	<li><code>a, b</code> are from <code>arr</code></li>
	<li><code>a &lt; b</code></li>
	<li><code>b - a</code>&nbsp;equals to the minimum absolute difference of any two elements in <code>arr</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,2,1,3]
<strong>Output:</strong> [[1,2],[2,3],[3,4]]
<strong>Explanation: </strong>The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,3,6,10,15]
<strong>Output:</strong> [[1,3]]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,8,-10,23,19,-4,-14,27]
<strong>Output:</strong> [[-14,-10],[19,23],[23,27]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 10^5</code></li>
	<li><code>-10^6 &lt;= arr[i] &lt;= 10^6</code></li>
</ul>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        int n = arr.size();
        if (n <= 1) return {};
        sort(arr.begin(), arr.end());
        
        vector<vector<int>> ret;
        int minDiff = INT_MAX;
        
        for (int i = 1; i < n; ++i) {
            if (abs(arr[i] - arr[i-1]) == minDiff) {
                ret.push_back({arr[i-1], arr[i]});
            } else if (abs(arr[i] - arr[i-1]) < minDiff) {
                minDiff = abs(arr[i] - arr[i-1]);
                ret = {{arr[i-1], arr[i]}};
            }
        }
        
        return ret;
    }
};
```
