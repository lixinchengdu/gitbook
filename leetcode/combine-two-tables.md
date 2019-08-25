# 175. Combine Two Tables

* *Difficulty: Easy*

* *Topics: *

* *Similar Questions:*

  * [Employee Bonus](employee-bonus.md)

## Problem:

<p>Table: <code>Person</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
</pre>

<p>Table: <code>Address</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
</pre>

<p>&nbsp;</p>

<p>Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:</p>

<pre>
FirstName, LastName, City, State
</pre>

## Solutions:

```c++
# Write your MySQL query statement below
SELECT Person.FirstName, Person.LastName, Address.City, Address.State FROM Person LEFT JOIN Address on Person.PersonId = Address.PersonId 
```
