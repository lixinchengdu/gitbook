# 288. Unique Word Abbreviation

* *Difficulty: Medium*

* *Topics: Hash Table, Design*

* *Similar Questions:*

  * [Two Sum III - Data structure design](two-sum-iii-data-structure-design.md)

  * [Generalized Abbreviation](generalized-abbreviation.md)

## Problem:

<p>An abbreviation of a word follows the form &lt;first letter&gt;&lt;number&gt;&lt;last letter&gt;. Below are some examples of word abbreviations:</p>

<pre>
a) it                      --&gt; it    (no abbreviation)

     1
     &darr;
b) d|o|g                   --&gt; d1g

              1    1  1
     1---5----0----5--8
     &darr;   &darr;    &darr;    &darr;  &darr;    
c) i|nternationalizatio|n  --&gt; i18n

              1
     1---5----0
&nbsp;    &darr;   &darr;    &darr;
d) l|ocalizatio|n          --&gt; l10n
</pre>

<p>Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word&#39;s abbreviation is unique if no <i>other</i> word from the dictionary has the same abbreviation.</p>

<p><strong>Example:</strong></p>

<pre>
Given dictionary = [ &quot;deer&quot;, &quot;door&quot;, &quot;cake&quot;, &quot;card&quot; ]

isUnique(&quot;dear&quot;) -&gt; <code>false</code>
isUnique(&quot;cart&quot;) -&gt; <code>true</code>
isUnique(&quot;cane&quot;) -&gt; <code>false</code>
isUnique(&quot;make&quot;) -&gt; <code>true</code>
</pre>

## Solutions:

```c++
class ValidWordAbbr {
public:
    ValidWordAbbr(vector<string>& dictionary) {
        words.insert(dictionary.begin(), dictionary.end());
        
        for (const auto& word : words) {
            string abbr = toAbbr(word);
            ++wordAbbrFreq[abbr];
        }
    }
    
    bool isUnique(const string& word) {
        if (words.count(word) > 0) {
            return wordAbbrFreq[toAbbr(word)] == 1;
        } else {
            return wordAbbrFreq.find(toAbbr(word)) == wordAbbrFreq.end();
        }
    }
private:
    string toAbbr(const string& str) {
        string abbr;
        abbr.push_back(str[0]);
        if (str.length() > 2) {
            abbr.append(to_string(str.length() - 2));
        }
        if (str.length() > 1) {
            abbr.push_back(str.back());
        }
        
        return abbr;
    }
    
    unordered_set<string> words;
    unordered_map<string, int> wordAbbrFreq;
    
};

/**
 * Your ValidWordAbbr object will be instantiated and called as such:
 * ValidWordAbbr* obj = new ValidWordAbbr(dictionary);
 * bool param_1 = obj->isUnique(word);
 */
```
