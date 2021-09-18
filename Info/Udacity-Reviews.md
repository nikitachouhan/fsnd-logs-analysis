# Review Comments

- [Suggestions](#suggestions)
- [Resources](#resources)

## Suggestions

1. For multi-line query statements, using the triple quotation (either ''' or """) mark,
   makes it easy to understand the code and also more readable.
   To improve readability, capitalize all keywords and separate each new clause by a new line.
   e.g.:

```python
query = """
CREATE VIEW all_count AS
SELECT date(TIME) AS DAY,
       count(*) AS all_method
FROM log
GROUP BY DAY;
"""
```

2. str.format was a major breakthrough in Strings formatting in Python 3 compared to Python-2 %-format.
   But sometimes it can be pretty verbose.
   From Python 3.6, f-strings have emerged as a less verbose and faster form for formatting.

```sh
>>> name = "Eric"
>>> age = 74
>>> f"Hello, {name}. You are {age}."
Hello, Eric. You are 74.'
```

3. According to this project rubric, you can't use multiple selects. Instead of it, you must JOIN tables when needed.

For example:

```sql
  SELECT author.name, count(author.name) AS Views
    FROM log l, articles a JOIN authors author ON author.id = a.author
   WHERE l.path = '/article/' || a.slug
GROUP BY author.name
ORDER BY Views DESC
```

## Resources

- [PostgreSQL JOIN](https://www.w3resource.com/PostgreSQL/postgresql-join.php)
  The main concept which is focusing on a join is that, two or more data sets, when joined, combined their columns into a new set of rows, including each of the columns requested from each of the data sets.

- [How to Control Vagrant Box Using Vagrant commands](https://www.linuxshelltips.com/basic-vagrant-commands/)
  This article focus on customizing the vagrant file according to our requirements and see important commands to work with the vagrant.
