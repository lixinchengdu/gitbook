# 551. Student Attendance Record I

* *Difficulty: Easy*

* *Topics: String*

* *Similar Questions:*

  * [Student Attendance Record II](student-attendance-record-ii.md)

## Problem:

You are given a string representing an attendance record for a student. The record only contains the following three characters:

<p>
<ol>
<li><b>'A'</b> : Absent. </li>
<li><b>'L'</b> : Late.</li>
<li> <b>'P'</b> : Present. </li>
</ol>
</p>

<p>
A student could be rewarded if his attendance record doesn't contain <b>more than one 'A' (absent)</b> or <b>more than two continuous 'L' (late)</b>.    </p>

<p>You need to return whether the student could be rewarded according to his attendance record.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "PPALLP"
<b>Output:</b> True
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> "PPALLL"
<b>Output:</b> False
</pre>
</p>



## Solutions:

```c++
class Solution {
public:
    bool checkRecord(string s) {
        int absentCount = 0;
        int lateCount = 0;
        for (auto c : s) {
            switch(c) {
                case 'A':
                    if (++absentCount == 2) return false;
                    lateCount = 0;
                    break;
                case 'L':
                    if (++lateCount == 3)   return false;
                    break;
                case 'P':
                    lateCount = 0;
            }
        }
        
        return true;
    }
};
```
