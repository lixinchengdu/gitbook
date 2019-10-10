# 537. Complex Number Multiplication

* *Difficulty: Medium*

* *Topics: Math, String*

* *Similar Questions:*

## Problem:

<p>
Given two strings representing two <a href = "https://en.wikipedia.org/wiki/Complex_number">complex numbers</a>.</p>

<p>
You need to return a string representing their multiplication. Note i<sup>2</sup> = -1 according to the definition.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "1+1i", "1+1i"
<b>Output:</b> "0+2i"
<b>Explanation:</b> (1 + i) * (1 + i) = 1 + i<sup>2</sup> + 2 * i = 2i, and you need convert it to the form of 0+2i.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> "1+-1i", "1+-1i"
<b>Output:</b> "0+-2i"
<b>Explanation:</b> (1 - i) * (1 - i) = 1 + i<sup>2</sup> - 2 * i = -2i, and you need convert it to the form of 0+-2i.
</pre>
</p>

<p><b>Note:</b>
<ol>
<li>The input strings will not have extra blank.</li>
<li>The input strings will be given in the form of <b>a+bi</b>, where the integer <b>a</b> and <b>b</b> will both belong to the range of [-100, 100]. And <b>the output should be also in this form</b>.</li>
</ol>
</p>
## Solutions:

```c++
class Solution {
public:
    string complexNumberMultiply(string a, string b) {
        auto complex1 = parse(a);
        auto complex2 = parse(b);
        
        int real = complex1.first * complex2.first - complex1.second * complex2.second;
        int img = complex1.first * complex2.second + complex2.first * complex1.second;
        
        return to_string(real) + "+" + to_string(img) + "i";
    }
    
private:
    pair<int, int> parse(const string& str) {
        int real = 0;
        int img = 0;
        int realSign = 1;
        int imgSign = 1;
        
        int pos = 0;
        if (str[pos] == '-') {
            realSign = -1;
            ++pos;
        }
        while (str[pos] != '+') {
            real = real * 10 + str[pos] - '0';
            ++pos;
        }
        
        ++pos;
        
        if (str[pos] == '-') {
            imgSign = -1;
            ++pos;
        }
        while (str[pos] != 'i') {
            img = 10 * img + str[pos] - '0';
            ++pos;
        }
        
        return {real * realSign, img * imgSign};
    }
    
};
```
