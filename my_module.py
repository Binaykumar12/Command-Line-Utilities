# my_module.py
import requests

def scrape_website(url):
    """Function to scrape data from a website"""
    response = requests.get(url)
    return response.text

def save_to_file(data, filename):
    """Function to save scraped data to a file"""
    with open(filename, 'w') as file:
        file.write(data)
