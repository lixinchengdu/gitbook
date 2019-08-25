# 681. Next Closest Time

* *Difficulty: Medium*

* *Topics: String*

* *Similar Questions:*

## Problem:

<p>Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.</p>

<p>You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.</p>

<p><b>Example 1:</b>
<pre>
<b>Input:</b> "19:34"
<b>Output:</b> "19:39"
<b>Explanation:</b> The next closest time choosing from digits <b>1</b>, <b>9</b>, <b>3</b>, <b>4</b>, is <b>19:39</b>, which occurs 5 minutes later.  It is not <b>19:33</b>, because this occurs 23 hours and 59 minutes later.
</pre>
</p>

<p><b>Example 2:</b>
<pre>
<b>Input:</b> "23:59"
<b>Output:</b> "22:22"
<b>Explanation:</b> The next closest time choosing from digits <b>2</b>, <b>3</b>, <b>5</b>, <b>9</b>, is <b>22:22</b>. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    string nextClosestTime(string time) {
        set<char> digitSet;
        for (auto c : time) {
            if (c != ':') {
                digitSet.insert(c);
            }
        }
        
        vector<char> digits (digitSet.begin(), digitSet.end());

        ++time[4];
        char nextChar = next(digits, time[4]);
        if (nextChar != '#') {
            time[4] = nextChar;
            return time;
        } else {
            time[4] = digits[0];
        }
        
        ++time[3];
        nextChar = next(digits, time[3]);
        if (nextChar != '#') {
            time[3] = nextChar;
            if (time[3] < '6')  return time;
            else time[3] = digits[0];
        } else {
            time[3] = digits[0];
        }
        
        ++time[1];
        nextChar = next(digits, time[1]);
        if (nextChar != '#') {
            time[1] = nextChar;
            if (time[0] == '2' && time[1] > '3') {
                time[1] = digits[0];
            } else {
                return time;
            }
        } else {
            time[1] = digits[0];
        }
        
        ++time[0];
        nextChar = next(digits, time[0]);
        if (nextChar != '#') {
            time[0] = nextChar;
            if (time[0] > '2') {
                time[0] = digits[0];
            } else {
                return time;
            }
        } else {
            time[0] = digits[0];
        }
        
        return time;
    }
    
    char next(vector<char>& digits, char c) {
        auto it = lower_bound(digits.begin(), digits.end(), c);
        if (it != digits.end()) {
            return *it;
        } else {
            return '#';
        }
    }
};
```
