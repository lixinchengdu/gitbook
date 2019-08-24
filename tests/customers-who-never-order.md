# 183. Customers Who Never Order

* *Difficulty: Easy*

* *Topics: *

* *Similar Questions:*

## Problem:

<p>Suppose that a website contains two tables, the <code>Customers</code> table and the <code>Orders</code> table. Write a SQL query to find all customers who never order anything.</p>

<p>Table: <code>Customers</code>.</p>

<pre>
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
</pre>

<p>Table: <code>Orders</code>.</p>

<pre>
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
</pre>

<p>Using the above tables as example, return the following:</p>

<pre>
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
</pre>

## Solutions:

```c++
# Write your MySQL query statement below
select Customers.Name as 'Customers' from Customers left join Orders on Customers.Id = Orders.CustomerId where Orders.Id is NULL
```
