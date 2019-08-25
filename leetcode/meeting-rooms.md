# 252. Meeting Rooms

* *Difficulty: Easy*

* *Topics: Sort*

* *Similar Questions:*

  * [Merge Intervals](merge-intervals.md)

  * [Meeting Rooms II](meeting-rooms-ii.md)

## Problem:

<p>Given an array of meeting time intervals consisting of start and end times <code>[[s1,e1],[s2,e2],...]</code> (s<sub>i</sub> &lt; e<sub>i</sub>), determine if a person could attend all meetings.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <code>[[0,30],[5,10],[15,20]]</code>
<b>Output:</b> false
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [[7,10],[2,4]]
<b>Output:</b> true
</pre>

<p><strong>NOTE:</strong>&nbsp;input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.</p>

## Solutions:

```c++
class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](vector<int>& lhs, vector<int>& rhs) {
            return lhs[0] < rhs[0];
        });
        
        for (int i = 1; i < intervals.size(); ++i) {
            if (intervals[i][0] < intervals[i-1][1])    return false;
        }
        
        return true;
    }
};
```
