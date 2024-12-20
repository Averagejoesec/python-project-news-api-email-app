import requests

api_key = "ENV_VARIABLE" # This should be stored as an external variable
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=APIKEY"

# Make a requests
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])