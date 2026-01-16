import psycopg2
import psycopg2.extensions

print("Creating database if missing...")

try:
    # Connect to default database
    conn = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password="RJTRIXU@#143"
    )
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    
    # Create the database
    cursor.execute("CREATE DATABASE fastapi_server;")
    print("✅ Created 'fastapi_server' database!")
    
    conn.close()
    print("✅ Done! Try your main.py now")
    
except Exception as error:
    print(f"❌ Failed to create: {error}")
