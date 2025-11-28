import json
import re
import sqlite3
import os

INPUT_DATA_FILE = 'task1_d.json'
DATABASE_NAME = 'library_books.db'


def convert_ruby_hash_to_json(file_path):
    """Reads Ruby-style hash file and converts it to Python list of dicts."""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Convert Ruby symbol keys (:name=>) to JSON format ("name":)
        content = re.sub(r':(\w+)=>', r'"\1":', content)
        content = content.replace('nil', 'null')
        
        return json.loads(content)

    except (json.JSONDecodeError, IOError) as error:
        print(f"Error reading file: {error}")
        return []


def create_tables(cursor):
    """Create database tables."""
    cursor.execute('DROP TABLE IF EXISTS book_inventory')
    cursor.execute('DROP TABLE IF EXISTS year_summary')
    
    cursor.execute('''
        CREATE TABLE book_inventory (
            id TEXT PRIMARY KEY,
            title TEXT,
            author TEXT,
            genre TEXT,
            publisher TEXT,
            publication_year INTEGER,
            original_price TEXT
        )
    ''')


def insert_books(cursor, books):
    """Insert book records into database."""
    rows = [
        (
            str(book.get('id')),
            book.get('title'),
            book.get('author'),
            book.get('genre'),
            book.get('publisher'),
            book.get('year'),
            book.get('price', '').strip()
        )
        for book in books
    ]

    cursor.executemany('''
        INSERT OR IGNORE INTO book_inventory (
            id, title, author, genre,
            publisher, publication_year, original_price
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', rows)
    
    return len(rows)


def create_summary_table(cursor):
    """Create summary table with SQL transformation (EUR to USD conversion)."""
    cursor.execute('''
        CREATE TABLE year_summary AS
        SELECT 
            publication_year,
            COUNT(*) as book_count,
            ROUND(
                AVG(
                    CASE 
                        WHEN substr(original_price, 1, 1) = '€' 
                        THEN CAST(substr(original_price, 2) AS REAL) * 1.2
                        ELSE CAST(substr(original_price, 2) AS REAL)
                    END
                ), 2
            ) as average_price_usd
        FROM book_inventory
        GROUP BY publication_year
        ORDER BY publication_year ASC
    ''')


def display_results(cursor):
    """Display row counts and summary table content."""
    cursor.execute("SELECT COUNT(*) FROM book_inventory")
    print(f"Table 'book_inventory': {cursor.fetchone()[0]} rows")

    cursor.execute("SELECT COUNT(*) FROM year_summary")
    print(f"Table 'year_summary':   {cursor.fetchone()[0]} rows")

    print(f"\n{'Year':<10} | {'Book Count':<12} | {'Avg Price (USD)':<15}")
    print("-" * 45)

    cursor.execute("SELECT * FROM year_summary")
    for year, count, avg_price in cursor.fetchall():
        print(f"{year:<10} | {count:<12} | ${avg_price:<15}")


def main():
    books = convert_ruby_hash_to_json(INPUT_DATA_FILE)
    
    if not books:
        print("No books loaded. Exiting.")
        return

    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        
        create_tables(cursor)
        insert_books(cursor, books)
        conn.commit()
        
        create_summary_table(cursor)
        conn.commit()
        
        display_results(cursor)


if __name__ == "__main__":
    main()
