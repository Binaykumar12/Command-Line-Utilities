# main.py
import argparse
from my_module import scrape_website, save_to_file

def main():
    parser = argparse.ArgumentParser(description="Web Scraping Utility")
    parser.add_argument("url", help="URL of the website to scrape")
    parser.add_argument("-o", "--output", help="Output file to save the scraped data", default="output.txt")
    args = parser.parse_args()

    data = scrape_website(args.url)
    save_to_file(data, args.output)
    print(f"Data scraped from {args.url} and saved to {args.output}")

if __name__ == "__main__":
    main()
