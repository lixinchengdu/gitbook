# 374. Guess Number Higher or Lower

* *Difficulty: Easy*

* *Topics: Binary Search*

* *Similar Questions:*

  * [First Bad Version](first-bad-version.md)

  * [Guess Number Higher or Lower II](guess-number-higher-or-lower-ii.md)

  * [Find K Closest Elements](find-k-closest-elements.md)

## Problem:

<p>We are playing the Guess Game. The game is as follows:</p>

<p>I pick a number from <b>1</b> to <b><i>n</i></b>. You have to guess which number I picked.</p>

<p>Every time you guess wrong, I&#39;ll tell you whether the number is higher or lower.</p>

<p>You call a pre-defined API <code>guess(int num)</code> which returns 3 possible results (<code>-1</code>, <code>1</code>, or <code>0</code>):</p>

<pre>
-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
</pre>

<p><strong>Example :</strong></p>

<div>
<pre>
<strong>Input: </strong>n = <span id="example-input-1-1">10</span>, pick = <span id="example-input-1-2">6</span>
<strong>Output: </strong><span id="example-output-1">6</span>
</pre>
</div>

## Solutions:

```c++
// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int left = 1;
        int right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            int ret = guess(mid);
            if (ret == 0)   return mid;
            else if (ret == 1) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return left;
    }
};
```
