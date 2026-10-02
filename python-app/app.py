from flask import Flask
import os
import socket
import psycopg2
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv() 
@app.route("/")
def hello():
    return "Hello from Python Docker App!"

@app.route("/health")
def health():
    return "Healthy"

@app.route("/api/system")
def sysinfo():
    return [socket.gethostname(), os.getuid(), os.getcwd()]

@app.route("/api/message")
def postgrescon():
    try:
    # 1. Establish the connection
      connection = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        dbname=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),  # No password hardcoded here!
        port=os.environ.get("DB_PORT")
      )

    # 2. Create a cursor object to execute SQL commands
      cursor = connection.cursor()
    
    # 3. Execute a test query
      cursor.execute("SELECT version();")
    
    # 4. Fetch and print the result
      db_version = cursor.fetchone()
      print(f"Connection successful PostgreSQL version: {db_version[0]}")
      return f"Connection successful! PostgreSQL version: {db_version[0]}"
 
    except Exception as error:
      print(f"Error connecting to PostgreSQL: {error}")
      return{"status": "error", "message : ": str(error)}, 500 

    finally:
    # 5. Clean up and close connections
      if 'cursor' in locals():
        cursor.close()
      if 'connection' in locals():
        connection.close()
    print("PostgreSQL connection closed.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
