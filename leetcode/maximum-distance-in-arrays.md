# 624. Maximum Distance in Arrays

* *Difficulty: Easy*

* *Topics: Array, Hash Table*

* *Similar Questions:*

## Problem:

<p>
Given <code>m</code> arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers <code>a</code> and <code>b</code> to be their absolute difference <code>|a-b|</code>. Your task is to find the maximum distance.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
[[1,2,3],
 [4,5],
 [1,2,3]]
<b>Output:</b> 4
<b>Explanation:</b> 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
</pre>
</p>
	
<p><b>Note:</b><br>
<ol>
<li>Each given array will have at least 1 number. There will be at least two non-empty arrays.</li>
<li>The total number of the integers in <b>all</b> the <code>m</code> arrays will be in the range of [2, 10000].</li>
<li>The integers in the <code>m</code> arrays will be in the range of [-10000, 10000].</li>
</ol>
</p>
## Solutions:

```c++
class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int m = arrays.size();
        if (m == 0) return 0;
        
        int firstVal = INT_MIN;
        int secondVal = INT_MIN;
        int firstIndex = -1;
        int secondIndex = -1;
        
        for (int i = 0; i < m; ++i) {
            if (arrays[i].back() >= firstVal) {
                secondVal = firstVal;
                secondIndex = firstIndex;
                firstVal = arrays[i].back();
                firstIndex = i;
            } else if (arrays[i].back() > secondVal) {
                secondVal = arrays[i].back();
                secondIndex = i;
            }
        }
        
        int ret = 0;
        for (int i = 0; i < m; ++i) {
            if (i == firstIndex) {
                ret = max(ret, secondVal - arrays[i][0]);
            } else {
                ret = max(ret, firstVal - arrays[i][0]);
            }
        }
        
        return ret;
        
    }
};
```
