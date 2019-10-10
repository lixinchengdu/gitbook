# 501. Find Mode in Binary Search Tree

* *Difficulty: Easy*

* *Topics: Tree*

* *Similar Questions:*

  * [Validate Binary Search Tree](validate-binary-search-tree.md)

## Problem:

<p>Given a binary search tree (BST) with duplicates, find all the <a href="https://en.wikipedia.org/wiki/Mode_(statistics)" target="_blank">mode(s)</a> (the most frequently occurred element) in the given BST.</p>

<p>Assume a BST is defined as follows:</p>

<ul>
	<li>The left subtree of a node contains only nodes with keys <b>less than or equal to</b> the node&#39;s key.</li>
	<li>The right subtree of a node contains only nodes with keys <b>greater than or equal to</b> the node&#39;s key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>

<p>For example:<br />
Given BST <code>[1,null,2,2]</code>,</p>

<pre>
   1
    \
     2
    /
   2
</pre>

<p>&nbsp;</p>

<p>return <code>[2]</code>.</p>

<p><b>Note:</b> If a tree has more than one mode, you can return them in any order.</p>

<p><b>Follow up:</b> Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).</p>

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
    vector<int> findMode(TreeNode* root) {
        if (root == nullptr)    return {};
        int count = 0;
        vector<int> ret;
        int lastVal = 0;
        int largest = 0;
        
        helper(root, lastVal, count, ret, largest);
        if (count > largest) {
            ret.clear();
            ret.push_back(lastVal);
        } else if (count == largest) {
            ret.push_back(lastVal);
        }
        
        return ret;
    }
    
private:
    void helper(TreeNode* root, int& lastVal, int& count, vector<int>& ret, int& largest) {
        if (root == nullptr)    return;
        helper(root->left, lastVal, count, ret, largest);
        
        if (root->val == lastVal) {
            ++count;
        } else {
            if (count > 0) {
                if (count > largest) {
                    ret.clear();
                    ret.push_back(lastVal);
                    largest = count;
                } else if (count == largest) {
                    ret.push_back(lastVal);
                }
            }
            count = 1;
        }
        
        lastVal = root->val;
        
        helper(root->right, lastVal, count, ret, largest);
    }
    
};
```
