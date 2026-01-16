import psycopg2
from psycopg2.extras import RealDictCursor

print("Testing connection...")

try:
    conn = psycopg2.connect(
        host='localhost',
        database='postgres',  # Try DEFAULT database first
        user='postgres',
        password="RJTRIXU@#143",
        cursor_factory=RealDictCursor
    )
    print("✅ STEP 1: Connected to DEFAULT 'postgres' database!")
    
    # Check if fastapi_server exists
    cursor = conn.cursor()
    cursor.execute("SELECT datname FROM pg_database WHERE datname = 'fastapi_server';")
    result = cursor.fetchone()
    
    if result:
        print(f"✅ STEP 2: Found 'fastapi_server' database: {result['datname']}")
    else:
        print("❌ STEP 2: 'fastapi_server' database NOT found in this connection")
    
    conn.close()
    
except Exception as error:
    print(f"❌ ERROR: {error}")
