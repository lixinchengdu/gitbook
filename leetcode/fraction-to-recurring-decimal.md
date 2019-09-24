# 166. Fraction to Recurring Decimal

* *Difficulty: Medium*

* *Topics: Hash Table, Math*

* *Similar Questions:*

## Problem:

<p>Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.</p>

<p>If the fractional part is repeating, enclose the repeating part in parentheses.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> numerator = 1, denominator = 2
<strong>Output:</strong> &quot;0.5&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> numerator = 2, denominator = 1
<strong>Output:</strong> &quot;2&quot;</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> numerator = 2, denominator = 3
<strong>Output: </strong>&quot;0.(6)&quot;
</pre>

## Solutions:

```c++
class Solution {
public:
    string fractionToDecimal(int n, int d) {
        
        int sign = 1;
        if (((n >> 31) & 1) != ((d >> 31) & 1))  sign = -1;
        
        long numerator = n;
        long denominator = d;
        
        numerator = abs(numerator);
        denominator = abs(denominator);
        
        long integral = numerator / denominator; // integral should be of type long
        numerator = numerator % denominator;
        
        string fractional;
        computeFraction(numerator * 10, denominator, fractional);
        
        string ret;
        if (numerator == 0 && integral == 0)    return "0"; // this is essential
        if (sign == -1) {
            ret.push_back('-');
        }
        
        ret.append(to_string(integral));
        if (numerator == 0) return ret;
        
        ret.push_back('.');
        ret.append(fractional);
        
        return ret;
    }
    
    void computeFraction(long numerator, long denominator, string& fractional) {
        vector<int> digits;
        unordered_map<int, int> indices;
        while (numerator != 0) {
            if (indices.count(numerator)) {
                int unRepeatingIndex = indices[numerator];
                for (int i = 0; i < unRepeatingIndex; ++i) {
                    fractional.push_back('0' + digits[i]);
                }
                fractional.push_back('(');
                for (int i = unRepeatingIndex; i < digits.size(); ++i) {
                    fractional.push_back('0' + digits[i]);
                }
                fractional.push_back(')');
                return;
            }
            int q = numerator / denominator;
            digits.push_back(q);
            indices[numerator] = digits.size() - 1;
            numerator = (numerator % denominator) * 10;
        }
        
        for (int i = 0; i < digits.size(); ++i) {
            fractional.push_back('0' + digits[i]);
        }
        
    }
};
```
