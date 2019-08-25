# 294. Flip Game II

* *Difficulty: Medium*

* *Topics: Backtracking, Minimax*

* *Similar Questions:*

  * [Nim Game](nim-game.md)

  * [Flip Game](flip-game.md)

  * [Guess Number Higher or Lower II](guess-number-higher-or-lower-ii.md)

  * [Can I Win](can-i-win.md)

## Problem:

<p>You are playing the following Flip Game with your friend: Given a string that contains only these two characters: <code>+</code> and <code>-</code>, you and your friend take turns to flip two <b>consecutive</b> <code>&quot;++&quot;</code> into <code>&quot;--&quot;</code>. The game ends when a person can no longer make a move and therefore the other person will be the winner.</p>

<p>Write a function to determine if the starting player can guarantee a win.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> <code>s = &quot;++++&quot;</code>
<strong>Output:</strong> true 
<strong>Explanation: </strong>The starting player can guarantee a win by flipping the middle <code>&quot;++&quot;</code> to become <code>&quot;+--+&quot;</code>.
</pre>

<p><b>Follow up:</b><br />
Derive your algorithm&#39;s runtime complexity.</p>
## Solutions:

```c++
class Solution {
public:
    bool canWin(string s) {
        unordered_map<string, bool> cache;
        return helper(s, cache);
    }
    
private:
    bool helper(string& s, unordered_map<string, bool>& cache) {
        if (cache.count(s) > 0) return cache[s];
        for (int i = 0; i < (int)s.length() - 1; ++i) {
            if (s[i] == '+' && s[i+1] == '+') {
                s[i] = '-';
                s[i+1] = '-';
                auto ret =  (!helper(s, cache));
                s[i + 1] = '+';
                s[i] = '+';
                if (ret == true) { // it is wrong to return result intermediately without set s back!
                    cache[s] = ret;
                    return true;
                }
            }
        }
        cache[s] = false;
        return false;
    }
};
```
