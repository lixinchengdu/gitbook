# 1076. Brace Expansion

* *Difficulty: Medium*

* *Topics: Backtracking*

* *Similar Questions:*

  * [Decode String](decode-string.md)

  * [Letter Case Permutation](letter-case-permutation.md)

  * [Brace Expansion II](brace-expansion-ii.md)

## Problem:

<p>A string <code>S</code>&nbsp;represents a list of words.</p>

<p>Each letter in the word has 1 or more options.&nbsp; If there is one option, the letter is represented as is.&nbsp; If there is more than one option, then curly braces delimit the options.&nbsp; For example, <code>&quot;{a,b,c}&quot;</code> represents options <code>[&quot;a&quot;, &quot;b&quot;, &quot;c&quot;]</code>.</p>

<p>For example, <code>&quot;{a,b,c}d{e,f}&quot;</code> represents the list <code>[&quot;ade&quot;, &quot;adf&quot;, &quot;bde&quot;, &quot;bdf&quot;, &quot;cde&quot;, &quot;cdf&quot;]</code>.</p>

<p>Return all words that can be formed in this manner, in lexicographical order.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;{a,b}c{d,e}f&quot;</span>
<strong>Output: </strong><span id="example-output-1">[&quot;acdf&quot;,&quot;acef&quot;,&quot;bcdf&quot;,&quot;bcef&quot;]</span>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;abcd&quot;</span>
<strong>Output: </strong><span id="example-output-2">[&quot;abcd&quot;]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= S.length &lt;= 50</code></li>
	<li>There are no&nbsp;nested curly brackets.</li>
	<li>All characters inside a pair of&nbsp;consecutive opening and ending curly brackets are different.</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    vector<string> expand(string S) {
        set<string> ret;
        string path;
        helper(S, 0, path, ret);
        return {ret.begin(), ret.end()};
    }
    
private:
    void helper(const string& S, int pos, string& path, set<string>& ret) {
        if (pos == S.length()) {
            ret.insert(path);
            return;
        }
        
        string origin = path;
        while (pos < S.length() && S[pos] != '{') {
            path.push_back(S[pos++]);
        }
        
        if (S[pos] == '{') {
            ++pos; 
            vector<char> letters;
            while (S[pos] != '}') {
                if (S[pos] == ',') {
                    ++pos;
                } else {
                    letters.push_back(S[pos++]);
                }
            }
            
            for (char& c : letters) {
                path.push_back(c);
                helper(S, pos + 1, path, ret);
                path.pop_back();
            }
            path = origin;
            return;
        }
        
        ret.insert(path);
        path = origin;
        return;
    }
    
};
```
