# 530. Minimum Absolute Difference in BST

* *Difficulty: Easy*

* *Topics: Tree*

* *Similar Questions:*

  * [K-diff Pairs in an Array](k-diff-pairs-in-an-array.md)

## Problem:

<p>Given a binary search tree with non-negative values, find the minimum <a href="https://en.wikipedia.org/wiki/Absolute_difference">absolute difference</a> between values of any two nodes.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b>

   1
    \
     3
    /
   2

<b>Output:</b>
1

<b>Explanation:</b>
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
</pre>

<p>&nbsp;</p>

<p><b>Note:</b> There are at least two nodes in this BST.</p>
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
    int getMinimumDifference(TreeNode* root) {
        vector<int> last;
        int ret = INT_MAX;
        helper(root, last, ret);
        return ret;
    }
    
private:
    void helper(TreeNode* root, vector<int>& last, int& ret) {
        if (root == nullptr)    return;
        helper(root->left, last, ret);
        
        if (last.size() == 0) {
            last.push_back(root->val);
        } else {
            ret = min(ret, abs(last.back() - root->val));
            last.back() = root->val;
        }
        
        helper(root->right, last, ret);
    }
    
};
```
