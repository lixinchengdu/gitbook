# 17. Letter Combinations of a Phone Number

* *Difficulty: Medium*

* *Topics: String, Backtracking*

* *Similar Questions:*

  * [Generate Parentheses](./tests/letter-combinations-of-a-phone-number.md)

  * [Combination Sum](./tests/letter-combinations-of-a-phone-number.md)

  * [Binary Watch](./tests/letter-combinations-of-a-phone-number.md)

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
        vector <string> result;
        string path;
        if (digits.length() == 0)   return result;
        helper (digits, 0, path, result);
        return result;
    }
    
    void helper(string& digits, int pos, string& path, vector <string>& result)
    {
        vector <string> num2letter = {" ", "\n", "abc", "def", "ghi", "jkl","mno", "pqrs", "tuv", "wxyz"};
        if (pos == digits.length())
        {
            result.push_back(path);
            return;
        }
        for(char c: num2letter[(digits[pos]-'0')])
        {
            path.append(1,c);
            helper(digits, pos+1, path, result);
            path.pop_back();
        }
        
    }
};
```
