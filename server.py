import os
import pyodbc
from flask import Flask

PORT = 8000
MESSAGE = "Hello, world! \n This is flask app(v-2.0.11).I am Nabeel \n"
# Get the connection string from an environment variable
conn_str = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:testsqlservernab.database.windows.net,1433;Database=testdb;Uid=CloudSAc6dc0547;Pwd=Hanu@1234567;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"


app = Flask(__name__)


@app.route("/")
def root():
    #result = MESSAGE.encode("utf-8")
    # Connect to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # Execute a SELECT statement to retrieve data from the database
    cursor.execute("SELECT * FROM mytable")
    rows = cursor.fetchall()
    
    # Build the response string
    result = MESSAGE
    result += "Data from Azure SQL database:\n"
    for row in rows:
        result += str(row) + "\n"
    
    return result.encode("utf-8")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
    

