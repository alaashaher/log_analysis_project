-Log Analysis Project BY Alaa shaher

-This is project to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.
   
-This Project answered the three Quation:

   - What are the most popular three articles of all time?
   - Who are the most popular article authors of all time?
   - On which days did more than 1% of requests lead to errors?
   
            ******************************************
            
-How to run the project :-  
  
  - Install Python 3 onto your computer.
  - Install Vagrant and VirtualBox.
  - Download the VM configuration
     - use Github to fork and clone the repository
        "https://github.com/udacity/fullstack-nanodegree-vm".
  - Start the VM:
     - from the bash git, run the vagrant up and run the vagrant ssh to log in.
     
  - Extract compressed file 'log analysis project'.
  - Then cd into the vagrant directory and then cd to 'log analysis project' file 
  - Setup  the Database
    - use the following command 'psql -d news -f newsdata.sql'
  - Make Views by running the two queries belwo.
    - Run this command 'python log-analysis.py'
    
        *************************************************


        *************************************************

- I create two database views:

  1 - create view ALL_Status as select time::date as day , count(*) from log group by day;
  
  2 - create view Logs as select time::date as day , count(*) as errors 
      from log where status = '404 NOT FOUND' group by day;

        *****************************************************

- What's included

  - log-analysis.py :- This is the main code for the application
                               
  - newsdata.sql :- it is the database that includes three tables:
                    1-The authors table that contain information about the authors of articles.
                    2-The articles table that contain the articles themselves.
                    3-The log table that contain one entry for each time a user has accessed the site.


  

  