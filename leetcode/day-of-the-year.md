# 1260. Day of the Year

* *Difficulty: Easy*

* *Topics: Math*

* *Similar Questions:*

## Problem:

<p>Given a string <code>date</code> representing a <a href="https://en.wikipedia.org/wiki/Gregorian_calendar" target="_blank">Gregorian&nbsp;calendar</a> date formatted as <code>YYYY-MM-DD</code>, return the day number of the year.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> date = &quot;2019-01-09&quot;
<strong>Output:</strong> 9
<strong>Explanation:</strong> Given date is the 9th day of the year in 2019.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> date = &quot;2019-02-10&quot;
<strong>Output:</strong> 41
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> date = &quot;2003-03-01&quot;
<strong>Output:</strong> 60
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> date = &quot;2004-03-01&quot;
<strong>Output:</strong> 61
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>date.length == 10</code></li>
	<li><code>date[4] == date[7] == &#39;-&#39;</code>, and all other <code>date[i]</code>&#39;s are digits</li>
	<li><code>date</code> represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.</li>
</ul>
## Solutions:

```c++
class Solution {
public:
    int dayOfYear(string date) {
        int year = 0;
        for (int i = 0; i < 4; ++i) {
            year = 10 * year + date[i] - '0';
        }
        
        int month = 10 * (date[5] - '0') + date[6] - '0';
        int day = 10 * (date[8] - '0') + date[9] - '0';
        
        int dayNum[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}; // non-leap year
        
        bool leapYear = false;
        if ((year % 100 == 0 && year % 400 == 0) || (year % 100 != 0 && year % 4 == 0)) {
            leapYear = true;
        }
        
        if (leapYear) {
            dayNum[1] = 29;
        }
        
        int count = 0;
        for (int i = 0; i < month - 1; ++i) {
            count += dayNum[i];
        }
        
        return count + day;
    }
};
```
