# 301. Remove Invalid Parentheses

* *Difficulty: Hard*

* *Topics: Depth-first Search, Breadth-first Search*

* *Similar Questions:*

  * [Valid Parentheses](./tests/remove-invalid-parentheses.md)

## Problem:

<p>Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.</p>

<p><strong>Note:</strong>&nbsp;The input string may contain letters other than the parentheses <code>(</code> and <code>)</code>.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> &quot;()())()&quot;
<b>Output:</b> [&quot;()()()&quot;, &quot;(())()&quot;]
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> &quot;(a)())()&quot;
<b>Output:</b> [&quot;(a)()()&quot;, &quot;(a())()&quot;]
</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> &quot;)(&quot;
<b>Output: </b>[&quot;&quot;]
</pre>
## Solutions:

```c++
class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        int left = 0;
        int right = 0;
        for (char c : s)
        {
            if (c == '(')   left++;
            else if (c == ')')
            {
                if (left == 0)  right ++;
                else left--;
            }
        }
      //  cout << left << right << endl;
        set <string> result;
        helper (s, 0, "", result, left, right, 0);
        return vector <string> (result.begin(), result.end());
    }
    
    void helper (string& s, int pos, string path, set<string>& result, int left, int right, int leftpar)
    {
      //   cout << pos << endl;
      //  cout << path << endl;
      //  cout << left << " " << right << " " << leftpar << endl;
        if (leftpar < 0)    return;
        if (left == 0 && right == 0 && leftpar == 0 && pos == s.length())    
        {
            result.insert(path);
            return;
        }
        if (left < 0 || right < 0)  return;
        if (pos == s.length())  return;
        if (s[pos] == '(')
        {
            helper(s, pos+1, path, result, left -1, right, leftpar);
            helper(s, pos+1, path + "(", result, left, right, leftpar+1);
        }
        else if (s[pos] == ')')
        {
            helper(s, pos+1, path, result, left, right -1, leftpar);
            helper(s, pos+1, path + ")", result, left, right, leftpar-1);
        }
        else
        {
            helper(s, pos+1, path + string(1,s[pos]), result, left, right, leftpar);
        }
    }
    
};
```
