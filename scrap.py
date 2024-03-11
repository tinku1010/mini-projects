import requests
from bs4 import BeautifulSoup

def get_news_headlines(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the elements containing news headlines
    headlines = soup.find_all('h2', class_='headline')

    # Extract the text from each headline and store it in a list
    news_headlines = [headline.text.strip() for headline in headlines]

    return news_headlines


# Example usage
url = 'https://www.hindustantimes.com/'
headlines = get_news_headlines(url)
print("News Headlines:")
for headline in headlines:
    print(headline)