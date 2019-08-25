# 658. Find K Closest Elements

* *Difficulty: Medium*

* *Topics: Binary Search*

* *Similar Questions:*

  * [Guess Number Higher or Lower](guess-number-higher-or-lower.md)

  * [Guess Number Higher or Lower II](guess-number-higher-or-lower-ii.md)

  * [Find K-th Smallest Pair Distance](find-k-th-smallest-pair-distance.md)

## Problem:

<p>
Given a sorted array, two integers <code>k</code> and <code>x</code>, find the <code>k</code> closest elements to <code>x</code> in the array.  The result should also be sorted in ascending order.
If there is a tie,  the smaller elements are always preferred.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1,2,3,4,5], k=4, x=3
<b>Output:</b> [1,2,3,4]
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [1,2,3,4,5], k=4, x=-1
<b>Output:</b> [1,2,3,4]
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The value k is positive and will always be smaller than the length of the sorted array.</li>
<li> Length of the given array is positive and will not exceed 10<sup>4</sup></li>
<li> Absolute value of elements in the array and x will not exceed 10<sup>4</sup></li>
</ol>
</p>

<hr />

<p>
<b><font color="red">UPDATE (2017/9/19):</font></b><br />
The <i>arr</i> parameter had been changed to an <b>array of integers</b> (instead of a list of integers). <b><i>Please reload the code definition to get the latest changes</i></b>.
</p>
## Solutions:

```c++
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int startIndex = findClosest(arr, x);
        if (startIndex < 0) startIndex = 0;
        if (k == 0) return {};
        
        vector<int> ret;
        int forward, backward;
        if (arr[startIndex] == x) {
            ret.push_back(arr[startIndex]);
            --k;
            forward = startIndex + 1;
            backward = startIndex - 1;
        } else if (arr[startIndex] > x){
            forward = startIndex;
            backward = startIndex - 1;
        } else {
            forward = startIndex + 1;
            backward = startIndex;
        }
        
        
        while (k > 0) {
            if (forward >= arr.size()) {
                ret.push_back(arr[backward--]);
                --k;
            } else if (backward < 0) {
                ret.push_back(arr[forward++]);
                --k;
            } else {
                int forwardDis = abs(arr[forward] - x);
                int backDis = abs(arr[backward] -x);
                
                if (forwardDis == backDis) {
                    ret.push_back(arr[backward--]);
                    --k;
                } else if (forwardDis < backDis) {
                    ret.push_back(arr[forward++]);
                    --k;
                } else {
                    ret.push_back(arr[backward--]);
                    --k;
                }
            }
        }
        
        sort(ret.begin(), ret.end()); // we could construct result from two limits; and just return a sublist.
        return ret;
        
    }
    
    int findClosest(vector<int>& arr, int target) {
        int left = 0;
        int right = arr.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) return mid;
            else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return left;
    }
};
```
