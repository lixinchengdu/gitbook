# 362. Design Hit Counter

* *Difficulty: Medium*

* *Topics: Design*

* *Similar Questions:*

  * [Logger Rate Limiter](logger-rate-limiter.md)

## Problem:

<p>Design a hit counter which counts the number of hits received in the past 5 minutes.</p>

<p>Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.</p>

<p>It is possible that several hits arrive roughly at the same time.</p>

<p><b>Example:</b></p>

<pre>
HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 
</pre>

<p><b>Follow up:</b><br />
What if the number of hits per second could be very large? Does your design scale?</p>
## Solutions:

```c++
class HitCounter {
public:
    /** Initialize your data structure here. */
    HitCounter() {
        
    }
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    void hit(int timestamp) {
        log.push_back(timestamp);
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    int getHits(int timestamp) {
        int start = timestamp - 299;
        int end = timestamp;
        
        auto lower = lower_bound(log.begin(), log.end(), start);
        auto upper = upper_bound(log.begin(), log.end(), end);
        
        return distance(lower, upper);
        
    }
    
private:
    vector<int> log;
};

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter* obj = new HitCounter();
 * obj->hit(timestamp);
 * int param_2 = obj->getHits(timestamp);
 */
```
