import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

def get_product_data(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    # Product Title
    title_tag = soup.find("span", {"class": "B_NuCI"})
    
    # Price
    price_tag = soup.find("div", {"class": "_30jeq3 _16Jk6d"})
    
    # Rating
    rating_tag = soup.find("div", {"class": "_3LWZlK"})

    title = title_tag.text.strip() if title_tag else "N/A"
    price = price_tag.text.strip() if price_tag else "N/A"
    rating = rating_tag.text.strip() if rating_tag else "N/A"

    return title, price, rating