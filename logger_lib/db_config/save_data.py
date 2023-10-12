from logger_lib.db_config.connect import get_session
import json
from datetime import datetime

def save_data(service_name: str, raw_response: json, log_status: str):
    cursor, connection = get_session()
    try:
        insert_query = """INSERT INTO custom_logs (service_name, raw_response, log_status, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)"""
        print("INSERT QUERY: ", insert_query)
        insertion_data = (
            service_name,
            raw_response,
            log_status,
            datetime.now().utcnow(),
            datetime.now().utcnow(),
        )
        print("DATA: ", insertion_data)
        cursor.execute(insert_query, insertion_data)
        connection.commit()

    except Exception as e:
        print(e)
        connection.rollback()