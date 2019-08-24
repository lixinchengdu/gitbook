# 278. First Bad Version

* *Difficulty: Easy*

* *Topics: Binary Search*

* *Similar Questions:*

  * [Find First and Last Position of Element in Sorted Array](./tests/first-bad-version.md)

  * [Search Insert Position](./tests/first-bad-version.md)

  * [Guess Number Higher or Lower](./tests/first-bad-version.md)

## Problem:

<p>You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.</p>

<p>Suppose you have <code>n</code> versions <code>[1, 2, ..., n]</code> and you want to find out the first bad one, which causes all the following ones to be bad.</p>

<p>You are given an API <code>bool isBadVersion(version)</code> which will return whether <code>version</code> is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.</p>

<p><b>Example:</b></p>

<pre>
Given n = 5, and version = 4 is the first bad version.

<code>call isBadVersion(3) -&gt; false
call isBadVersion(5)&nbsp;-&gt; true
call isBadVersion(4)&nbsp;-&gt; true

Then 4 is the first bad version.&nbsp;</code>
</pre>

## Solutions:

```c++
// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int low = 1, high = n;
        while (low + 1 < high)
        {
            int mid = low + (high-low)/2;
            if (isBadVersion(mid))
            {
                high = mid;
            }
            else
            {
                low = mid;
            }
        }
        if (isBadVersion(low))  return low;
        else return high;
        
    }
};
```
