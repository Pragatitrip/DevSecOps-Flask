from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = db.cursor()
    cursor.execute("SELECT 'Hello from DevSecOps behind pfSense'")
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return str(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
