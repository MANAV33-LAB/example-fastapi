import psycopg2
import psycopg2.extensions

print("Deleting the empty fastapi_server database...")

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
    
    # Delete the database
    cursor.execute("DROP DATABASE IF EXISTS fastapi_server;")
    print("✅ Deleted 'fastapi_server' database (the empty one)")
    
    conn.close()
except Exception as error:
    print(f"❌ Error: {error}")
