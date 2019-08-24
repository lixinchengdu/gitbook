# 99. Recover Binary Search Tree

* *Difficulty: Hard*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

## Problem:

<p>Two elements of a binary search tree (BST) are swapped by mistake.</p>

<p>Recover the tree without changing its structure.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [1,3,null,null,2]

&nbsp;  1
&nbsp; /
&nbsp;3
&nbsp; \
&nbsp;  2

<strong>Output:</strong> [3,1,null,null,2]

&nbsp;  3
&nbsp; /
&nbsp;1
&nbsp; \
&nbsp;  2
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [3,1,4,null,null,2]

  3
 / \
1   4
&nbsp;  /
&nbsp; 2

<strong>Output:</strong> [2,1,4,null,null,3]

  2
 / \
1   4
&nbsp;  /
 &nbsp;3
</pre>

<p><strong>Follow up:</strong></p>

<ul>
	<li>A solution using O(<em>n</em>) space is pretty straight forward.</li>
	<li>Could you devise a constant space solution?</li>
</ul>

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
 
 void traverse(TreeNode* root, TreeNode** cur, TreeNode** pre, TreeNode** first, TreeNode **second, bool *isfirst, bool *isfinish);
class Solution {
public:
    void recoverTree(TreeNode* root) {
        TreeNode* first = NULL;
        TreeNode* second = NULL;
        TreeNode* cur = NULL;
        TreeNode* pre = NULL;
        bool isfirst = true;
        bool isfinish = false;
        traverse (root, &cur, &pre, &first, &second, &isfirst, &isfinish);
        cout << first << endl;
        cout << second << endl;
        int temp = (first)->val;
        (first)->val = (second)->val;
        (second)->val = temp;
    }
};

void traverse(TreeNode* root, TreeNode** cur, TreeNode** pre, TreeNode** first, TreeNode **second, bool *isfirst, bool *isfinish)
{
   
    if (!root)  return;
    
    traverse(root->left, cur, pre, first, second, isfirst, isfinish);
    if (*isfinish) return;
   
    *pre = *cur;
    *cur = root;
    
    if (*isfirst)
    {
        if (*pre && (*pre)->val > (*cur)-> val)
        {
            *first = *pre;
            *isfirst = false;
            *second = *cur;
        }
       
        
    }
    
    else
    {
        if (*pre && (*pre)->val > (*cur)-> val)
        {
            *second = *cur;
            *isfinish = true;
        }
    }
    
    traverse(root->right, cur, pre, first, second, isfirst, isfinish);
}
```
