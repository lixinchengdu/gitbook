# 196. Delete Duplicate Emails

* *Difficulty: Easy*

* *Topics: *

* *Similar Questions:*

## Problem:

<p>Write a SQL query to <strong>delete</strong> all duplicate email entries in a table named <code>Person</code>, keeping only unique emails based on its <i>smallest</i> <b>Id</b>.</p>

<pre>
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
</pre>

<p>For example, after running your query, the above <code>Person</code> table should have the following rows:</p>

<pre>
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
</pre>

<p><strong>Note:</strong></p>

<p>Your output is the whole <code>Person</code>&nbsp;table after executing your sql. Use <code>delete</code> statement.</p>

## Solutions:

```c++
# Write your MySQL query statement below
delete p1
 FROM Person p1 join Person p2
 on p1.Email = p2.Email AND p1.Id > p2.Id;

```
