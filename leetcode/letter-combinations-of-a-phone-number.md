# 17. Letter Combinations of a Phone Number

* *Difficulty: Medium*

* *Topics: String, Backtracking*

* *Similar Questions:*

  * [Generate Parentheses](generate-parentheses.md)

  * [Combination Sum](combination-sum.md)

  * [Binary Watch](binary-watch.md)

## Problem:

<p>Given a string containing digits from <code>2-9</code> inclusive, return all possible letter combinations that the number could represent.</p>

<p>A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.</p>

<p><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png" /></p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input: </strong>&quot;23&quot;
<strong>Output:</strong> [&quot;ad&quot;, &quot;ae&quot;, &quot;af&quot;, &quot;bd&quot;, &quot;be&quot;, &quot;bf&quot;, &quot;cd&quot;, &quot;ce&quot;, &quot;cf&quot;].
</pre>

<p><strong>Note:</strong></p>

<p>Although the above answer is in lexicographical order, your answer could be in any order you want.</p>

## Solutions:

```c++
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> ret;
        if (digits.length() == 0)   return ret;
        int pos = 0;
        string path;
        dfs(digits, pos, path, ret);
        return ret;
    }
    
    void dfs(string digits, int pos, string& path, vector<string>& ret) {
        if (pos == digits.length()) {
            ret.push_back(path);
            return;
        }
        
        char digit = digits[pos];
        for (auto c : numToLetters[digit]) {
            path.push_back(c);
            dfs(digits, pos + 1, path, ret);
            path.pop_back();
        }
    }
    
private:
    unordered_map<char, string> numToLetters {
            {'2', "abc"}, 
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
};
```
