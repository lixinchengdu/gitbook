# 729. My Calendar I

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [My Calendar II](my-calendar-ii.md)

  * [My Calendar III](my-calendar-iii.md)

## Problem:

<p>Implement a <code>MyCalendar</code> class to store your events. A new event can be added if adding the event will not cause a double booking.</p>

<p>Your class will have the method, <code>book(int start, int end)</code>. Formally, this represents a booking on the half open interval <code>[start, end)</code>, the range of real numbers <code>x</code> such that <code>start &lt;= x &lt; end</code>.</p>

<p>A <i>double booking</i> happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)</p>

<p>For each call to the method <code>MyCalendar.book</code>, return <code>true</code> if the event can be added to the calendar successfully without causing a double booking. Otherwise, return <code>false</code> and do not add the event to the calendar.</p>
Your class will be called like this: <code>MyCalendar cal = new MyCalendar();</code> <code>MyCalendar.book(start, end)</code>

<p><b>Example 1:</b></p>

<pre>
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
<b>Explanation:</b> 
The first event can be booked.  The second can&#39;t because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ul>
	<li>The number of calls to <code>MyCalendar.book</code> per test case will be at most <code>1000</code>.</li>
	<li>In calls to <code>MyCalendar.book(start, end)</code>, <code>start</code> and <code>end</code> are integers in the range <code>[0, 10^9]</code>.</li>
</ul>

<p>&nbsp;</p>

## Solutions:

```c++
class MyCalendar {
public:
    struct Interval {
        int start;
        int end;
        
        Interval(int start, int end) {
            this->start = start;
            this->end = end;
        }
        
        bool operator< (const Interval& other) const {
            return start < other.start;
        }
    };
    
    MyCalendar() {
        
    }
    
    bool book(int start, int end) {
        if (start == end)   return true;
        Interval interval {start, end};
        if (intervals.empty()) {
            intervals.insert(interval);
            return true;
        }
        
        auto it = intervals.lower_bound(interval);
        
        if (it != intervals.begin()) {
            it = prev(it); // assignment1!!!!
            if (interval.start < it->end)   return false;
            it = next(it);
        }
        
        if (it != intervals.end()) {
            if (interval.end > it->start)   return false;
            else {
                intervals.insert(interval);
                return true;
            }
        } else {
            intervals.insert(interval);
            return true;
        }
    } 
    
private:
    set<Interval> intervals;
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */
```
