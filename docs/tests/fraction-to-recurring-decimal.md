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
    string fractionToDecimal(long long numerator, long long denominator) {
        if (numerator == 0) return "0";
        bool sign = false;
        if ((abs(numerator) == numerator && abs(denominator) == denominator) || (abs(numerator) != numerator && abs(denominator) != denominator))
            sign = true;
        numerator = abs(numerator);
        denominator = abs(denominator);
        long long integerPart = numerator/denominator;
        long long residual = numerator%denominator;
        string result;
        //cout << sign << endl;
        if (!sign)  result += '-';
        result += to_string(integerPart);
        if (residual == 0)  {return result;}
        result += ".";
        int index = result.length();
        while (residual !=0)
        {
            if (residual2index.count(residual) > 0)
            {
                result.insert(residual2index[residual], 1,'(');
                result.append(1,')');
                return result;
            }
            int oldResidual = residual;
            int nextDigit = getNextDigit(residual, denominator);
            result.append(1, '0' + nextDigit);
            residual2index[oldResidual] = index++;
        }
        return result;
    }

private:
    int getNextDigit(long long& residual, long long denominator)
    {
        int digit = 0;
        residual *= 10;
        for (int i = 0; i < 10; i++)
        {
            if (i*denominator <= residual)
            {
                digit = i;
            }
            else
                break;
        }
        residual = (residual - digit * denominator);
        return digit;
    }
    
    unordered_map <long long, int> residual2index;
    
};
```
