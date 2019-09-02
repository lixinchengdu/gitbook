# 339. Nested List Weight Sum

* *Difficulty: Easy*

* *Topics: Depth-first Search*

* *Similar Questions:*

  * [Nested List Weight Sum II](nested-list-weight-sum-ii.md)

  * [Array Nesting](array-nesting.md)

  * [Employee Importance](employee-importance.md)

## Problem:

<p>Given a nested list of integers, return the sum of all integers in the list weighted by their depth.</p>

<p>Each element is either an integer, or a list -- whose elements may also be integers or other lists.</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,1],2,[1,1]]</span>
<strong>Output: </strong><span id="example-output-1">10 </span>
<strong>Explanation: </strong>Four 1&#39;s at depth 2, one 2 at depth 1.</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,[4,[6]]]</span>
<strong>Output: </strong><span id="example-output-2">27 </span>
<strong>Explanation: </strong>One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.</pre>
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
    int depthSum(vector<NestedInteger>& nestedList) {
        return helper(nestedList, 1);
    }
private:
    int helper(vector<NestedInteger>& nestedList, int depth) {
        int sum = 0;
        for (auto& nestedInt : nestedList) {
            if (nestedInt.isInteger()) {
                sum += depth * nestedInt.getInteger();
            } else {
                sum += helper(nestedInt.getList(), depth + 1);
            }
        }
        
        return sum;
    }
    
};
```
