# 12. Integer to Roman

* *Difficulty: Medium*

* *Topics: Math, String*

* *Similar Questions:*

  * [Roman to Integer](./tests/integer-to-roman.md)

  * [Integer to English Words](./tests/integer-to-roman.md)

## Problem:

<p>Roman numerals are represented by seven different symbols:&nbsp;<code>I</code>, <code>V</code>, <code>X</code>, <code>L</code>, <code>C</code>, <code>D</code> and <code>M</code>.</p>

<pre>
<strong>Symbol</strong>       <strong>Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

<p>For example,&nbsp;two is written as <code>II</code>&nbsp;in Roman numeral, just two one&#39;s added together. Twelve is written as, <code>XII</code>, which is simply <code>X</code> + <code>II</code>. The number twenty seven is written as <code>XXVII</code>, which is <code>XX</code> + <code>V</code> + <code>II</code>.</p>

<p>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code>IX</code>. There are six instances where subtraction is used:</p>

<ul>
	<li><code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9.&nbsp;</li>
	<li><code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90.&nbsp;</li>
	<li><code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.</li>
</ul>

<p>Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;3
<strong>Output:</strong> &quot;III&quot;</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;4
<strong>Output:</strong> &quot;IV&quot;</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;9
<strong>Output:</strong> &quot;IX&quot;</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;58
<strong>Output:</strong> &quot;LVIII&quot;
<strong>Explanation:</strong> L = 50, V = 5, III = 3.
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;1994
<strong>Output:</strong> &quot;MCMXCIV&quot;
<strong>Explanation:</strong> M = 1000, CM = 900, XC = 90 and IV = 4.</pre>

## Solutions:

```c++
class Solution {
public:
    string intToRoman(int num) {
        int udigit = num%10;
        num /= 10;
        int tdigit = num%10;
        num /= 10;
        int hdigit = num%10;
        num /= 10;
        int kdigit = num%10;
        string result;
        result += getRoman(kdigit, 'M', 'X', 'X');
        result += getRoman(hdigit, 'C', 'D', 'M');
        result += getRoman(tdigit, 'X', 'L', 'C');
        result += getRoman(udigit, 'I', 'V', 'X');
        return result;
    }
    
    string getRoman(int num, char unit, char fiveUnit, char nextUnit)
    {
        string result;
        if (num == 0)   return result;
        if (num == 4)   return string(1, unit) + string(1,fiveUnit); 
        if (num == 9)   return string(1, unit) + string(1, nextUnit);
        if (num <= 3)
        {
            for (int i = 0; i < num; i++)
            {
                result += string(1, unit);
            }
            return result;
        }
        if(num >= 5)
        {
            result += string(1, fiveUnit);
            result += getRoman(num - 5, unit, fiveUnit, nextUnit);
            return result;
        }
    }
};
```
