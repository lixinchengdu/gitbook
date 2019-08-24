# 197. Rising Temperature

* *Difficulty: Easy*

* *Topics: *

* *Similar Questions:*

## Problem:

<p>Given a <code>Weather</code> table, write a SQL query to find all dates&#39; Ids with higher temperature compared to its previous (yesterday&#39;s) dates.</p>

<pre>
+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
</pre>

<p>For example, return the following Ids for the above <code>Weather</code> table:</p>

<pre>
+----+
| Id |
+----+
|  2 |
|  4 |
+----+
</pre>

## Solutions:

```c++
# Write your MySQL query statement below
select Weather.Id from Weather Join Weather as w on DATEDIFF(weather.date, w.date) = 1 where Weather.Temperature > w.Temperature
```
