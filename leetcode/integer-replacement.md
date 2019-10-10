# 397. Integer Replacement

* *Difficulty: Medium*

* *Topics: Math, Bit Manipulation*

* *Similar Questions:*

## Problem:

<p>
Given a positive integer <i>n</i> and you can do operations as follow:
</p>

<p>
<ol>
<li>If <i>n</i> is even, replace <i>n</i> with <code><i>n</i>/2</code>.</li>
<li>If <i>n</i> is odd, you can replace <i>n</i> with either <code><i>n</i> + 1</code> or <code><i>n</i> - 1</code>.</li>
</ol>
</p>

<p>
What is the minimum number of replacements needed for <i>n</i> to become 1?
</p>

</p>

<p><b>Example 1:</b>
<pre>
<b>Input:</b>
8

<b>Output:</b>
3

<b>Explanation:</b>
8 -> 4 -> 2 -> 1
</pre>
</p>

<p><b>Example 2:</b>
<pre>
<b>Input:</b>
7

<b>Output:</b>
4

<b>Explanation:</b>
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    int integerReplacement(int N) {
        int count = 0;
        long n = N; // to prevent overflow
        while (n > 3) {
            if (n % 2 == 0) {
                n = (n >> 1);
            } else {
                if ((n & 0x2) == 0) {
                    n -= 1;
                } else {
                    n += 1;
                }
            }
            ++count;
        }
        
        if (n == 3) return count + 2; // special check
        if (n == 2) return count + 1; // special check
        return count;
    }
};
```
