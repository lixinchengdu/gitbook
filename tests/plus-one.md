# 66. Plus One

* *Difficulty: Easy*

* *Topics: Array*

* *Similar Questions:*

  * [Multiply Strings](./tests/plus-one.md)

  * [Add Binary](./tests/plus-one.md)

  * [Plus One Linked List](./tests/plus-one.md)

  * [Add to Array-Form of Integer](./tests/plus-one.md)

## Problem:

<p>Given a <strong>non-empty</strong> array of digits&nbsp;representing a non-negative integer, plus one to the integer.</p>

<p>The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.</p>

<p>You may assume the integer does not contain any leading zero, except the number 0 itself.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3]
<strong>Output:</strong> [1,2,4]
<strong>Explanation:</strong> The array represents the integer 123.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [4,3,2,1]
<strong>Output:</strong> [4,3,2,2]
<strong>Explanation:</strong> The array represents the integer 4321.
</pre>
## Solutions:

```c++
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 1;
        for (auto rit = digits.rbegin(); rit != digits.rend(); ++rit) {
            (*rit) += carry;
            if (*rit == 10) {
                *rit = 0;
                carry = 1;
            } else {
                return digits;
            }
        }
        
        digits.insert(digits.begin(), 1);
        return digits;
    }
};
```
