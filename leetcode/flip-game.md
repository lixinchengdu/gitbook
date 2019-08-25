# 293. Flip Game

* *Difficulty: Easy*

* *Topics: String*

* *Similar Questions:*

  * [Flip Game II](flip-game-ii.md)

## Problem:

<p>You are playing the following Flip Game with your friend: Given a string that contains only these two characters: <code>+</code> and <code>-</code>, you and your friend take turns to flip two <b>consecutive</b> <code>&quot;++&quot;</code> into <code>&quot;--&quot;</code>. The game ends when a person can no longer make a move and therefore the other person will be the winner.</p>

<p>Write a function to compute all possible states of the string after one valid move.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> <code>s = &quot;++++&quot;</code>
<strong>Output:</strong> 
[
  &quot;--++&quot;,
  &quot;+--+&quot;,
  &quot;++--&quot;
]
</pre>

<p><strong>Note: </strong>If there is no valid move, return an empty list <code>[]</code>.</p>

## Solutions:

```c++
class Solution {
public:
    vector<string> generatePossibleNextMoves(string s) {
        vector<string> ret;
        for (int i = 0; i < int(s.length() - 1) ; ++i) { // caution!!!!
            if (s[i] == '+' && s[i + 1] == '+') {
                s[i] = '-';
                s[i + 1] = '-';
                ret.push_back(s);
                s[i + 1] = '+';
                s[i] = '+';
            }
        }
        
        return ret;
    }
};
```
