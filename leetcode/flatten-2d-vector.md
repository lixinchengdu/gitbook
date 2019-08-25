# 251. Flatten 2D Vector

* *Difficulty: Medium*

* *Topics: Design*

* *Similar Questions:*

  * [Binary Search Tree Iterator](binary-search-tree-iterator.md)

  * [Zigzag Iterator](zigzag-iterator.md)

  * [Peeking Iterator](peeking-iterator.md)

  * [Flatten Nested List Iterator](flatten-nested-list-iterator.md)

## Problem:

<p>Design and implement an iterator to flatten a 2d vector. It should support the following operations: <code>next</code> and <code>hasNext</code>.</p>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false
</pre>

<p>&nbsp;</p>

<p><strong>Notes:</strong></p>

<ol>
	<li>Please remember to <b>RESET</b> your class variables declared in Vector2D, as static/class variables are <b>persisted across multiple test cases</b>. Please see <a href="https://leetcode.com/faq/" target="_blank">here</a> for more details.</li>
	<li>You may assume that <code>next()</code> call will always be valid, that is, there will be at least a next element in the 2d vector when <code>next()</code> is called.</li>
</ol>

<p>&nbsp;</p>

<p><b>Follow up:</b></p>

<p>As an added challenge, try to code it using only <a href="http://www.cplusplus.com/reference/iterator/iterator/" target="_blank">iterators in C++</a> or <a href="http://docs.oracle.com/javase/7/docs/api/java/util/Iterator.html" target="_blank">iterators in Java</a>.</p>

## Solutions:

```c++
class Vector2D {
public:
    Vector2D(vector<vector<int>>& v) {
        this->v = v;
        i = 0;
        j = 0;
    }
    
    int next() {
        hasNext();
        int val = v[i][j];
        step();
        return val;
    }
    
    bool hasNext() {
        while (i < v.size() && !valid()) { // two conditions!
           step();
        }
        return i < v.size();
    }
    
    bool valid() {
        return i < v.size() && j < v[i].size();
    }
    
    void step() {
        if (++j >= v[i].size()) {
            ++i;
            j = 0;
        }
    }
private:
    vector<vector<int>> v;
    int i;
    int j;
};

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D* obj = new Vector2D(v);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
```
