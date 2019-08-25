# 253. Meeting Rooms II

* *Difficulty: Medium*

* *Topics: Heap, Greedy, Sort*

* *Similar Questions:*

  * [Merge Intervals](merge-intervals.md)

  * [Meeting Rooms](meeting-rooms.md)

  * [Minimum Number of Arrows to Burst Balloons](minimum-number-of-arrows-to-burst-balloons.md)

  * [Car Pooling](car-pooling.md)

## Problem:

<p>Given an array of meeting time intervals consisting of start and end times <code>[[s1,e1],[s2,e2],...]</code> (s<sub>i</sub> &lt; e<sub>i</sub>), find the minimum number of conference rooms required.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>[[0, 30],[5, 10],[15, 20]]</code>
<strong>Output:</strong> 2</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [[7,10],[2,4]]
<b>Output:</b> 1</pre>

<p><strong>NOTE:</strong>&nbsp;input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.</p>

## Solutions:

```c++
class Solution {
public:
    struct MeetingEvent {
        int time;
        bool start;
        
        MeetingEvent(int time, bool start) {
            this->time = time;
            this->start = start;
        }
        
        bool operator< (const MeetingEvent& event) const {
            if (this->time == event.time) {
                return !(this->start);
            } else {
                return this->time < event.time;
            }
        }
    };
    
    int minMeetingRooms(vector<vector<int>>& intervals) {
        vector<MeetingEvent> events;
        for (auto& interval : intervals) {
            events.push_back({interval[0], true});
            events.push_back({interval[1], false});
        }
        
        sort(events.begin(), events.end());
        int count = 0;
        int ret = 0;
        for (int i = 0; i < events.size(); ++i) {
            if (events[i].start) {
                ++count;
                ret = max(ret, count);
            } else {
                --count;
            }
        }
        
        return ret;
    }
};
```
