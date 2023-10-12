import psycopg2

conn_cursor = None
db_dsn = ""
conn = None

def connect(dsn: str):
    try:
        global db_dsn
        db_dsn = dsn
        global conn_cursor, conn
        conn = psycopg2.connect(dsn)
        conn_cursor = conn.cursor()
        print("connection cursor: ", conn_cursor)
        create_table()
        print("Table created")
    except Exception as e:
        print(e)

def create_table():
    try:
        if conn_cursor.connection == conn:
            conn_cursor.execute("""
                CREATE TABLE IF NOT EXISTS custom_logs (
                    id SERIAL PRIMARY KEY,
                    service_name VARCHAR(255) NOT NULL,
                    raw_response JSON NOT NULL,
                    log_status VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP NOT NULL,
                    updated_at TIMESTAMP NOT NULL
                )
            """)
            conn.commit()
        print("Table created!!!")
    except Exception as e:
        conn.rollback()
        print(e)


def get_session() -> tuple:
    if conn_cursor:
        print("Connected already")
        return conn_cursor, conn
    else:
        print("No connection")
        connect(db_dsn)
        if conn_cursor:
            return conn_cursor, conn
