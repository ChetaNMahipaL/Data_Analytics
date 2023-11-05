# Web Scraping and Data Analysis with Bag of Words

## Introduction

This repository showcases my work on an assignment involving web scraping, data analysis, and the creation of a word cloud using Python. The assignment is divided into two tasks, each with its own set of requirements.

## Task 1 - Web Scraping and Data Analysis

### Task 1.1 - Web Scraping and Graph Plotting

In this part of the assignment, I was tasked with the following:

1. Write a Python script to scrape the top 1000 highest-grossing movies of all time from the IMDB website. After scraping the data, save it to a file named 'q1text.txt' for further analysis. Additionally, I was required to use the obtained data to plot the following graphs:
   - A bar graph of the genre to the frequency of movies belonging to that genre.
   - A line graph of the top 100 movies and their gross value.

### Task 1.2 - Data Filtering and Sorting

In the second part of Task 1, I created a Python program that performs the following:

1. Prints the top 100 movies in descending order of their IMDb rating. If two movies have the same IMDb rating, they are sorted based on increasing runtime.
2. Enables the user to filter the list of top 1000 movies based on the following criteria:
   - Duration
   - IMDb Rating
   - Year of Release
   - Genre
   For the first three criteria, the user is prompted to enter a range, and the entries that fall within the range are displayed. For the genre, the user is prompted to enter a genre, and all the movies belonging to that genre are printed.

## Task 2 - Text Data Analysis

In Task 2, I focused on manipulating text data in Python. The objective was to create a word cloud from a given text file while removing common English stopwords. This task consisted of the following steps:

1. Reading the 'sh.txt' file containing text data to generate a word cloud.
2. Removing English stopwords using a manual approach.
3. Printing the most common word in 'sh.txt' after removing the stopwords.
4. Calculating and printing the average word length of the words in 'sh.txt'.

## Submission Files

This repository contains the following files related to the assignment:

- q1.py: Python script for Task 1.1 (Web scraping and graph plotting).
- q2.py: Python program for Task 1.2 (Data filtering and sorting).
- q3.py: Python script for Task 2 (Text data analysis and word cloud generation).
- q1text.txt: File containing scraped data from Task 1.1.
- graph1.png: Bar graph generated in Task 1.1.
- graph2.png: Line graph generated in Task 1.1.
- wordcloud.png: Word cloud generated in Task 2.

## Instructions

To view the code and results for each task, please explore the respective Python script files (q1.py, q2.py, q3.py) and the generated image files (graph1.png, graph2.png, wordcloud.png).
