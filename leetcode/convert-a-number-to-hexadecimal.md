# 405. Convert a Number to Hexadecimal

* *Difficulty: Easy*

* *Topics: Bit Manipulation*

* *Similar Questions:*

## Problem:

<p>
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, <a href="https://en.wikipedia.org/wiki/Two%27s_complement" target="_blank">two’s complement</a> method is used.
</p>

<p><b>Note:</b>
<ol>
<li>All letters in hexadecimal (<code>a-f</code>) must be in lowercase.</li>
<li>The hexadecimal string must not contain extra leading <code>0</code>s. If the number is zero, it is represented by a single zero character <code>'0'</code>; otherwise, the first character in the hexadecimal string will not be the zero character.</li>
<li>The given number is guaranteed to fit within the range of a 32-bit signed integer.</li>
<li>You <b>must not use <i>any</i> method provided by the library</b> which converts/formats the number to hex directly.</li>
</ol>
</p>

<p><b>Example 1:</b>
<pre>
Input:
26

Output:
"1a"
</pre>
</p>

<p><b>Example 2:</b>
<pre>
Input:
-1

Output:
"ffffffff"
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    string toHex(int num) {
        bool sign = (num >= 0);
        if (!sign) {
            num += INT_MAX;
            num += 1;
        }
        
        string ret;
        if (num == 0) { // this check is important!
            ret.push_back('0');
        }
        while (num > 0) {
            ret.push_back(decimalToHex(num % 16));
            num /= 16;
        }
        
        if (!sign) {
            while (ret.size() != 8) {
                ret.push_back('0');
            }
            ret.back() = decimalToHex(ret.back() - '0' + 8);
        }
        
        reverse(ret.begin(), ret.end());
        return ret;
    }
    
private:
    char decimalToHex(int val) {
        if (val < 10)   return '0' + val;
        else return 'a' + (val - 10);
    }
    
};
```
