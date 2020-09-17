import requests
import config
import sys
from colorama import init, Fore

init(autoreset=True)

headers = {
    "api-key": config.DEV_API_KEY
}

url = f"https://dev.to/api/articles/me/published"

data = requests.get(url, headers=headers).json()
print(data)

article_list = []
for article in data:
    article_list.append(article["title"])

print(article_list)
