# 273. Integer to English Words

* *Difficulty: Hard*

* *Topics: Math, String*

* *Similar Questions:*

  * [Integer to Roman](./tests/integer-to-english-words.md)

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
        int original = num;
        string result = "";
        if (!num){result = "Zero"; return result;}
        int unit = num%1000;
        num /= 1000;
        int thousand = num%1000;
        num /= 1000;
        int million = num%1000;
        num /= 1000;
        int billion = num%1000;
        //cout << billion << endl;
        //cout << million << endl;
        //cout << thousand << endl;
        if (billion > 0)    {result += (getEnglish(billion) + " Billion"); if (original%1000000000)   result += " ";}
        if (million > 0)    {result += (getEnglish(million) + " Million"); if (original%1000000)   result += " ";}
        if (thousand > 0)   {result += (getEnglish(thousand) + " Thousand"); ;if(original%1000 > 0)  { result += " ";}}
        if (unit > 0)   result += getEnglish(unit);
        return result;
        
    }

private:

string getEnglish(int n)
{
    string belowtwenty[] = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
string tens[] = {"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    string word = "";
    int unitDigit = n%10;
    n = n/10;
    int tenDigit = n%10;
    n = n/10;
    int hundredDigit = n%10;
    if (hundredDigit)   word = belowtwenty[hundredDigit] + " Hundred";
    if (hundredDigit && (tenDigit || unitDigit))    word += " ";
    if (tenDigit >= 2)  {word += (tens[tenDigit-2]); if (unitDigit) {word += (" " + belowtwenty[unitDigit]);}    return word;}
    else
    {
        int val = 10*tenDigit + unitDigit;
        if (unitDigit || tenDigit)  word += (belowtwenty[val]);
        return word;
    }
}

};
```
