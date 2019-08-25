# 202. Happy Number

* *Difficulty: Easy*

* *Topics: Hash Table, Math*

* *Similar Questions:*

  * [Linked List Cycle](linked-list-cycle.md)

  * [Add Digits](add-digits.md)

  * [Ugly Number](ugly-number.md)

## Problem:

<p>Write an algorithm to determine if a number is &quot;happy&quot;.</p>

<p>A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.</p>

<p><strong>Example:&nbsp;</strong></p>

<pre>
<strong>Input:</strong> 19
<strong>Output:</strong> true
<strong>Explanation: 
</strong>1<sup>2</sup> + 9<sup>2</sup> = 82
8<sup>2</sup> + 2<sup>2</sup> = 68
6<sup>2</sup> + 8<sup>2</sup> = 100
1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
</pre>
## Solutions:

```c++
class Solution {
public:
    bool isHappy(int n) {
      
        if (n <= 0) return false;
        if (n == 1) return true;
        unordered_set<int> seen;
        
        int nextVal = 0;
        for (;;) {
            nextVal = 0; // reset nextVal
            while (n > 0) {
                nextVal += (n%10) * (n%10);
                n /= 10;
            }
            
            if (nextVal == 1) return true;
            if (seen.count(nextVal) > 0)    return false;
            seen.insert(nextVal);
            n = nextVal;
        }

    }
};
```
