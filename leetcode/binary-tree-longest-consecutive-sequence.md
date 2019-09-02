# 298. Binary Tree Longest Consecutive Sequence

* *Difficulty: Medium*

* *Topics: Tree*

* *Similar Questions:*

  * [Longest Consecutive Sequence](longest-consecutive-sequence.md)

  * [Binary Tree Longest Consecutive Sequence II](binary-tree-longest-consecutive-sequence-ii.md)

## Problem:

<p>Given a binary tree, find the length of the longest consecutive sequence path.</p>

<p>The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>

   1
    \
     3
    / \
   2   4
        \
         5

<strong>Output:</strong> <code>3</code>

<strong>Explanation: </strong>Longest consecutive sequence path is <code>3-4-5</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">, so return </span><code>3</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">.</span></pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:

</strong>   2
    \
     3
    / 
   2    
  / 
 1

<strong>Output: 2 

Explanation: </strong>Longest consecutive sequence path is <code>2-3</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">, not </span><code>3-2-1</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">, so return </span><code>2</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">.</span></pre>
## Solutions:

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int longestConsecutive(TreeNode* root) {
        if (root == nullptr)    return 0;
        int consecutiveLen = 1;
        return helper(root, consecutiveLen);
    }
private:
    int helper(TreeNode* root, int& consecutiveLen) {
        int ret = 0;
        if (root->left) {
            int leftConsecutive = 1;
            ret = max(ret, helper(root->left, leftConsecutive));
            if (root->val + 1 == root->left->val) {
                consecutiveLen = max(consecutiveLen, 1 + leftConsecutive);
            }
        }
        
        if (root->right) {
            int rightConsecutive = 1;
            ret = max(ret, helper(root->right, rightConsecutive));
            if (root->val + 1 == root->right->val) {
                consecutiveLen = max(consecutiveLen, 1 + rightConsecutive);
            }
        }
        
        ret = max(ret, consecutiveLen);
        
        return ret;
    }
    
};
```
