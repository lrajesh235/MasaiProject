import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd

# Constants
BASE_URL = "http://books.toscrape.com/catalogue/category/books_1/index.html"
CURRENCY_CONVERSION_RATE = 105.50  # 1 GBP = 105.50 INR

def scrape_books():
    books = []
    for page in range(1, 6):  # Scraping first 5 pages
        url = BASE_URL.replace('index.html', f'page-{page}.html')
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for book in soup.select('.product_pod'):
            title = book.h3.a['title']
            price_gbp = float(book.select_one('.price_color').text[1:])
            star_rating = book.p['class'][1]  # e.g., "Three"
            availability = book.select_one('.instock.availability').text.strip()
            category = soup.select_one('ul.breadcrumb li:nth-of-type(3) a').text
            
            books.append({
                'title': title,
                'price_gbp': price_gbp,
                'star_rating': star_rating,
                'availability': availability,
                'category': category
            })
    
    return books

def clean_books(books):
    for book in books:
        # Convert star rating to integer
        star_mapping = {
            'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5
        }
        book['rating'] = star_mapping.get(book['star_rating'], None)
        book['in_stock'] = 1 if 'In stock' in book['availability'] else 0
        book['price_inr'] = book['price_gbp'] * CURRENCY_CONVERSION_RATE

    # Drop books with missing ratings
    cleaned_books = [book for book in books if book['rating'] is not None]
    return cleaned_books

def load_to_database(books):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY,
            category_name TEXT UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY,
            title TEXT,
            price_gbp REAL,
            price_inr REAL,
            rating INTEGER,
            in_stock INTEGER,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories (category_id)
        )
    ''')

    # Insert categories and books
    for book in books:
        cursor.execute('''
            INSERT OR IGNORE INTO categories (category_name) VALUES (?)
        ''', (book['category'],))
        cursor.execute('''
            SELECT category_id FROM categories WHERE category_name = ?
        ''', (book['category'],))
        category_id = cursor.fetchone()[0]

        cursor.execute('''
            INSERT INTO books (title, price_gbp, price_inr, rating, in_stock, category_id) VALUES (?, ?, ?, ?, ?, ?)
        ''', (book['title'], book['price_gbp'], book['price_inr'], book['rating'], book['in_stock'], category_id))

    conn.commit()
    conn.close()

def main():
    books = scrape_books()
    cleaned_books = clean_books(books)
    load_to_database(cleaned_books)

if __name__ == "__main__":
    main()