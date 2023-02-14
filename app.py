from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

@app.route("/")
def index():
    conn = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=testsqlservernab.database.windows.net;"
        "Database=testdb;"
        "UID=CloudSAc6dc0547;"
        "PWD=Hanu@1234567;"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nabeel")
    rows = cursor.fetchall()
    return render_template("index.html", rows=rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
