# 1028. Interval List Intersections

* *Difficulty: Medium*

* *Topics: Two Pointers*

* *Similar Questions:*

  * [Merge Intervals](merge-intervals.md)

  * [Merge Sorted Array](merge-sorted-array.md)

  * [Employee Free Time](employee-free-time.md)

## Problem:

<p>Given two lists&nbsp;of <strong>closed</strong> intervals, each list of intervals is pairwise disjoint and in sorted order.</p>

<p>Return the intersection of these two interval lists.</p>

<p><em>(Formally, a closed interval <code>[a, b]</code> (with <code>a &lt;= b</code>) denotes&nbsp;the set of real numbers <code>x</code> with <code>a &lt;= x &lt;= b</code>.&nbsp; The&nbsp;intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.&nbsp; For example, the intersection of [1, 3] and [2, 4] is [2, 3].)</em></p>

<div>
<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/01/30/interval1.png" style="width: 506px; height: 140px;" /></strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[[0,2],[5,10],[13,23],[24,25]]</span>, B = <span id="example-input-1-2">[[1,5],[8,12],[15,24],[25,26]]</span>
<strong>Output: </strong><span id="example-output-1">[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]</span>
<strong>Reminder: </strong>The inputs and the desired output are lists of Interval&nbsp;objects, and not arrays or lists.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt; 1000</code></li>
	<li><code>0 &lt;= B.length &lt; 1000</code></li>
	<li><code>0 &lt;= A[i].start, A[i].end, B[i].start, B[i].end &lt; 10^9</code></li>
</ol>

<p><strong>NOTE:</strong>&nbsp;input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.</p>
</div>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& A, vector<vector<int>>& B) {
        vector<vector<int>> ret;
        
        if(A.empty() && B.empty())  return {};
        
        int posA = 0;
        int posB = 0;
        
        while (posA < A.size() || posB < B.size()) {
            if (posA == A.size()) {
                merge(ret, B[posB++]);
                continue;
            } 
            
            if (posB == B.size()) {
                merge(ret, A[posA++]);
                continue;
            }
            
            if (A[posA][0] <= B[posB][0]) {
                merge(ret, A[posA++]);
            } else {
                merge(ret, B[posB++]);
            }
        }
        
        ret.pop_back();
        return ret;
    }
    
private:
    void merge(vector<vector<int>>& ret, vector<int>& interval) {
        if (ret.empty()) {
            ret.push_back(interval);
            return;
        }
        
        vector<int> pending = ret.back();
        ret.pop_back();
        int overLapLeft = max(pending[0], interval[0]);
        int overLapRight = min(pending[1], interval[1]);
        
        if (overLapLeft <= overLapRight) {
            ret.push_back({overLapLeft, overLapRight});
        }
        
        ret.push_back({min(pending[1], interval[1]), max(pending[1], interval[1])});
    }
};
```
