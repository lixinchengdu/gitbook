# 43. Multiply Strings

* *Difficulty: Medium*

* *Topics: Math, String*

* *Similar Questions:*

  * [Add Two Numbers](add-two-numbers.md)

  * [Plus One](plus-one.md)

  * [Add Binary](add-binary.md)

  * [Add Strings](add-strings.md)

## Problem:

<p>Given two non-negative integers <code>num1</code> and <code>num2</code> represented as strings, return the product of <code>num1</code> and <code>num2</code>, also represented as a string.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> num1 = &quot;2&quot;, num2 = &quot;3&quot;
<strong>Output:</strong> &quot;6&quot;</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> num1 = &quot;123&quot;, num2 = &quot;456&quot;
<strong>Output:</strong> &quot;56088&quot;
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li>The length of both <code>num1</code> and <code>num2</code> is &lt; 110.</li>
	<li>Both <code>num1</code> and <code>num2</code> contain&nbsp;only digits <code>0-9</code>.</li>
	<li>Both <code>num1</code> and <code>num2</code>&nbsp;do not contain any leading zero, except the number 0 itself.</li>
	<li>You <strong>must not use any built-in BigInteger library</strong> or <strong>convert the inputs to integer</strong> directly.</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    string multiply(string num1, string num2) {
        int len1 = num1.length();
        int len2 = num2.length();
        if (num1 == "0" || num2 == "0") return "0"; // this check is important
        
        vector<int> digits (len1 + len2, 0);
        
        for (int i = 0; i < len1; ++i) {
            for (int j = 0; j < len2; ++j) {
                digits[i + j + 1] += (num1[i] - '0') * (num2[j] - '0'); // remeber the position of digits.
            }
        }
        string ret;
        for (int i = digits.size() - 1; i > 0; --i) {
            int digit = digits[i] % 10;
            digits[i-1] += digits[i]/10;
            ret.push_back(digit + '0');
        }
        
        if (digits[0] > 0)  ret.push_back(digits[0] + '0');
        
        reverse(ret.begin(), ret.end());
        return ret;
    }
};
```

## Another more concise solution

It is possible to aggregate sum and carry. 

From [Huahua](https://zxi.mytechroad.com/blog/string/leetcode-43-multiply-strings/)

```c++
// Author: Huahua
// Running time: 4 ms
class Solution {
public:
  string multiply(string num1, string num2) {
    const int l1 = num1.length();
    const int l2 = num2.length();
    string ans(l1 + l2, '0');
    for (int i = l1 - 1; i >= 0; --i)
      for (int j = l2 - 1; j >= 0; --j) {
        int sum = (ans[i + j + 1] - '0') + (num1[i] - '0') * (num2[j] - '0');        
        ans[i + j + 1] = (sum % 10) + '0';
        ans[i + j] += sum / 10; // This line is not a problem if the order is from right to left
      }

    // ans[0] is guaranteed to be less than 10 due to math property
    for (int i = 0; i < ans.length(); ++i)
      if (ans[i] != '0' || i == ans.length() - 1) return ans.substr(i);
    return "";
  }
};
```
