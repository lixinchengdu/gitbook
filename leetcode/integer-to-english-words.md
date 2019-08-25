# 273. Integer to English Words

* *Difficulty: Hard*

* *Topics: Math, String*

* *Similar Questions:*

  * [Integer to Roman](integer-to-roman.md)

## Problem:

<p>Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2<sup>31</sup> - 1.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 123
<b>Output:</b> &quot;One Hundred Twenty Three&quot;
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> 12345
<b>Output:</b> &quot;Twelve Thousand Three Hundred Forty Five&quot;</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> 1234567
<b>Output:</b> &quot;One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven&quot;
</pre>

<p><b>Example 4:</b></p>

<pre>
<b>Input:</b> 1234567891
<b>Output:</b> &quot;One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One&quot;
</pre>

## Solutions:

```c++
class Solution {
public:
    string numberToWords(int num) {
        if (num == 0)   return "Zero";
        string ret;
        if (num >= 1000000000) {
            ret += lessThousand(num / 1000000000) + " Billion ";
            num = num % 1000000000;
        }
        if (num >= 1000000) {
            ret += lessThousand(num / 1000000) + " Million ";
            num = num % 1000000;
        }
        
        if (num >= 1000) {
            ret += lessThousand(num / 1000) + " Thousand ";
            num = num % 1000;
        }
        
        ret += lessThousand(num);
        
        if (ret.back() == ' ') {
            ret.pop_back();
        }
        
        return ret;
    }
    
private:
    string lessThousand(int num) {
        string twenty[] {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
        string hundred[] {"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
        string ret;
        if (num / 100 > 0) {
            ret = twenty[num / 100] + " " + "Hundred ";
            num = num % 100;
        }
        
        if (num >= 20) {
            ret += hundred[num/10 - 2] + " ";
            num = num % 10;
        }
        
        if (num > 0) {
            ret += twenty[num];
        }
        
        if (ret.length() > 0 && ret.back() == ' ') {
            ret.pop_back();
        }
        
        return ret;
    }
};
```
