# 306. Additive Number

* *Difficulty: Medium*

* *Topics: Backtracking*

* *Similar Questions:*

  * [Split Array into Fibonacci Sequence](split-array-into-fibonacci-sequence.md)

## Problem:

<p>Additive number is a string whose digits can form additive sequence.</p>

<p>A valid additive sequence should contain <b>at least</b> three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.</p>

<p>Given a string containing only digits <code>&#39;0&#39;-&#39;9&#39;</code>, write a function to determine if it&#39;s an additive number.</p>

<p><b>Note:</b> Numbers in the additive sequence <b>cannot</b> have leading zeros, so sequence <code>1, 2, 03</code> or <code>1, 02, 3</code> is invalid.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <code>&quot;112358&quot;</code>
<b>Output:</b> true 
<strong>Explanation: </strong>The digits can form an additive sequence: <code>1, 1, 2, 3, 5, 8</code>. 
&nbsp;            1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> <code>&quot;199100199&quot;</code>
<b>Output:</b> true 
<strong>Explanation: </strong>The additive sequence is: <code>1, 99, 100, 199</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">.</span>&nbsp;
&nbsp;            1 + 99 = 100, 99 + 100 = 199</pre>

<p><b>Follow up:</b><br />
How would you handle overflow for very large input integers?</p>
## Solutions:

```c++
class Solution {
public:
    bool isAdditiveNumber(string num) {
        //return isFabonacii(num, 0, 1);
        if (num.size() < 3) return false;
        for (int i = 0; i <= num.length() - 3; ++i) {
            for (int j = i + 1; j <= num.length() - 2; ++j) {
                cout << i << " " << j << endl;
                if (isFabonacii(num, i, j)) return true;
            }
        }
        return false;
    }
    
    bool isFabonacii(string& num, int i, int j) {
        int pos = 0;
        string a = num.substr(0, i + 1);
        if (leadingZero(a)) return false;
        pos = i;
        string b = num.substr(i + 1, j - i);
        if (leadingZero(b)) return false;
        pos = j;
        string c = addStrings(a, b);
        if (leadingZero(c)) return false;
        pos = j + c.length();
        
        while (pos < num.length() - 1) {
            cout << a << " " << b << endl;
            a = b;
            b = c;
            c = addStrings(a, b);
            if (leadingZero(c)) return false;
            if (c != num.substr(pos + 1, c.length()))   return false;
            pos += c.length();
        }
        
        return (pos == num.length() - 1 && c == num.substr(num.length() - c.length(), c.length()));
    }
    
    string addStrings(string num1, string num2) const {
        string ret;
        int carry = 0;
        int i1 = num1.length() - 1;
        int i2 = num2.length() - 1; 
        
        while (carry != 0 || i1 >= 0 && i2 >= 0) {
            int value = carry + (i1 >= 0 ? num1[i1--] - '0': 0) + (i2 >= 0 ? num2[i2--] - '0' : 0);
            ret.push_back(value % 10 + '0');
            carry = value / 10;
        }
        
        reverse(ret.begin(), ret.end());
        
        if (i1 >= 0) {
            ret = num1.substr(0, i1 + 1) + ret;
        }
        
        if (i2 >= 0) {
            ret = num2.substr(0, i2 + 1) + ret;
        }
        
        return ret;
    }
    
    bool leadingZero(string num) {
        return num.length() > 1 && num[0] == '0';
    }
};
```
