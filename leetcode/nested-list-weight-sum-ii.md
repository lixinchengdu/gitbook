# 364. Nested List Weight Sum II

* *Difficulty: Medium*

* *Topics: Depth-first Search*

* *Similar Questions:*

  * [Nested List Weight Sum](nested-list-weight-sum.md)

  * [Array Nesting](array-nesting.md)

## Problem:

<p>Given a nested list of integers, return the sum of all integers in the list weighted by their depth.</p>

<p>Each element is either an integer, or a list -- whose elements may also be integers or other lists.</p>

<p>Different from the <a href="https://leetcode.com/problems/nested-list-weight-sum/">previous question</a> where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,1],2,[1,1]]</span>
<strong>Output: </strong><span id="example-output-1">8 
<strong>Explanation: </strong>F</span>our 1&#39;s at depth 1, one 2 at depth 2.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,[4,[6]]]</span>
<strong>Output: </strong><span id="example-output-2">17 
<strong>Explanation:</strong> O</span>ne 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.
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
    int depthSumInverse(vector<NestedInteger>& nestedList) {
        int depth = getDepth(nestedList);
        return helper(nestedList, depth);
    }
    
private:
    int getDepth(vector<NestedInteger>& nestedList) {
        int depth = 0;
        for (auto& nestedInt : nestedList) {
            if (nestedInt.isInteger()) {
                depth = max(depth, 1);
            } else {
                depth = max(depth, 1 + getDepth(nestedInt.getList()));
            }
        }
        
        return depth;
    }
    
    int helper(vector<NestedInteger>& nestedList, int depth) {
        int sum = 0;
        for (auto& nestedInt : nestedList) {
            if (nestedInt.isInteger()) {
                sum += depth * nestedInt.getInteger();
            } else {
                sum += helper(nestedInt.getList(), depth - 1);
            }
        }
        
        return sum;
    }
};
```
