# 182. Duplicate Emails

* *Difficulty: Easy*

* *Topics: *

* *Similar Questions:*

## Problem:

<p>Write a SQL query to find all duplicate emails in a table named <code>Person</code>.</p>

<pre>
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
</pre>

<p>For example, your query should return the following for the above table:</p>

<pre>
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
</pre>

<p><strong>Note</strong>: All emails are in lowercase.</p>

## Solutions:

```c++
# Write your MySQL query statement below
SELECT Email FROM
(SELECT Email, COUNT(Id) AS C
FROM Person
GROUP BY Email
 ) AS T
WHERE T.C > 1
 
 
```
