# 30. Substring with Concatenation of All Words

* *Difficulty: Hard*

* *Topics: Hash Table, Two Pointers, String*

* *Similar Questions:*

  * [Minimum Window Substring](minimum-window-substring.md)

## Problem:

<p>You are given a string, <strong>s</strong>, and a list of words, <strong>words</strong>, that are all of the same length. Find all starting indices of substring(s) in <strong>s</strong> that is a concatenation of each word in <strong>words</strong> exactly once and without any intervening characters.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:
  s =</strong> &quot;barfoothefoobarman&quot;,
<strong>  words = </strong>[&quot;foo&quot;,&quot;bar&quot;]
<strong>Output:</strong> <code>[0,9]</code>
<strong>Explanation:</strong> Substrings starting at index 0 and 9 are &quot;barfoor&quot; and &quot;foobar&quot; respectively.
The output order does not matter, returning [9,0] is fine too.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:
  s =</strong> &quot;wordgoodgoodgoodbestword&quot;,
<strong>  words = </strong>[&quot;word&quot;,&quot;good&quot;,&quot;best&quot;,&quot;word&quot;]
<strong>Output:</strong> <code>[]</code>
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        int n = words.size();
        if (n == 0) return {};
        int wordLen = words[0].length();
        int strLen = s.length();
        if (strLen < wordLen * n)   return {};
        vector<int> ret;
        
        unordered_map<int, vector<int>> hashToIndex;
        for (int i = 0; i < n; ++i) {
            hashToIndex[hash(words[i])].push_back(i);
        }
        
        vector<int> RobinHash(strLen - wordLen + 1, 0);
        
        int runningHash = 0;
        for (int i = 0; i < wordLen - 1; ++i) {
            runningHash = (runningHash * MAGIC + s[i] - 'a') % MOD;
        }
        
        int mostSignificantHash = 1;
        for (int i = 0; i < wordLen - 1; ++i) {
            mostSignificantHash = (mostSignificantHash * MAGIC) % MOD;
        }
        
        for (int i = wordLen - 1; i < strLen; ++i) {
            runningHash = (runningHash * MAGIC + s[i] - 'a') % MOD;
            RobinHash[i - wordLen + 1] = runningHash;
            runningHash = (MOD + runningHash - ((s[i - wordLen + 1] - 'a') * mostSignificantHash % MOD)) % MOD;
        }
        
        for (int i = 0; i < strLen - wordLen * n + 1; ++i) {
            unordered_map<int, int> seen;
            bool stop = false;
            int count = 0;
            for (int j = 0; j < n && !stop; ++j) {
                int h = RobinHash[i + j * wordLen];
                if (hashToIndex.count(h) == 0) {
                    stop = true;
                    break;
                }
                else {
                    ++seen[h];
                    if (seen[h] > hashToIndex[h].size()) {
                        stop = true;
                        break;
                    }
                    ++count; // count is after if
                } 
            }
            if (count == n) {
                ret.push_back(i);
            }
        }
        
        return ret;
    }
    
    int hash(string s) {
        int ret = 0;
        for (auto c : s) {
            ret = (ret * MAGIC + c - 'a') % MOD;
        }
        
        return ret;
    }
    
private:
    int MAGIC = 31;
    int MOD = INT_MAX/MAGIC;
};
```
