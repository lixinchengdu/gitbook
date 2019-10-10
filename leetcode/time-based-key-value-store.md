# 1023. Time Based Key-Value Store

* *Difficulty: Medium*

* *Topics: Hash Table, Binary Search*

* *Similar Questions:*

## Problem:

<p>Create a timebased key-value store class&nbsp;<code>TimeMap</code>, that supports two operations.</p>

<p>1. <code>set(string key, string value, int timestamp)</code></p>

<ul>
	<li>Stores the <code>key</code> and <code>value</code>, along with the given <code>timestamp</code>.</li>
</ul>

<p>2. <code>get(string key, int timestamp)</code></p>

<ul>
	<li>Returns a value such that <code>set(key, value, timestamp_prev)</code> was called previously, with <code>timestamp_prev &lt;= timestamp</code>.</li>
	<li>If there are multiple such values, it returns the one with the largest <code>timestamp_prev</code>.</li>
	<li>If there are no values, it returns the empty string (<code>&quot;&quot;</code>).</li>
</ul>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>inputs = <span id="example-input-1-1">[&quot;TimeMap&quot;,&quot;set&quot;,&quot;get&quot;,&quot;get&quot;,&quot;set&quot;,&quot;get&quot;,&quot;get&quot;]</span>, inputs = <span id="example-input-1-2">[[],[&quot;foo&quot;,&quot;bar&quot;,1],[&quot;foo&quot;,1],[&quot;foo&quot;,3],[&quot;foo&quot;,&quot;bar2&quot;,4],[&quot;foo&quot;,4],[&quot;foo&quot;,5]]</span>
<strong>Output: </strong><span id="example-output-1">[null,null,&quot;bar&quot;,&quot;bar&quot;,null,&quot;bar2&quot;,&quot;bar2&quot;]</span>
<strong>Explanation: </strong><span id="example-output-1">&nbsp; 
TimeMap kv; &nbsp; 
kv.set(&quot;foo&quot;, &quot;bar&quot;, 1); // store the key &quot;foo&quot; and value &quot;bar&quot; along with timestamp = 1 &nbsp; 
kv.get(&quot;foo&quot;, 1);  // output &quot;bar&quot; &nbsp; 
kv.get(&quot;foo&quot;, 3); // output &quot;bar&quot; since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie &quot;bar&quot; &nbsp; 
kv.set(&quot;foo&quot;, &quot;bar2&quot;, 4); &nbsp; 
kv.get(&quot;foo&quot;, 4); // output &quot;bar2&quot; &nbsp; 
kv.get(&quot;foo&quot;, 5); //output &quot;bar2&quot; &nbsp; 
</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>inputs = <span id="example-input-2-1">[&quot;TimeMap&quot;,&quot;set&quot;,&quot;set&quot;,&quot;get&quot;,&quot;get&quot;,&quot;get&quot;,&quot;get&quot;,&quot;get&quot;]</span>, inputs = <span id="example-input-2-2">[[],[&quot;love&quot;,&quot;high&quot;,10],[&quot;love&quot;,&quot;low&quot;,20],[&quot;love&quot;,5],[&quot;love&quot;,10],[&quot;love&quot;,15],[&quot;love&quot;,20],[&quot;love&quot;,25]]</span>
<strong>Output: </strong><span id="example-output-2">[null,null,null,&quot;&quot;,&quot;high&quot;,&quot;high&quot;,&quot;low&quot;,&quot;low&quot;]</span>
</pre>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>All key/value strings are lowercase.</li>
	<li>All key/value strings have&nbsp;length in the range&nbsp;<code>[1, 100]</code></li>
	<li>The <code>timestamps</code> for all <code>TimeMap.set</code> operations are strictly increasing.</li>
	<li><code>1 &lt;= timestamp &lt;= 10^7</code></li>
	<li><code>TimeMap.set</code> and <code>TimeMap.get</code>&nbsp;functions will be called a total of <code>120000</code> times (combined) per test case.</li>
</ol>

## Solutions:

```c++
class TimeMap {
public:
    /** Initialize your data structure here. */
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        keyToValues[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        if (keyToValues.count(key) == 0)    return "";
        string dummy;
        auto upperBound = upper_bound(keyToValues[key].begin(), keyToValues[key].end(), make_pair(timestamp + 1, dummy)); // pay attention to +1
        if (upperBound == keyToValues[key].begin())   return "";
        return prev(upperBound)->second;
    }
    
private:
    unordered_map<string, vector<pair<int, string>>> keyToValues;
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
```
