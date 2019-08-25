# 346. Moving Average from Data Stream

* *Difficulty: Easy*

* *Topics: Design, Queue*

* *Similar Questions:*

## Problem:

<p>Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.</p>

<p><strong>Example:</strong></p>

<pre>
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
</pre>

<p>&nbsp;</p>

## Solutions:

```c++
class MovingAverage {
public:
    /** Initialize your data structure here. */
    MovingAverage(int size) {
        capacity = size;
    }
    
    double next(int val) {
        nums.push(val);
        sum += val;
        if (nums.size() > capacity) {
            sum -= nums.front(); nums.pop(); 
        }
        
        return (double) sum / nums.size();
    }
private:
    int sum = 0;
    queue<int> nums;
    int capacity;
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */
```
