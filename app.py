from flask import Flask, render_template
import pyodbc
import os

app = Flask(__name__)

@app.route("/")
def index():
    my_secret = os.environ.get('SQLCONNSTR_MySecret')
    print(f'The value of MySecret is {my_secret}')
    conn = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=testsqlservernab.privatelink.database.windows.net;"
        "Database=testdb;"
        "UID=CloudSAc6dc0547;"
        f"PWD={my_secret};"
    )
#     "Server=testsqlservernab.database.windows.net;
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nabeel")
    rows = cursor.fetchall()
    return render_template("index.html", rows=rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
