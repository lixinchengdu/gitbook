# 359. Logger Rate Limiter

* *Difficulty: Easy*

* *Topics: Hash Table, Design*

* *Similar Questions:*

  * [Design Hit Counter](design-hit-counter.md)

## Problem:

<p>Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is <b>not printed in the last 10 seconds</b>.</p>

<p>Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.</p>

<p>It is possible that several messages arrive roughly at the same time.</p>

<p><b>Example:</b></p>

<pre>
Logger logger = new Logger();

// logging string &quot;foo&quot; at timestamp 1
logger.shouldPrintMessage(1, &quot;foo&quot;); returns true; 

// logging string &quot;bar&quot; at timestamp 2
logger.shouldPrintMessage(2,&quot;bar&quot;); returns true;

// logging string &quot;foo&quot; at timestamp 3
logger.shouldPrintMessage(3,&quot;foo&quot;); returns false;

// logging string &quot;bar&quot; at timestamp 8
logger.shouldPrintMessage(8,&quot;bar&quot;); returns false;

// logging string &quot;foo&quot; at timestamp 10
logger.shouldPrintMessage(10,&quot;foo&quot;); returns false;

// logging string &quot;foo&quot; at timestamp 11
logger.shouldPrintMessage(11,&quot;foo&quot;); returns true;
</pre>
## Solutions:

```c++
class Logger {
public:
    /** Initialize your data structure here. */
    Logger() {
        
    }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) {
        if (!lastTime.count(message)) {
            lastTime[message] = timestamp;
            return true;
        }
        
        if (timestamp - lastTime[message] >= 10) {
            lastTime[message] = timestamp;
            return true;
        } else {
            return false;
        }
    }
    
private:
    unordered_map<string, int> lastTime;
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */
```
