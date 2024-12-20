import requests
from send_email import send_email

api_key = "ENV_VARIABLE" # This should be stored as an external variable
url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}"

# Make a requests
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
body = ""
for article in content['articles']:
    if article['title'] is not None:
        body = body + article['title'] + "\n" + article['description'] + 2*"\n"
    

body = body.encode('utf-8')
send_email(message=body)