import requests
from send_email import send_email

api_key = "ENV_VARIABLE" # This should be stored as an external variable
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&" \
        f"apiKey={api_key}&" \
        "language=en"

# Make a requests
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
body = ""
for article in content['articles'][:20]:
    if article['title'] is not None:
        body = "Subject: Today's Tech News" + "\n" \
        + body + article['title'] + "\n" \
        + article['description'] + "\n" \
        + article["url"] + 2*"\n"
    

body = body.encode('utf-8')
send_email(message=body)