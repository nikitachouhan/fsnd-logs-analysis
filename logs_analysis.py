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
                where log.path = concat('/article/', articles.slug) \
                group by articles.title \
                order by views desc Limit 3")
    results = cr.fetchall()
    print("\nQuery Result 1:- The most popular three articles of all time \n")
    for row in results:
        print("{} - {} views".format(row[0], row[1]))
    db.close()


def print_authors():
    db = psycopg2.connect(database=DB_NAME)
    cr = db.cursor()
    cr.execute("select authors.name, count(*) as views \
                from (select * \
                      from articles,log \
                      where log.path = concat('/article/', articles.slug) \
                      ) as popular_articles, authors \
                where authors.id = popular_articles.author \
                group by authors.name \
                order by views desc")
    results = cr.fetchall()
    print("\nQuery Result 2:- The most popular article authors of all time \n")
    for row in results:
        print("{} - {} views".format(row[0], row[1]))
    db.close()


def print_request_error_day():
    db = psycopg2.connect(database=DB_NAME)
    cr = db.cursor()
    cr.execute("select date_log, trunc(percentage_error,2) \
                from (select date_log, ((error_count*100.0)/total_count) \
                                        as percentage_error \
                    from (select date(time) as date_log, \
                            count(case when status like '%404%' then 1 end) \
                                 as error_count, \
                            count(*) as total_count \
                            from log \
                            group by date(time) \
                        ) as error_results \
                ) as percentage_results \
                where percentage_error > 1")
    results = cr.fetchall()
    print("\nQuery Result 3:- More than 1% of requests lead to errors \n")
    format_string = '{} {},{} - {}% errors'
    for row in results:
        month = row[0].strftime("%B")
        day = row[0].strftime("%d")
        year = row[0].strftime("%Y")
        error_percent = row[1]
        print(format_string.format(month, day, year, error_percent))
    db.close()


if __name__ == '__main__':
    # Most popular three articles.
    print_articles()
    # Most popular article authors.
    print_authors()
    # More than 1 % error requests.
    print_request_error_day()
