# 716. Max Stack

* *Difficulty: Easy*

* *Topics: Design*

* *Similar Questions:*

  * [Min Stack](min-stack.md)

## Problem:

<p>Design a max stack that supports push, pop, top, peekMax and popMax.</p>

<p>
<ol>
<li>push(x) -- Push element x onto stack.</li>
<li>pop() -- Remove the element on top of the stack and return it.</li>
<li>top() -- Get the element on the top.</li>
<li>peekMax() -- Retrieve the maximum element in the stack.</li>
<li>popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.</li>
</ol>
</p>

<p><b>Example 1:</b><br />
<pre>
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>-1e7 <= x <= 1e7</li>
<li>Number of operations won't exceed 10000.</li>
<li>The last four operations won't be called when stack is empty.</li>
</ol>
</p>
## Solutions:

```c++
class MaxStack {
public:
    /** initialize your data structure here. */
    MaxStack() {
        
    }
    
    void push(int x) {
        data.push(x);
        if (maxs.empty() || x >= maxs.top()) {
            maxs.push(x);
        }
    }
    
    int pop() {
        int val = data.top();
        data.pop();
        if (val == maxs.top()) {
            maxs.pop();
        }
        return val;
    }
    
    int top() {
        return data.top();
    }
    
    int peekMax() {
        return maxs.top();
    }
    
    int popMax() {
        int maxVal = maxs.top();
        stack<int> buffer;
        while (top() != maxVal) buffer.push(pop());
        pop();
        while (!buffer.empty()) {
            push(buffer.top());
            buffer.pop();
        }
        return maxVal;
    }
private:
    stack<int> data;
    stack<int> maxs;
};

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack* obj = new MaxStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->peekMax();
 * int param_5 = obj->popMax();
 */
```
