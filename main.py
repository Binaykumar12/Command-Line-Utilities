# main.py
import argparse
from my_module import scrape_books, save_to_file

def main():
    parser = argparse.ArgumentParser(description="Book Scraping Utility")
    parser.add_argument("url", help="URL of the website to scrape")
    parser.add_argument("-o", "--output", help="Output file to save the scraped data", default="books.txt")
    args = parser.parse_args()

    book_titles = scrape_books(args.url)
    save_to_file(book_titles, args.output)
    print(f"Data scraped from {args.url} and saved to {args.output}")

if __name__ == "__main__":
    main()
