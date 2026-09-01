1. get all statuses, not repeating, alphabetically ordered

```sql
SELECT DISTINCT status
FROM tasks
ORDER BY status;
```

2. get the count of all tasks in each project, order by tasks count descending

```sql
SELECT projects.name AS project, COUNT(tasks.id) AS tasks_count
FROM projects
LEFT JOIN tasks ON tasks.project_id = projects.id
GROUP BY projects.id
ORDER BY tasks_count DESC;
```

3. get the count of all tasks in each project, order by projects names

```sql
SELECT projects.name AS project, COUNT(tasks.id) AS tasks_count
FROM projects
LEFT JOIN tasks ON tasks.project_id = projects.id
GROUP BY projects.id
ORDER BY projects;
```

4. get the tasks for all projects having the name beginning with "N" letter

```sql
SELECT tasks.*
FROM tasks
JOIN projects ON tasks.project_id = projects.id
WHERE projects.name LIKE 'N%';
```

5. get the list of al projects containing the 'a' letter in the middle of the name, and show the tasks count near each project. Mention that there can exist projects without tasks and tasks with project_id= NULL

```sql
SELECT projects.name AS project, COUNT(tasks.id) AS tasks_count
FROM projects
LEFT JOIN tasks ON tasks.project_id = projects.id
WHERE projects.name LIKE '%a%'
GROUP BY projects.id
ORDER BY project;
```

6. get the list of tasks with duplicate names. Order alphabetically

```sql
SELECT name, COUNT(*) AS matches_count
FROM tasks
GROUP BY name
HAVING COUNT(*) > 1
ORDER BY name;
```

7. get the list of tasks having several exact matches of both name and status, from the project 'Delivery’. Order by matches count

```sql
SELECT tasks.name, COUNT(*) AS matches_count
FROM tasks
JOIN projects ON tasks.project_id = projects.id
WHERE projects.name = 'Delivery'
GROUP BY tasks.name, tasks.status
HAVING COUNT(*) > 1
ORDER BY matches_count;
```

8. get the list of project names having more than 10 tasks in status 'completed'. Order by project_id

```sql
SELECT projects.name
FROM projects
JOIN tasks ON tasks.project_id = projects.id
WHERE tasks.status = 'completed'
GROUP BY projects.id
HAVING COUNT(tasks.id) > 10
ORDER BY projects.id;
```
