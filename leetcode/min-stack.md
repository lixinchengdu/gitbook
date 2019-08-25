# 155. Min Stack

* *Difficulty: Easy*

* *Topics: Stack, Design*

* *Similar Questions:*

  * [Sliding Window Maximum](sliding-window-maximum.md)

  * [Max Stack](max-stack.md)

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
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        if (mins.empty() || mins.top() >= x) {
            mins.push(x);
        }
        stk.push(x);
    }
    
    void pop() {
        int num = stk.top(); stk.pop();
        if (!mins.empty() && num == mins.top()) {
            mins.pop();
        } 
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        if (mins.empty()) {
            return -1;
        }
        return mins.top();
    }
private:
    stack<int> stk;
    stack<int> mins;
    
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```
