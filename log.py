#!/usr/bin/env python
import psycopg2

DBNAME = "news"
conn = psycopg2.connect(database=DBNAME)
cursor = conn.cursor()
        """ Quation 1 What are the most popular three articles of all time? """"
        cursor.execute("""
            select articles.title , count(*) as most_popular
            from articles, log
            where log.path = concat('/article/',articles.slug)
            group by articles.title order by most_popular desc limit 3;
          """)
q1 = cursor.fetchall()
print("\n"+"The most popular three articles of all time is:")
for row in q1:
        print("\t"+'"'+row[0]+'"'+" - "+str(row[1])+" most_popular")

        """Quation(2) Who are the most popular article authors of all time?"""
        cursor.execute("""
        select authors.name, count(*) as ""
        ""most_popular from articles, authors ,log
        where authors.id = articles.author and
        log.path = concat('/article/',articles.slug)
        group by authors.name  order by most_popular desc;
         """)
        q2 = cursor.fetchall()
        print("\n"+"The most popular article authors of all time is:")
        for row in q2:
                print("\t"+'"'+row[0]+'"'+" - "+str(row[1])+" most_popular")

        """Quation(3) On which days did more than 1% of ""
        ""requests lead to errors?"""
        cursor.execute("""
              select to_char(Logs.day,'Mon ,DD,YYYY'),
              round((Logs.errors*1.0/ALL_Status.count)*100.0,2)
              from Logs , ALL_Status
              where Logs.day = ALL_Status.day and
                    round((Logs.errors*100.0/ALL_Status.count),2) > 1.0;
         """)
        q3 = cursor.fetchall()
        print("\n"+"The day on which more 1% of requests lead to errors is:")
        for row in q3:
                print("\t"+row[0]+" - "+str(row[1])+"% errors")

        conn.close()
