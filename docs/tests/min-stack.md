# 155. Min Stack

* *Difficulty: Easy*

* *Topics: Stack, Design*

* *Similar Questions:*

  * [Sliding Window Maximum](./tests/min-stack.md)

  * [Max Stack](./tests/min-stack.md)

## Problem:

<p>Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.</p>

<ul>
	<li>push(x) -- Push element x onto stack.</li>
	<li>pop() -- Removes the element on top of the stack.</li>
	<li>top() -- Get the top element.</li>
	<li>getMin() -- Retrieve the minimum element in the stack.</li>
</ul>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --&gt; Returns -3.
minStack.pop();
minStack.top();      --&gt; Returns 0.
minStack.getMin();   --&gt; Returns -2.
</pre>

<p>&nbsp;</p>

## Solutions:

```c++
class MinStack {
public:
    void push(int x) {
        elements.push(x);
        if (mins.empty()||x<=mins.top())
            mins.push(x);
    }

    void pop() {
        if (elements.empty()) return;
        if (elements.top() == mins.top())
            mins.pop();
        elements.pop();
    }

    int top() {
        return elements.top();
    }

    int getMin() {
        return mins.top();
    }
private:
    stack<int> elements;
    stack<int> mins;
};
```
