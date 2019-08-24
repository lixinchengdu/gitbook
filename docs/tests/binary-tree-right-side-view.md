# 199. Binary Tree Right Side View

* *Difficulty: Medium*

* *Topics: Tree, Depth-first Search, Breadth-first Search*

* *Similar Questions:*

  * [Populating Next Right Pointers in Each Node](./tests/binary-tree-right-side-view.md)

  * [Boundary of Binary Tree](./tests/binary-tree-right-side-view.md)

## Problem:

<p>Given a binary tree, imagine yourself standing on the <em>right</em> side of it, return the values of the nodes you can see ordered from top to bottom.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;[1,2,3,null,5,null,4]
<strong>Output:</strong>&nbsp;[1, 3, 4]
<strong>Explanation:
</strong>
   1            &lt;---
 /   \
2     3         &lt;---
 \     \
  5     4       &lt;---
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
    vector<int> rightSideView(TreeNode* root) {
        vector <int> right; 
        list < pair<TreeNode*, int> > nodeList;
        pair <TreeNode*, int> initial_pair(root, 0);
        nodeList.push_back(initial_pair);
        while (!nodeList.empty())
        {
            
            if (!nodeList.front().first)    
            {
                nodeList.pop_front();
                continue;
            }
            nodeList.push_back(pair <TreeNode*, int> (nodeList.front().first->left,nodeList.front().second+1));
            nodeList.push_back(pair <TreeNode*, int> (nodeList.front().first->right,nodeList.front().second+1));
            
            if (nodeList.front().second + 1> right.size())
            {
                right.push_back(-1);
                
            }
            
            right[nodeList.front().second] = nodeList.front().first->val;
            cout << nodeList.empty() << endl;
            nodeList.pop_front();
            cout << nodeList.empty() << endl;
        }
        return right;
        
    }
};
```
