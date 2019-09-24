# 422. Valid Word Square

* *Difficulty: Easy*

* *Topics: *

* *Similar Questions:*

  * [Word Squares](word-squares.md)

  * [Toeplitz Matrix](toeplitz-matrix.md)

## Problem:

<p>Given a sequence of words, check whether it forms a valid word square.</p>

<p>A sequence of words forms a valid word square if the <i>k</i><sup>th</sup> row and column read the exact same string, where 0 &le; <i>k</i> &lt; max(numRows, numColumns).</p>

<p><b>Note:</b><br />
<ol>
<li>The number of words given is at least 1 and does not exceed 500.</li>
<li>Word length will be at least 1 and does not exceed 500.</li>
<li>Each word contains only lowercase English alphabet <code>a-z</code>.</li>
</ol>
</p>

<p><b>Example 1:</b>
<pre>
<b>Input:</b>
[
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]

<b>Output:</b>
true

<b>Explanation:</b>
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crmy".
The fourth row and fourth column both read "dtye".

Therefore, it is a valid word square.
</pre>
</p>

<p><b>Example 2:</b>
<pre>
<b>Input:</b>
[
  "abcd",
  "bnrt",
  "crm",
  "dt"
]

<b>Output:</b>
true

<b>Explanation:</b>
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crm".
The fourth row and fourth column both read "dt".

Therefore, it is a valid word square.
</pre>
</p>

<p><b>Example 3:</b>
<pre>
<b>Input:</b>
[
  "ball",
  "area",
  "read",
  "lady"
]

<b>Output:</b>
false

<b>Explanation:</b>
The third row reads "read" while the third column reads "lead".

Therefore, it is <b>NOT</b> a valid word square.
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    bool validWordSquare(vector<string>& words) {
        int m = words.size();
        if (m == 0) return true;
        int n = words[0].size();
        if (n == 0) return true;
        if (m != n) return false;
        
        for (int i = 0; i <m; ++i) {
            if (words[i].length() > m)  return false;
            for (int j = 0; j < i; ++j) {
                if (j >= words[i].length() && i >= words[j].length()) {
                    continue;
                }
                else if (j < words[i].length() && j < words[j].length()) {
                    if (words[i][j] != words[j][i]) return false;
                }
                else 
                    return false;
            }
        }
        
        return true;
        
    }
};
```
