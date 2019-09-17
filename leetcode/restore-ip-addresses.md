# 93. Restore IP Addresses

* *Difficulty: Medium*

* *Topics: String, Backtracking*

* *Similar Questions:*

  * [IP to CIDR](ip-to-cidr.md)

## Problem:

<p>Given a string containing only digits, restore it by returning all possible valid IP address combinations.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> &quot;25525511135&quot;
<strong>Output:</strong> <code>[&quot;255.255.11.135&quot;, &quot;255.255.111.35&quot;]
</code></pre>

## Solutions:

```c++
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> path;
        vector<string> ret;
        helper(s, 0, path, ret);
        return ret;
    }
private:
    void helper(const string& s, int pos, vector<string>& path, vector<string>& ret) {
        // for (auto str : path) {
        //     cout << str << " ";
        // }
        // cout << "end" << endl;
        
        
        // base case;
        if (path.size() > 4)    return;
        if (pos == s.length()) {
            if (path.size() != 4)   return;
            ret.push_back(prettyPrint(path));
            //return;
        }
        
        
        for (int len = 1; len <= 3 && pos + len <= s.length(); ++len) {
            
            if (len != 1 && s[pos] == '0')  return;
            int num = 0;
            for (int j = 0; j < len ;++j) {
                num = 10 * num + (s[pos + j] - '0');
            }
            
            //cout << num << endl;
            if (num > 255)  return;
            path.push_back(s.substr(pos, len));
            helper(s, pos + len, path, ret);
            path.pop_back();
        }
        
    }
    
    string prettyPrint(vector<string>& path) {
        string ret;
        for (auto& seg : path) {
            ret.append(seg);
            ret.push_back('.');
        }
        
        ret.pop_back();
        return ret;
    }
    
};
```
