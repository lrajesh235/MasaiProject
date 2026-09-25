def execute_query(connection, query, params=None):
    cursor = connection.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def get_all_books(connection):
    query = "SELECT * FROM books;"
    return execute_query(connection, query)

def get_books_by_category(connection, category_id):
    query = "SELECT * FROM books WHERE category_id = ?;"
    return execute_query(connection, query, (category_id,))

def get_highest_rated_books(connection, limit=10):
    query = "SELECT * FROM books ORDER BY rating DESC LIMIT ?;"
    return execute_query(connection, query, (limit,))

def get_books_in_stock(connection):
    query = "SELECT * FROM books WHERE in_stock = 1;"
    return execute_query(connection, query)

def get_average_price_by_category(connection):
    query = """
    SELECT c.category_name, AVG(b.price_gbp) as average_price
    FROM books b
    JOIN categories c ON b.category_id = c.category_id
    GROUP BY c.category_name;
    """
    return execute_query(connection, query)