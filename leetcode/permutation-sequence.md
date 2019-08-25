# 60. Permutation Sequence

* *Difficulty: Medium*

* *Topics: Math, Backtracking*

* *Similar Questions:*

  * [Next Permutation](next-permutation.md)

  * [Permutations](permutations.md)

## Problem:

<p>The set <code>[1,2,3,...,<em>n</em>]</code> contains a total of <em>n</em>! unique permutations.</p>

<p>By listing and labeling all of the permutations in order, we get the following sequence for <em>n</em> = 3:</p>

<ol>
	<li><code>&quot;123&quot;</code></li>
	<li><code>&quot;132&quot;</code></li>
	<li><code>&quot;213&quot;</code></li>
	<li><code>&quot;231&quot;</code></li>
	<li><code>&quot;312&quot;</code></li>
	<li><code>&quot;321&quot;</code></li>
</ol>

<p>Given <em>n</em> and <em>k</em>, return the <em>k</em><sup>th</sup> permutation sequence.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Given <em>n</em> will be between 1 and 9 inclusive.</li>
	<li>Given&nbsp;<em>k</em>&nbsp;will be between 1 and <em>n</em>! inclusive.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, k = 3
<strong>Output:</strong> &quot;213&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4, k = 9
<strong>Output:</strong> &quot;2314&quot;
</pre>

## Solutions:

```c++
class Solution {
public:
    string getPermutation(int n, int k) {
        string digits = "123456789";
        digits = digits.substr(0, n);
        if (n == 1) return "1";
        int base = 1;
        for (int i = 1; i < n; ++i) {
            base *= i;
        }
        
       helper(digits, base, k - 1);
        return ret;
    }
    
    void helper(string& digits, int base, int k) {
        cout << base << endl;
       if (digits.length() == 0)    return; 
        int index = k/base;
        ret.push_back(digits[index]);
        digits.erase(index, 1);
        if (digits.length() == 1) {
            ret.push_back(digits[0]);
            return;
        }
        int newBase = base/(digits.length());
        helper(digits, newBase, k - index * base);
    }
private:
    string ret;

};
```
