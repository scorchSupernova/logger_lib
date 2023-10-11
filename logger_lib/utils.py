import json
from datetime import datetime
from django.db import connections



primary_db = connections["default"]
primary_conn = primary_db.cursor()


def save_log_data(service_name: str, raw_response: json, log_status: str):
    try:
        insert_query = """INSERT INTO customer_logs (service_name, raw_response, log_status, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)"""
        print("INSERT QUERY: ", insert_query)
        insertion_data = (
            service_name,
            raw_response,
            log_status,
            datetime.now().utcnow(),
            datetime.now().utcnow(),
        )
        print("DATA: ", insertion_data)
        primary_conn.execute(insert_query, insertion_data)

    except Exception as e:
        print(e)

