# 500. Keyboard Row

* *Difficulty: Easy*

* *Topics: Hash Table*

* *Similar Questions:*

## Problem:

<p>Given a List of words, return the words that can be typed using letters of <b>alphabet</b> on only one row&#39;s of American keyboard like the image below.</p>

<p>&nbsp;</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2018/10/12/keyboard.png" style="width: 100%; max-width: 600px" /></p>
&nbsp;

<p><b>Example:</b></p>

<pre>
<b>Input:</b> [&quot;Hello&quot;, &quot;Alaska&quot;, &quot;Dad&quot;, &quot;Peace&quot;]
<b>Output:</b> [&quot;Alaska&quot;, &quot;Dad&quot;]
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>You may use one character in the keyboard more than once.</li>
	<li>You may assume the input string will only contain letters of alphabet.</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        vector<string> ret;
        for (auto& word : words) {
            if (sameRow(word)) {
                ret.push_back(word);
            }
        }
        
        return ret;
    }
    
private:
    bool sameRow(const string& str) {
        if (str.length() == 0)  return true;
        char c = tolower(str[0]);
        int row = -1;
        for (int i = 0; i < 3; ++i) {
            if (board[i].find(c) != string::npos) {
                row = i;
                break;
            }
        }
        
        for (int i = 1; i < str.length(); ++i) {
            if (board[row].find(tolower(str[i])) == string::npos)   return false;
        }
        
        return true;
    }
    
    vector<string> board = {
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"
    };
};
```
