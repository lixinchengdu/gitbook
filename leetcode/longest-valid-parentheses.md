# 32. Longest Valid Parentheses

* *Difficulty: Hard*

* *Topics: String, Dynamic Programming*

* *Similar Questions:*

  * [Valid Parentheses](valid-parentheses.md)

## Problem:

<p>Given a string containing just the characters <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>, find the length of the longest valid (well-formed) parentheses substring.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;(()&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest valid parentheses substring is <code>&quot;()&quot;</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;<code>)()())</code>&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest valid parentheses substring is <code>&quot;()()&quot;</code>
</pre>

## Solutions:

```c++
class Solution { //gready method need to consider two scenarios
                // example "(()"
public:
    int longestValidParentheses(string s) {
        string reversed = s;
        reverse(reversed.begin(), reversed.end());
        replace(reversed.begin(), reversed.end(), '(', '=');
        replace(reversed.begin(), reversed.end(), ')', '(');
        replace(reversed.begin(), reversed.end(), '=', ')');
        
    
        return max(longestValidParenthesesHelper(s), longestValidParenthesesHelper(reversed));
    }
    
    int longestValidParenthesesHelper(string s) {
        int ret = 0;
        int balance = 0;
        int left = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '(') {
                ++balance;
            } else {
                --balance;
                if (balance == 0) {
                    ret = max(ret, i - left + 1);
                } else if (balance < 0) {
                    left = i + 1;
                    balance = 0;
                }
            }
        }
        
        return ret;
    }
    
};
```

#### More concise solution

Stack solution from [Huahua](https://zxi.mytechroad.com/blog/stack/leetcode-32-longest-valid-parentheses/)
```c++
// Author: Huahua
class Solution {
public:
  int longestValidParentheses(string s) {
    stack<int> q;
    int start = 0;
    int ans = 0;
    for (int i = 0;i < s.length(); i++) {
      if(s[i] == '(') {
        q.push(i);
      } else {
        if (q.empty()) {
          start = i + 1;
        } else {
          int index = q.top(); q.pop();
          ans = max(ans, q.empty() ? i - start + 1 : i - q.top());          
        }
      }
    }
    return ans;
  }
};
```

DP solution from [Xishuashua](http://bangbingsyb.blogspot.com/2014/11/leetcode-longest-valid-parentheses.html)

```c++
class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.size(), maxLen = 0;
        vector<int> dp(n+1,0);
        for(int i=1; i<=n; i++) {
            int j = i-2-dp[i-1];
            if(s[i-1]=='(' || j<0 || s[j]==')') 
                dp[i] = 0;
            else {
                dp[i] = dp[i-1]+2+dp[j];
                maxLen = max(maxLen, dp[i]);
            }
        }
        return maxLen;
    }
};
```
