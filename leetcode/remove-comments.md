# 722. Remove Comments

* *Difficulty: Medium*

* *Topics: String*

* *Similar Questions:*

  * [Mini Parser](mini-parser.md)

  * [Ternary Expression Parser](ternary-expression-parser.md)

## Problem:

<p>Given a C++ program, remove comments from it. The program <code>source</code> is an array where <code>source[i]</code> is the <code>i</code>-th line of the source code.  This represents the result of splitting the original source code string by the newline character <code>\n</code>.</p>

<p>In C++, there are two types of comments, line comments, and block comments.</p>
<p>
The string <code>//</code> denotes a line comment, which represents that it and rest of the characters to the right of it in the same line should be ignored.
</p><p>
The string <code>/*</code> denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of <code>*/</code> should be ignored.  (Here, occurrences happen in reading order: line by line from left to right.)  To be clear, the string <code>/*/</code> does not yet end the block comment, as the ending would be overlapping the beginning.
</p><p>
The first effective comment takes precedence over others: if the string <code>//</code> occurs in a block comment, it is ignored. Similarly, if the string <code>/*</code> occurs in a line or block comment, it is also ignored.
</p><p>
If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.
</p><p>
There will be no control characters, single quote, or double quote characters.  For example, <code>source = "string s = "/* Not a comment. */";"</code> will not be a test case.  (Also, nothing else such as defines or macros will interfere with the comments.)
</p><p>
It is guaranteed that every open block comment will eventually be closed, so <code>/*</code> outside of a line or block comment always starts a new comment.
</p><p>
Finally, implicit newline characters can be deleted by block comments.  Please see the examples below for details.
</p>

<p>After removing the comments from the source code, return the source code in the same format.</p>

<p><b>Example 1:</b><br />
<pre style="white-space: pre-wrap">
<b>Input:</b> 
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]

The line by line code is visualized as below:
/*Test program */
int main()
{ 
  // variable declaration 
int a, b, c;
/* This is a test
   multiline  
   comment for 
   testing */
a = b + c;
}

<b>Output:</b> ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

The line by line code is visualized as below:
int main()
{ 
  
int a, b, c;
a = b + c;
}

<b>Explanation:</b> 
The string <code>/*</code> denotes a block comment, including line 1 and lines 6-9. The string <code>//</code> denotes line 4 as comments.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre style="white-space: pre-wrap">
<b>Input:</b> 
source = ["a/*comment", "line", "more_comment*/b"]
<b>Output:</b> ["ab"]
<b>Explanation:</b> The original source string is "a/*comment<b>\n</b>line<b>\n</b>more_comment*/b", where we have bolded the newline characters.  After deletion, the <i>implicit</i> newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].
</pre>
</p>

<p><b>Note:</b>
<li>The length of <code>source</code> is in the range <code>[1, 100]</code>.</li>
<li>The length of <code>source[i]</code> is in the range <code>[0, 80]</code>.</li>
<li>Every open block comment is eventually closed.</li>
<li>There are no single-quote, double-quote, or control characters in the source code.</li>
</p>
## Solutions:

```c++
class Solution {
public:
    vector<string> removeComments(vector<string>& source) {
        queue<char> buffer;
        bool inContext = false;
        vector<string> ret;
        
        for (auto& line : source) {
            auto processed = processLine(buffer, line, inContext);
            addLine(buffer, processed, ret);
        }
        
        return ret;
    }

private:
    string processLine(queue<char>& buffer, string& line, bool& inContext) {
        string ret;
        for (int i = 0; i < line.length();) {
            if (line[i] != '/' && line[i] != '*') {
               if (!inContext) {
                   ret.push_back(line[i]);
               }
               ++i;
               continue;
            }
            
            if (line[i] == '/') {
                if (!inContext) { // not in context
                    if (i + 1 < line.length() && line[i + 1] == '/') {
                        break;
                    }
                    else if (i + 1 < line.length() && line[i + 1] == '*') {
                        inContext = true;
                        i = i + 2;
                    }
                    else {
                        ret.push_back('/');
                        ++i;
                    }
                } else { // in context
                    ++i;
                }
            } else {
                if (!inContext) {
                    ret.push_back('*');
                    ++i;
                } else {
                    if (i + 1 < line.length() && line[i + 1] == '/') {
                        inContext = false;
                        i = i + 2;
                    } else {
                        ++i;
                    }
                }
            }
        }
        
        if (!inContext && (!buffer.empty() || ret.length() != 0)) { // CAUTION! buffer.empty() should also be checked!
            ret.push_back('\n');
        }
        return ret;
    }
    
    void addLine(queue<char>& buffer, string& line, vector<string>& ret) {
        for (auto c : line) {
            if (c != '\n') {
                buffer.push(c);
            } else {
                string str;
                while (!buffer.empty()) {
                    str.push_back(buffer.front()); buffer.pop();
                }
                ret.push_back(str);
            }
        }
    }
    
};
```
