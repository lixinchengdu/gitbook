# 341. Flatten Nested List Iterator

* *Difficulty: Medium*

* *Topics: Stack, Design*

* *Similar Questions:*

  * [Flatten 2D Vector](flatten-2d-vector.md)

  * [Zigzag Iterator](zigzag-iterator.md)

  * [Mini Parser](mini-parser.md)

  * [Array Nesting](array-nesting.md)

## Problem:

<p>Given a nested list of integers, implement an iterator to flatten it.</p>

<p>Each element is either an integer, or a list -- whose elements may also be integers or other lists.</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,1],2,[1,1]]</span>
<strong>Output: </strong><span id="example-output-1">[1,1,2,1,1]
</span><strong>Explanation: </strong>By calling <i>next</i> repeatedly until <i>hasNext</i> returns false, 
&nbsp;            the order of elements returned by <i>next</i> should be: <code>[1,1,2,1,1]</code>.</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,[4,[6]]]</span>
<strong>Output: </strong><span id="example-output-2">[1,4,6]
</span><strong>Explanation: </strong>By calling <i>next</i> repeatedly until <i>hasNext</i> returns false, 
&nbsp;            the order of elements returned by <i>next</i> should be: <code>[1,4,6]</code>.
</pre>
</div>
</div>

## Solutions:

```c++
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        for (int i = 0; i < nestedList.size(); ++i) {
            stk.push(nestedList[nestedList.size() - 1 - i]);
        }
    }

    int next() {
        int val = stk.top().getInteger();
        stk.pop();
        return val;
    }

    bool hasNext() {
        while (!stk.empty()) {
            if (stk.top().isInteger()) {
                return true;
            } else {
                auto nestedList = stk.top().getList(); stk.pop();
                for (int i = 0; i < nestedList.size(); ++i) {
                    stk.push(nestedList[nestedList.size() - 1 - i]);
                }
            }
        }
        return false;
    }
    
private:
    stack<NestedInteger> stk;
    int buffer;
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
```
