# 772. Construct Quad Tree

* *Difficulty: Medium*

* *Topics: *

* *Similar Questions:*

## Problem:

<p>We want to use quad trees to store an <code>N x N</code> boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes <strong>until the values in the region it represents are all the same</strong>.</p>

<p>Each node has another two boolean attributes : <code>isLeaf</code> and <code>val</code>. <code>isLeaf</code> is true if and only if the node is a leaf node. The <code>val</code> attribute for a leaf node contains the value of the region it represents.</p>

<p>Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:</p>

<p>Given the <code>8 x 8</code> grid below, we want to construct the corresponding quad tree:</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_grid.png" style="height:27%; max-height:300px; max-width:299px; width:27%" /></p>

<p>It can be divided according to the definition above:</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_grid_divided.png" style="height:100%; max-height:300px; max-width:1107px; width:100%" /></p>

<p>&nbsp;</p>

<p>The corresponding quad tree should be as following, where each node is represented as a <code>(isLeaf, val)</code> pair.</p>

<p>For the non-leaf&nbsp;nodes,&nbsp;<code>val</code> can be arbitrary, so it is represented as <code>*</code>.</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_quad_tree.png" style="height:100%; max-height:300px; max-width:836px; width:100%" /></p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>N</code> is less than <code>1000</code> and guaranteened to be a power of 2.</li>
	<li>If you want to know more about the quad tree, you can refer to its <a href="https://en.wikipedia.org/wiki/Quadtree">wiki</a>.</li>
</ol>

## Solutions:

```c++
/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;

    Node() {}

    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/
class Solution {
public:
    Node* construct(vector<vector<int>>& grid) {
        if (grid.size() == 0)   return new Node();
        return helper(grid, 0, 0, grid.size());
    }
    
private:
    Node* helper(vector<vector<int>>& grid, int row, int col, int len) {
        // base case
        if (len == 1) {
            Node* node = new Node();
            node->val = (grid[row][col] == 1);
            node->isLeaf = true;
            node->topLeft = nullptr;
            node->topRight = nullptr;
            node->bottomLeft = nullptr;
            node->bottomRight = nullptr;
            return node;
        }
        
        Node* upperLeft = helper(grid, row, col, len / 2);
        Node* upperRight = helper(grid, row, col + len /2, len / 2);
        Node* bottomLeft = helper(grid, row + len / 2, col, len / 2);
        Node* bottomRight = helper(grid, row + len / 2, col + len / 2, len / 2);
        
        if (upperLeft->isLeaf && upperRight->isLeaf && bottomLeft->isLeaf && bottomRight->isLeaf && upperLeft->val == upperRight->val && upperLeft->val == bottomLeft->val && upperLeft->val == bottomRight->val) {
            Node* node = new Node();
            node->val = upperLeft->val;
            node->isLeaf = true;
            node->topLeft = nullptr;
            node->topRight = nullptr;
            node->bottomLeft = nullptr;
            node->bottomRight = nullptr;
            return node;
        } else {
            return new Node(false, false, upperLeft, upperRight, bottomLeft, bottomRight);
        }
        
    }
    
};
```
