import csv
from datetime import datetime
from scraper import get_product_data

URL = "https://www.flipkart.com/product1"

def save_to_csv(data):
    file_path = "data/prices.csv"
    
    try:
        with open(file_path, "x", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Price", "Rating", "Date"])
    except FileExistsError:
        pass

    with open(file_path, "a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    title, price, rating = get_product_data(URL)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    save_to_csv([title, price, rating, date])
    print("✅ Data saved successfully!")

if __name__ == "__main__":
    main()
