# 1088. Number of Days in a Month

* *Difficulty: Easy*

* *Topics: *

* *Similar Questions:*

## Problem:

<p>Given a year <code>Y</code> and a month <code>M</code>, return how many days there are in that month.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>Y = <span id="example-input-1-1">1992</span>, M = <span id="example-input-1-2">7</span>
<strong>Output: </strong><span id="example-output-1">31</span>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>Y = <span id="example-input-2-1">2000</span>, M = <span id="example-input-2-2">2</span>
<strong>Output: </strong><span id="example-output-2">29</span>
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>Y = <span id="example-input-3-1">1900</span>, M = <span id="example-input-3-2">2</span>
<strong>Output: </strong><span id="example-output-3">28</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1583 &lt;= Y &lt;= 2100</code></li>
	<li><code>1 &lt;= M &lt;= 12</code></li>
</ol>

## Solutions:

```c++
class Solution {
public:
    int numberOfDays(int Y, int M) {
        int dayNum[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if (Y % 100 == 0) {
            if (Y % 400 == 0) {
                dayNum[1] = 29;
            }
        } else {
            if (Y % 4 == 0) {
                dayNum[1] = 29;
            }
        }
        
        return dayNum[M - 1];
    }
};
```
