# 9. Palindrome Number

* *Difficulty: Easy*

* *Topics: Math*

* *Similar Questions:*

  * [Palindrome Linked List](./tests/palindrome-number.md)

## Problem:

<p>Determine whether an integer is a palindrome. An integer&nbsp;is&nbsp;a&nbsp;palindrome when it&nbsp;reads the same backward as forward.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 121
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>

<p><strong>Follow up:</strong></p>

<p>Coud you solve&nbsp;it without converting the integer to a string?</p>

## Solutions:

```c++
#include <math.h>
class Solution {
public:
    bool isPalindrome(int x) {

        if (x < 0)  return false;
        int DigitNumber = 0;
        int aux = x;
        while (aux > 0)
        {
            DigitNumber ++;
            aux /= 10;
        }
        bool isPalindromeflag = true;
        aux = x;
        int most = 0;
        int least = 0;
        for (int i = 1; i < DigitNumber; i=i+2)
        {
            most = aux/pow(10,DigitNumber-i);
            aux -= most*pow(10,DigitNumber-i);
            least = aux%10;
            aux /= 10;
            cout << "most:" << most << endl;
            cout << "least:" << least << endl;
            
            if (least!=most)
            {
                isPalindromeflag = false;
                break;
            }
        }
        
        return isPalindromeflag;
        
        
    }
};
```
