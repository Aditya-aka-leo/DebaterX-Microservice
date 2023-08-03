import requests
from bs4 import BeautifulSoup
def scrape(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching the page: {e}")
        return None
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()

    return text


    
