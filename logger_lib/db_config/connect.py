import psycopg2

conn_cursor = None
global db_dsn

def connect(dsn: str):
    try:
        db_dsn = dsn
        global conn_cursor
        conn = psycopg2.connect(dsn)
        conn_cursor = conn.cursor()
        print("connection cursor: ")
        create_table()
        print("Table created")
    except Exception as e:
        print(e)

def create_table():
    try:
        conn_cursor.execute("""
            CREATE TABLE IF NOT EXISTS customer_logs (
                id SERIAL PRIMARY KEY,
                service_name VARCHAR(255) NOT NULL,
                raw_response JSON NOT NULL,
                log_status VARCHAR(255) NOT NULL,
                created_at TIMESTAMP NOT NULL,
                updated_at TIMESTAMP NOT NULL
            )
        """)
        print("Table created!!!")
    except Exception as e:
        print(e)


def get_session():
    if conn_cursor:
        return conn_cursor
    else:
        print("No connection")
        connect(db_dsn)
        if conn_cursor:
            return conn_cursor
