# 1044. Find Common Characters

* *Difficulty: Easy*

* *Topics: Array, Hash Table*

* *Similar Questions:*

  * [Intersection of Two Arrays II](intersection-of-two-arrays-ii.md)

## Problem:

<p>Given an array&nbsp;<code>A</code> of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list <strong>(including duplicates)</strong>.&nbsp;&nbsp;For example, if a character occurs 3 times&nbsp;in all strings but not 4 times, you need to include that character three times&nbsp;in the final answer.</p>

<p>You may return the answer in any order.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;bella&quot;,&quot;label&quot;,&quot;roller&quot;]</span>
<strong>Output: </strong><span id="example-output-1">[&quot;e&quot;,&quot;l&quot;,&quot;l&quot;]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[&quot;cool&quot;,&quot;lock&quot;,&quot;cook&quot;]</span>
<strong>Output: </strong><span id="example-output-2">[&quot;c&quot;,&quot;o&quot;]</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 100</code></li>
	<li><code>1 &lt;= A[i].length &lt;= 100</code></li>
	<li><code>A[i][j]</code> is a lowercase letter</li>
</ol>
</div>
</div>
## Solutions:

```c++
class Solution {
public:
    vector<string> commonChars(vector<string>& A) {
        if (A.size() == 0)  return {};
        
        vector<int> common = countFreq(A[0]);
        for (int i = 1; i < A.size(); ++i) {
            vector<int> freq = countFreq(A[i]);
            for (int j = 0; j < 26; ++j) {
                common[j] = min(common[j], freq[j]);
            }
        }
        
        vector<string> ret;
        for (int i = 0; i < 26; ++i) {
            for (int j = 0; j < common[i]; ++j) {
                ret.push_back(string(1, 'a' + i));
            }
        }
        
        return ret;  
    }
    
private:
    vector<int> countFreq(const string& str) {
        vector<int> freq(26, 0);
        for (auto& c : str) {
            ++freq[c - 'a'];
        }
        
        return freq;
    }
    
};
```
