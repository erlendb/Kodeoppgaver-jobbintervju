# Vipps assignment

## Tasks
### Task 1
Count the occurances of a string in a Wikipedia article.

Wikipedia API: `https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=[topic]`

### Task 2
Create an API that takes article title as argument and returns the count of the article name in the article text.
Create some kind of frontend to display the results.

## Solution
### Task 1

Fetches the article with Requests, and prints the result in the terminal.
Run with `python3 api/article.py`

### Task 2
Instead of counting the article title in the article, I went with counting any given string in the article.

The article is fetched as in task 1.
A simple API is exposed with Bottle.
Run with `python3 api/api.py`.

The frontend displays a form and the string count on a simple web page.
Information is fetched from the API with Ajax.
View the frontend by opening `frontend/index.html` in a browser.