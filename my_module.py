# my_module.py
import requests
from bs4 import BeautifulSoup

def scrape_books(url):

    """Function to scrape book titles from a website"""

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('h3')
    book_titles = [book.get_text() for book in books]
    return book_titles

def save_to_file(data, filename):

    """Function to save scraped data to a file"""
    
    with open(filename, 'w') as file:
        for item in data:
            file.write(f"{item}\n")
