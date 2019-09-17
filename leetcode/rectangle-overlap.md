# 866. Rectangle Overlap

* *Difficulty: Easy*

* *Topics: Math*

* *Similar Questions:*

  * [Rectangle Area](rectangle-area.md)

## Problem:

<p>A rectangle is&nbsp;represented as a&nbsp;list <code>[x1, y1, x2, y2]</code>, where&nbsp;<code>(x1, y1)</code>&nbsp;are the coordinates of its bottom-left corner, and <code>(x2,&nbsp;y2)</code>&nbsp;are the coordinates of its top-right corner.</p>

<p>Two rectangles overlap if the area of their intersection is positive.&nbsp; To be clear, two rectangles that only touch at the corner or edges do not overlap.</p>

<p>Given two (axis-aligned) rectangles, return whether&nbsp;they overlap.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>rec1 = [0,0,2,2], rec2 = [1,1,3,3]
<strong>Output: </strong>true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>rec1 = [0,0,1,1], rec2 = [1,0,2,1]
<strong>Output: </strong>false
</pre>

<p><strong>Notes:</strong></p>

<ol>
	<li>Both rectangles <code>rec1</code> and <code>rec2</code> are lists of 4 integers.</li>
	<li>All coordinates in rectangles will be between&nbsp;<code>-10^9 </code>and<code> 10^9</code>.</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        return overlap(rec1[0], rec1[2], rec2[0], rec2[2]) && overlap(rec1[1], rec1[3], rec2[1], rec2[3]);
    }
    
private:
    bool overlap(int left1, int right1, int left2, int right2) {
        return left2 >= left1 && left2 < right1 || left1 >= left2 && left1 < right2;
    }
};
```
