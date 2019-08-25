# 385. Mini Parser

* *Difficulty: Medium*

* *Topics: String, Stack*

* *Similar Questions:*

  * [Flatten Nested List Iterator](flatten-nested-list-iterator.md)

  * [Ternary Expression Parser](ternary-expression-parser.md)

  * [Remove Comments](remove-comments.md)

## Problem:

<p>Given a nested list of integers represented as a string, implement a parser to deserialize it.</p>

<p>Each element is either an integer, or a list -- whose elements may also be integers or other lists.</p>

<p><b>Note:</b>
You may assume that the string is well-formed:
<ul>
<li>String is non-empty.</li>
<li>String does not contain white spaces.</li>
<li>String contains only digits <code>0-9</code>, <code>[</code>, <code>-</code> <code>,</code>, <code>]</code>.</li>
</ul>
</p>

<p><b>Example 1:</b>
<pre>
Given s = "324",

You should return a NestedInteger object which contains a single integer 324.
</pre>
</p>

<p><b>Example 2:</b>
<pre>
Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
</pre>
</p>
## Solutions:

```c++
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    NestedInteger deserialize(string s) {
        int pos = 0;
        return helper(s, pos);
    }
    
    NestedInteger base(string&s, int& pos) {
        int sign = 1;
        if (s[pos] == '-') {
            sign = -1;
            ++pos;
        }
        int val = s[pos] - '0';
        while (pos + 1 < s.length() && isdigit(s[pos + 1])) {
            ++pos;
            val = 10 * val + (s[pos] - '0');    
        }
        return NestedInteger(val * sign);
    }

    NestedInteger helper(string& s, int& pos) {
        NestedInteger nestedInteger;
        if (pos == s.length())  return NestedInteger();
        if (s[pos] == ']')  return NestedInteger();
        
        NestedInteger temp;
        for (; pos < s.length(); ++pos) {
            char c = s[pos];
            if (isdigit(c) || c == '-') {
                temp = base(s, pos);
                continue;
            }
            if (c == ',') {
                nestedInteger.add(temp);
                continue;
            }

            if (c == ']') {
                nestedInteger.add(temp);
                return nestedInteger;
            }
            
            if (c == '[') {
                temp = helper(s, ++pos);
                continue;
            }
        }
    
        return temp;
    }
};
```
