import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    response = requests.get(url)
    if response.ok == True:
        soup = BeautifulSoup(response.text, 'html.parser')
        country_card = soup.find_all('div', class_="col-md-4 country")
        for country in country_card:
            country_name = country.find('h3', class_='country-name').get_text().strip()
            country_info = country.find('div', class_='country-info').get_text()
            print(f"Country is: {country_name}\r\nand the info is:\r\n{country_info}")
    else:
        print("URL not reachable!")


if __name__ == "__main__":
    URL = "http://www.scrapethissite.com/pages/simple/"
    scrape_website(URL)
