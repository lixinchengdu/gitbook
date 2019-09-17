# 1297. Maximum Number of Balloons

* *Difficulty: Easy*

* *Topics: Hash Table, String*

* *Similar Questions:*

## Problem:

<p>Given a string&nbsp;<code>text</code>, you want to use the characters of&nbsp;<code>text</code>&nbsp;to form as many instances of the word <strong>&quot;balloon&quot;</strong> as possible.</p>

<p>You can use each character in <code>text</code> <strong>at most once</strong>. Return the maximum number of instances that can be formed.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG" style="width: 132px; height: 35px;" /></strong></p>

<pre>
<strong>Input:</strong> text = &quot;nlaebolko&quot;
<strong>Output:</strong> 1
</pre>

<p><strong>Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG" style="width: 267px; height: 35px;" /></strong></p>

<pre>
<strong>Input:</strong> text = &quot;loonbalxballpoon&quot;
<strong>Output:</strong> 2
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> text = &quot;leetcode&quot;
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 10^4</code></li>
	<li><code>text</code>&nbsp;consists of lower case English letters only.</li>
</ul>
## Solutions:

```c++
class Solution {
public:
    int maxNumberOfBalloons(string text) {
        int charCount[26] = {0};
        for (auto& c : text) {
            ++charCount[c - 'a'];
        }
        
        int ret = INT_MAX;
        string target = "baon";
        
        for (auto& c : target) {
            ret = min(ret, charCount[c - 'a']);
        }
        
        ret = min(ret, charCount['l' - 'a'] / 2);
        ret = min(ret, charCount['o' - 'a'] / 2);
        
        return ret == INT_MAX ? 0 : ret;
    }
};
```
