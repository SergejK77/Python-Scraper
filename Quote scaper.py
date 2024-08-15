import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f"Quote: {text}")
        print(f"Author: {author}\n")


if __name__ == "__main__":
    tags = "simile"
    if tags == "":
        TAG_URL = ""
    else:
        TAG_URL = "tag/" + tags + "/"
    URL = "https://quotes.toscrape.com/" + TAG_URL
    scrape_website(URL)
