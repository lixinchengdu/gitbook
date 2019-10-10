# 1149. Intersection of Three Sorted Arrays

* *Difficulty: Easy*

* *Topics: Hash Table, Two Pointers*

* *Similar Questions:*

  * [Intersection of Two Arrays](intersection-of-two-arrays.md)

## Problem:

<p>Given three integer arrays <code>arr1</code>, <code>arr2</code> and <code>arr3</code>&nbsp;<strong>sorted</strong> in <strong>strictly increasing</strong> order, return a sorted array of <strong>only</strong>&nbsp;the&nbsp;integers that appeared in <strong>all</strong> three arrays.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
<strong>Output:</strong> [1,5]
<strong>Explanation: </strong>Only 1 and 5 appeared in the three arrays.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr1.length, arr2.length, arr3.length &lt;= 1000</code></li>
	<li><code>1 &lt;= arr1[i], arr2[i], arr3[i] &lt;= 2000</code></li>
</ul>

## Solutions:

```c++
class Solution {
public:
    vector<int> arraysIntersection(vector<int>& arr1, vector<int>& arr2, vector<int>& arr3) {
        vector<int> arr12 = helper(arr1, arr2);
        return helper(arr12, arr3);
    }
    
private: 
    vector<int> helper(vector<int>& arr1, vector<int>& arr2) {
        int i1 = 0, i2 = 0;
        vector<int> ret;
        while (i1 < arr1.size() && i2 < arr2.size()) {
            if (arr1[i1] == arr2[i2]) {
                ret.push_back(arr1[i1]);
                ++i1;
                ++i2;
            } else if (arr1[i1] < arr2[i2]) {
                ++i1;
            } else {
                ++i2;
            }
        }
        
        return ret;
    }
    
};
```
