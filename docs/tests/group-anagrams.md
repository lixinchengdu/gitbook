# 49. Group Anagrams

* *Difficulty: Medium*

* *Topics: Hash Table, String*

* *Similar Questions:*

  * [Valid Anagram](./tests/group-anagrams.md)

  * [Group Shifted Strings](./tests/group-anagrams.md)

## Problem:

<p>Given an array of strings, group anagrams together.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> <code>[&quot;eat&quot;, &quot;tea&quot;, &quot;tan&quot;, &quot;ate&quot;, &quot;nat&quot;, &quot;bat&quot;]</code>,
<strong>Output:</strong>
[
  [&quot;ate&quot;,&quot;eat&quot;,&quot;tea&quot;],
  [&quot;nat&quot;,&quot;tan&quot;],
  [&quot;bat&quot;]
]</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>All inputs will be in lowercase.</li>
	<li>The order of your output does not&nbsp;matter.</li>
</ul>

## Solutions:

```c++
class Solution {
    
public:

    class Freq
    {
        public:
        int alphafreq[26];
       // bool operator == (const Freq& another) const
       // {
       //     for (int i = 0; i< 26; i++)
      //      {
       //         if (this -> alphafreq[i] != another.alphafreq[i])   return false;
       //     }
      //      return true;
      //  }
        
        bool operator < (const Freq& another) const
        {
            for (int i = 0; i < 26; i++)
            {
               // cout << alphafreq[i] << " " << another.alphafreq[i] << endl;
                if (this -> alphafreq[i] < another.alphafreq[i])    return true;
                if (this -> alphafreq[i] > another.alphafreq[i])    return false;
            }
            return false;
        }
        
        Freq(string word)
        {
            for (int i = 0; i < 26 ;i++) alphafreq[i] = 0;
            for (auto c: word)
            {
                alphafreq[c-'a'] ++;
            }
        }
        
        
    };
    
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map <Freq, vector<string>> mapResult;
        vector < vector <string>> result;
        for (auto word: strs)
        {
            Freq f(word);
            mapResult[f].push_back(word); 
        }
        
        for (auto wordVector: mapResult)
        {
            result.push_back(wordVector.second);
        }
        return result;
        
    }
    
    int getHash(string word, int mod)
    {
        int product = 1;
        for (auto c: word)
        {
            product *= (c + 137);
           // product %= mod;
        }
        cout << word << product << endl;
        return product;
    }
    
    
    
};
```
