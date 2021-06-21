#!/usr/bin/env python3
#
# This is the code for printing out reports based on data in news database.

import psycopg2

DB_NAME = "news"


def print_articles():
    db = psycopg2.connect(database=DB_NAME)
    cr = db.cursor()
    cr.execute("select articles.title, count(*) as views \
                from articles, log \
                where log.path = '/article/' || articles.slug \
                group by articles.title \
                order by views desc Limit 3")
    results = cr.fetchall()
    print("\nQuery Result 1:- The most popular three articles of all time \n")
    for row in results:
        print(f"{row[0]} - {row[1]} views")
    db.close()


def print_authors():
    db = psycopg2.connect(database=DB_NAME)
    cr = db.cursor()
    cr.execute("select authors.name, count(authors.name) as views \
                from log, \
                    articles JOIN authors ON authors.id = articles.author \
                where log.path = '/article/' || articles.slug \
                group by authors.name \
                order by views desc")
    results = cr.fetchall()
    print("\nQuery Result 2:- The most popular article authors of all time \n")
    for row in results:
        print(f"{row[0]} - {row[1]} views")
    db.close()


def print_request_error_day():
    db = psycopg2.connect(database=DB_NAME)
    cr = db.cursor()
    cr.execute("select date(time) as log_date, \
                        trunc(count(case when status like '%404%' then 1 end) \
                            *100.0 /count(*) ,2) \
                        as percentage_error \
                from log \
                group by date(time) \
                having count(case when status like '%404%' then 1 end) \
                            *100.0 /count(*) >1")
    results = cr.fetchall()
    print("\nQuery Result 3:- More than 1% of requests lead to errors \n")
    for row in results:
        error_date = row[0]
        error_percent = row[1]
        print(f"{error_date:%B %d,%Y} - {error_percent}% errors")
    db.close()


if __name__ == '__main__':
    # Most popular three articles.
    print_articles()
    # Most popular article authors.
    print_authors()
    # More than 1 % error requests.
    print_request_error_day()
