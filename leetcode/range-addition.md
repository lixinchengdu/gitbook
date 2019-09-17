# 370. Range Addition

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [Range Addition II](range-addition-ii.md)

## Problem:

<p>Assume you have an array of length <b><i>n</i></b> initialized with all <b>0</b>&#39;s and are given <b><i>k</i></b> update operations.</p>

<p>Each operation is represented as a triplet: <b>[startIndex, endIndex, inc]</b> which increments each element of subarray <b>A[startIndex ... endIndex]</b> (startIndex and endIndex inclusive) with <b>inc</b>.</p>

<p>Return the modified array after all <b><i>k</i></b> operations were executed.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input: </strong>length = <span id="example-input-1-1">5</span>, updates = <span id="example-input-1-2">[[1,3,2],[2,4,3],[0,2,-2]]</span>
<strong>Output: </strong><span id="example-output-1">[-2,0,3,5,3]</span>
</pre>

<p><b>Explanation:</b></p>

<pre>
Initial state:
[0,0,0,0,0]

After applying operation [1,3,2]:
[0,2,2,2,0]

After applying operation [2,4,3]:
[0,2,5,5,3]

After applying operation [0,2,-2]:
[-2,0,3,5,3]
</pre>
## Solutions:

```c++
class Solution {
public:
    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
        vector<int> addition(length, 0);
        for (auto& update : updates) {
            int startIndex = update[0];
            int endIndex = update[1];
            int inc = update[2];
            
            addition[endIndex] += inc;
            if (startIndex - 1 >= 0) {
                addition[startIndex - 1] -= inc;
            }
        }
        
        vector<int> ret(length, 0);
        for (int i = length - 1; i > 0; --i) {
            ret[i] = addition[i];
            addition[i-1] += addition[i];
        }
        
        return addition;
    }
};
```
