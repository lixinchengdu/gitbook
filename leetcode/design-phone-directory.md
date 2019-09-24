# 379. Design Phone Directory

* *Difficulty: Medium*

* *Topics: Linked List, Design*

* *Similar Questions:*

## Problem:

<p>Design a Phone Directory which supports the following operations:</p>

<p>
<ol>
<li><code>get</code>: Provide a number which is not assigned to anyone.</li>
<li><code>check</code>: Check if a number is available or not.</li>
<li><code>release</code>: Recycle or release a number.</li>
</ol>
</p>

<p><b>Example:</b>
<pre>
// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// It can return any available phone number. Here we assume it returns 0.
directory.get();

// Assume it returns 1.
directory.get();

// The number 2 is available, so return true.
directory.check(2);

// It returns 2, the only number that is left.
directory.get();

// The number 2 is no longer available, so return false.
directory.check(2);

// Release number 2 back to the pool.
directory.release(2);

// Number 2 is available again, return true.
directory.check(2);
</pre>
</p>
## Solutions:

```c++
class PhoneDirectory {
public:
    /** Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    PhoneDirectory(int maxNumbers) {
        for (int i = 0; i < maxNumbers; ++i) {
            phones.insert(i);
        }
    }
    
    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    int get() {
        auto it = phones.begin(); // constant time complexity
        if (it == phones.end()) {
            return -1;
        }
        
        int val = *it;
        phones.erase(it);
        return val;
    }
    
    /** Check if a number is available or not. */
    bool check(int number) {
        return phones.count(number) > 0;
    }
    
    /** Recycle or release a number. */
    void release(int number) {
        phones.insert(number);
    }
private:
    unordered_set<int> phones;
    
};

/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory* obj = new PhoneDirectory(maxNumbers);
 * int param_1 = obj->get();
 * bool param_2 = obj->check(number);
 * obj->release(number);
 */
```
