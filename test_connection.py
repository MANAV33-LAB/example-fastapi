import psycopg2
from psycopg2.extras import RealDictCursor

try:
    conn = psycopg2.connect(
        host='localhost',
        database='fastapi_server',
        user='postgres',
        password="RJTRIXU@#143",
        cursor_factory=RealDictCursor
    )
    print("✅ Connected to database created in pgAdmin 4!")
    
    cursor = conn.cursor()
    cursor.execute("SELECT current_database();")
    result = cursor.fetchone()
    print(f"✅ Database name: {result['current_database']}")
    
    conn.close()
except Exception as e:
    print(f"❌ Error: {e}")
