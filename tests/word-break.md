# 139. Word Break

* *Difficulty: Medium*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Word Break II](./tests/word-break.md)

## Problem:

<p>Given a <strong>non-empty</strong> string <em>s</em> and a dictionary <em>wordDict</em> containing a list of <strong>non-empty</strong> words, determine if <em>s</em> can be segmented into a space-separated sequence of one or more dictionary words.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The same word in the dictionary may be reused multiple times in the segmentation.</li>
	<li>You may assume the dictionary does not contain duplicate words.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leetcode&quot;, wordDict = [&quot;leet&quot;, &quot;code&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because <code>&quot;leetcode&quot;</code> can be segmented as <code>&quot;leet code&quot;</code>.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;applepenapple&quot;, wordDict = [&quot;apple&quot;, &quot;pen&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because <code>&quot;</code>applepenapple<code>&quot;</code> can be segmented as <code>&quot;</code>apple pen apple<code>&quot;</code>.
&nbsp;            Note that you are allowed to reuse a dictionary word.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;catsandog&quot;, wordDict = [&quot;cats&quot;, &quot;dog&quot;, &quot;sand&quot;, &quot;and&quot;, &quot;cat&quot;]
<strong>Output:</strong> false
</pre>

## Solutions:

```c++
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        map<string, bool> cache;
        set<string> Dict;
        for (auto word:wordDict)
        {
            Dict.insert(word);
        }
      //  for (auto word: Dict)
      //  {
     //       cout << word << endl;
     //   }
      //  cout << bool(Dict.find("leet") != Dict.end()) << endl;
        return helper(s, Dict, cache);
    }
    
    bool helper(string s, set<string>& wordDict, map<string, bool>& cache)
    {
        if (s.length() == 0) return true;
        if (cache.find(s) != cache.end())   return cache[s];
        for (int i = 0; i < s.length(); i++)
        {
            string prefix = s.substr(0, i);
            string suffix = s.substr(i);
          //  cout << prefix << " " << suffix << endl;
         //   cout << bool(wordDict.find(suffix) != wordDict.end()) << endl;
            cache[s] = (wordDict.find(suffix) != wordDict.end() && helper(prefix, wordDict, cache));
            if (cache[s])   return true;
        }
        return false;
    }
    
};
```
