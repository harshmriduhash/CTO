import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection parameters
DB_URL = os.getenv('SUPABASE_DB_URL')

def init_db():
    if not DB_URL:
        print("Error: SUPABASE_DB_URL environment variable is not set.")
        return

    # Read the SQL file
    # Adjust this path to be relative to the script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.join(script_dir, '..', 'db', 'schema.sql')
    
    with open(schema_path, 'r') as file:
        sql_script = file.read()

    # Connect to the database
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    try:
        # Execute the SQL script
        cur.execute(sql_script)
        conn.commit()
        print("Database initialized successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    init_db()