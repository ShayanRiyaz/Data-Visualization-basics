import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response

language = input("Enter the desired programming language: ") 
                 
url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars'
headers = {'Accept' : 'application/vnd.github.v3+json'}
r = requests.get(url,headers = headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the respositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Process results.
repo_links, stars, labels = [], [], []

# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")

# Process results.
for key in sorted(repo_dict.keys()):
    print(key)
    
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href = '{repo_url}' > {repo_name} </a>"
    repo_links.append(repo_link)
    #repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br >/{description}"
    labels.append(label)
    
    
# Make visualization.
data = [{
    'type'  : 'bar',
    'x'     : repo_links,
    'y'     : stars,
    'hovertext' : labels,
    'marker': {
        'color' : 'rgb(60,100,150)',
        'line'  : {'width' : 1.5,
                   'color' : 'rgb(25,25,25)'}
    },
    'opacity' : 0.6,
                   
}]

my_layout = {
    'title' : f'Most-Starred {language} Projects on GitHub',
    'titlefont' : {'size' : 28},
    
    'xaxis' : {
        'title' : 'Repository',
        'titlefont' : {'size' : 24},
        'tickfont'  : {'size' : 14},
    },
    'yaxis' : {
        'title' : 'Stars',
        'titlefont' : {'size' : 24},
        'tickfont'  : {'size' : 14},
                      
    },
}

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig,filename = f'Assets/{language}-repos.html')

