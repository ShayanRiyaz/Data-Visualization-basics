# Working with APIs

We will be writing two programs which use a web *Application Programming Interface (API)* to automatically request specific information from a website instead of reading the entire pages. We next use that information rather tha entire pages and then use that information to generate a visualization. 

The programs that work with APIs always use current data to generate a visualization, even when that data might be rapidly changing, it will always be upto date.

## Using a Web API

- A web API is a part of a webste designed to interact with programs. 
- These programs use very specific URLs to request certain information.
- This request is called an ***API call***.
- The requested data will be returned in an easily processed format (such as JSON or CSV).
- Most apps that rely on external data sources such as apps that integrate with social media sites, rely on API calls.

## Git and GitHub

For this project we will base our visualization on information from GitHub a site that allows programmers to collaborate on codingprojects we'll use GitHub's API to request new information about Python projects on site, then generate an interactive visualization of the relative popularity of these projects using Plotly.

### Requesting Data Using an API Call

GitHub's API lets you request a wide range of information through API calls.

to see how an API works enter this in your *browser address*:

```https://api.github.com/search/repositories?q=language:python&sort=starts```

This call returns the number of Python projects currentely hosted on GitHub as well as information about the most popular Python repositories. Lets examine the parts:
  ``` https://api.github.com/ ```
    Directs the request to the part of GitHub that responds to API calls.
    
  ``` search/repositories ```
    Tells the API to conduct a search through all repositories on GitHub.
    
  ``` q= ```
    The q stands for query and the '=' sign lets us begin specifying a query 
    
  ``` language:python ```
    We indicate that we want information only on repositories that have Python as the primary language
    
  ``` &sort=stars ```
    Sorts the projects by the number of stars they've been given.
     
   **Response**
    
  ```{
  "total_count": 5399722,
  "incomplete_results": false,
  "items": [
    {
      "id": 83222441,
      "node_id": "MDEwOlJlcG9zaXRvcnk4MzIyMjQ0MQ==",
      "name": "system-design-primer",
      "full_name": "donnemartin/system-design-primer",
  ```
   
   We can see that the response is not intended to be entered by humans as the format is meant to be processed by a program.
   
   **Note:** The value for "incomplete_results" is false, as the request was successful.
   
## Installing Requests
   
   The requests package allows a Python program to easily request information from a website and examine the response.
   ``` python -m pip install --user requests ```
   
   
### 1. GitHub API 

#### Steps:
1. Run using ```python popular_repositories.py``` or ```python3 popular_repositories.py``` in the working directory.
2. Enter the language you want to view

***Example:***
![Python-GitHub!](Assets/python-repos.png)


### 2. Hacker News API

The hacker news API provides access to data about all submissions and comments on the site and we can use the API **without having to register for a key**

The following call returns information about the current top article of this writing:
``` https://hacker-news.firebaseio.com/v0/item/19155826.json ```

When we enter this browser you'll see that the text on the page is enclodes by braces meaning it's a dictionry. However, the response is difficult to examine without some better formatting.

#### Steps:
1.Run using ```python hacker_news_submissions.py ``` or ```python 3 hacker_news_submissions.py ```
   
   
   
   
   
 


## Useful Resources

- https://plot.ly/python/user-guide/ -  ***[Plotly User Guide]***
- https://plot.ly/python/reference/  -  ***[Python Figure Reference]***
- https://developer.github.com/v3/   -  ***[GitHub API Documentation]***