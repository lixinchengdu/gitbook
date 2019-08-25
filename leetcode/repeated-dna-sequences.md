# 187. Repeated DNA Sequences

* *Difficulty: Medium*

* *Topics: Hash Table, Bit Manipulation*

* *Similar Questions:*

## Problem:

<p>All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: &quot;ACGAATTCCG&quot;. When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.</p>

<p>Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT&quot;

<strong>Output:</strong> [&quot;AAAAACCCCC&quot;, &quot;CCCCCAAAAA&quot;]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        if (s.length() < 10)    return {};
        int code = 0;
        for (int i = 0; i < 9; ++i) {
            updateCode(code, s[i]);
        }
        
        unordered_map<int, int> merCount;
        vector<string> ret;
        
        for (int i = 9; i < s.length(); ++i) {
            updateCode(code, s[i]);
            if (++merCount[code] == 2) {
                ret.push_back(s.substr(i - 9, 10));
            }
        }
        
        return ret;
        
    }
    
    void updateCode(int& code, char c) {
        const int mask = 0xFFFFF;
        code = ((code << 2) & mask);
        switch(c) {
            case 'A':
                // no-op
                break;
            case 'C':
                code = code | 0x1;
                break;
            case 'G':
                code = code | 0x2;
                break;
            case 'T':
                code = code | 0x3;
                break;
            default:
                throw "Illegal input";
        }
    }
};
```
