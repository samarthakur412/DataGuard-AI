import os
import psycopg2
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

def get_connection():
    try:
        
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )

        logger.info("Database connection successful")

        return conn

    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        return None

























# import psycopg2


# def get_connection():
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="dataguard",
#             user="postgres",
#             password="6260347112S@m",
#             port="5432"
#         )

#         print("Database connection successful")
#         return conn

#     except Exception as e:
#         print("Database connection failed:", e)
#         return None