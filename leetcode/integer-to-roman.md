# 12. Integer to Roman

* *Difficulty: Medium*

* *Topics: Math, String*

* *Similar Questions:*

  * [Roman to Integer](roman-to-integer.md)

  * [Integer to English Words](integer-to-english-words.md)

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
        vector<pair<char, int>> values = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000},
            {'?', 5000},
            {'*', 10000}
        };
        
        string ret;
        
        vector<int> digits;
        for (int i = 0; i < 4; ++i) {
            int digit = num % 10;
            num /= 10;
            digits.push_back(digit);
        }
        
        for (int i = 3; i >= 0; --i) {
            populateStr(ret, digits[i], values[i*2 + 2].first, values[i*2 + 1].first, values[i*2].first);
        }
        
        return ret;
    }
    
    void populateStr(string& ret, int digit, char tenChar, char fiveChar, char oneChar) {
        if (digit == 0) return;
        if (digit <= 3) {
            for (int i = 0; i < digit; ++i) {
                ret.push_back(oneChar);
            }
            return;
        }
        if (digit == 4) {
            ret.push_back(oneChar);
            ret.push_back(fiveChar);
            return;
        }
        if (digit <= 8) {
            ret.push_back(fiveChar);
            for (int i = 0; i < digit - 5; ++i) {
                ret.push_back(oneChar);
            }
            return;
        }
        if (digit == 9) {
            ret.push_back(oneChar);
            ret.push_back(tenChar);
            return;
        }
    }
};
```

### More concise solution1

From [Grandyang](https://www.cnblogs.com/grandyang/p/4123374.html)
```c++
class Solution {
public:
    string intToRoman(int num) {
        string res = "";
        vector<int> val{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        vector<string> str{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        for (int i = 0; i < val.size(); ++i) {
            while (num >= val[i]) {
                num -= val[i];
                res += str[i];
            }
        }
        return res;
    }
};
```

### More concise solution2
From [Grandyang](https://www.cnblogs.com/grandyang/p/4123374.html)
```c++
class Solution {
public:
    string intToRoman(int num) {
        string res = "";
        vector<string> v1{"", "M", "MM", "MMM"};
        vector<string> v2{"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        vector<string> v3{"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        vector<string> v4{"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        return v1[num / 1000] + v2[(num % 1000) / 100] + v3[(num % 100) / 10] + v4[num % 10];
    }
};
```
