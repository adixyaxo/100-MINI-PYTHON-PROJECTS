# This is a app where you can read the daily news in python 
# we are going to use newsapi.org for this purpose
from datetime import date as dt
import requests
api_key = "2abfe998f0eb4d0e95f89b04a8e694d1"


def main():
    global api_key
    print("Welcome to the News App")
    query = input("Enter the topic you want to search news for: ")
    query = query.strip()
    query = query.replace(" ", "+")
    date = input("Enter the date from which you want news (YYYY-MM-DD): ")
    no_of_articles = int(input("Enter the number of articles you want to read: "))
    if date == "today":
        date = dt.today().strftime('%Y-%m-%d')
    url = f"https://newsapi.org/v2/everything?q={query}&from={date}&sortBy=publishedAt&apiKey={api_key}"
    print(f"Fetching news from: {url}")
    response = requests.get(url)
    news_data = response.json()
    print(news_data)
    status = news_data['status']
    totalResults = news_data['totalResults']
    articles = news_data['articles']
    if status == "ok":
        print(f"Total Results: {news_data['totalResults']}")
        for i in range (0,no_of_articles):
                dict = articles[i]
                source = dict['source']['name']
                author = dict['author']
                title = dict['title']
                description = dict['description']
                url = dict['url']
                publishedAt = dict['publishedAt']
                content = dict['content']
                content = content.remove("[+")
                content = content.remove(" ]")
                print(f"\nArticle {i+1}:")
                print(f"Source: {source}")
                print(f"Author: {author}")
                print(f"Title: {title}")
                print(f"Description: {description}")
                print(f"URL: {url}")
                print(f"Published At: {publishedAt}")
                print(f"Content: {content}\n")
        else:
            print("Failed to fetch news")
if __name__ == "__main__":
    main()