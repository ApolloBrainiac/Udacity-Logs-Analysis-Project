# Udacity Logs Analysis Project
3rd Project for Udacity's [Fullstack Nanodegree Program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).
***

## Project Details:
***
#### Task

*You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an __internal reporting tool__ that will use information from the database to discover what kind of articles the site's readers like.*

*The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.*

*The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.*

#### Questions to Answer:
1. __What are the most popular three articles of all time?__ Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2. __Who are the most popular article authors of all time?__ That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top

3. __On which days did more than 1% of requests lead to errors?__ The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## Setup:

This project was developed on a Vagrant run virtual machine.

__