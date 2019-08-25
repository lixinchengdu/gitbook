# 95. Unique Binary Search Trees II

* *Difficulty: Medium*

* *Topics: Dynamic Programming, Tree*

* *Similar Questions:*

  * [Unique Binary Search Trees](unique-binary-search-trees.md)

  * [Different Ways to Add Parentheses](different-ways-to-add-parentheses.md)

## Problem:

<p>Given an integer <em>n</em>, generate all structurally unique <strong>BST&#39;s</strong> (binary search trees) that store values 1 ...&nbsp;<em>n</em>.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 3
<strong>Output:</strong>
[
&nbsp; [1,null,3,2],
&nbsp; [3,2,null,1],
&nbsp; [3,1,null,null,2],
&nbsp; [2,1,3],
&nbsp; [1,null,2,null,3]
]
<strong>Explanation:</strong>
The above output corresponds to the 5 unique BST&#39;s shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
</pre>

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
    vector<TreeNode*> generateTrees(int n) {
        if (n <= 0) return {};
        map<pair<int, int>, vector<TreeNode*>> cache;
        return helper(1, n, cache);
    }
    
    vector<TreeNode*> helper(int left, int right, map<pair<int, int>, vector<TreeNode*>>& cache) {
        if (left > right)   return {nullptr};
        if (left == right)  return {new TreeNode(left)};
        
        auto range = make_pair(left, right);
        if (cache.count(range) > 0) return cache[range];
        
        vector<TreeNode*> ret;
        
        for (int rootVal = left; rootVal <= right; ++rootVal) {
            vector<TreeNode*> leftRoots = helper(left, rootVal - 1, cache);
            vector<TreeNode*> rightRoots = helper(rootVal + 1, right, cache);
            
            for (auto leftRoot : leftRoots) {
                for (auto rightRoot : rightRoots) {
                    TreeNode* root = new TreeNode(rootVal);
                    root->left = leftRoot;
                    root->right = rightRoot;
                    ret.push_back(root);
                }
            }
            
        }
        
        cache[range] = ret;
        return ret;
    }
};
```
