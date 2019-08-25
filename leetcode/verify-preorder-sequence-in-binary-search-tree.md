# 255. Verify Preorder Sequence in Binary Search Tree

* *Difficulty: Medium*

* *Topics: Stack, Tree*

* *Similar Questions:*

  * [Binary Tree Preorder Traversal](binary-tree-preorder-traversal.md)

## Problem:

<p>Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.</p>

<p>You may assume each number in the sequence is unique.</p>

<p>Consider the following&nbsp;binary search tree:&nbsp;</p>

<pre>
     5
    / \
   2   6
  / \
 1   3</pre>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [5,2,6,1,3]
<strong>Output:</strong> false</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [5,2,1,3,6]
<strong>Output:</strong> true</pre>

<p><b>Follow up:</b><br />
Could you do it using only constant space complexity?</p>

## Solutions:

```c++
class Solution {
public:
    bool verifyPreorder(vector<int>& preorder) {
        stack<int> stk;
        int lowerBound = INT_MIN;
        for (auto num : preorder) {
            if (num <= lowerBound)  return false;
            if (!stk.empty() && stk.top() == num)   return false;
            while (!stk.empty() && stk.top() < num) {
                lowerBound = stk.top();
                //cout << lowerBound << " " << num << endl;
                stk.pop();
            }
            stk.push(num);
        }
        return true;
    }
};
```
