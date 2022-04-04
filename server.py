from flask import Flask, send_from_directory
import random
import sqlite3

app = Flask(__name__)
myConnection = sqlite3.connect('userData.sqlite')

myCursor = myConnection.cursor()

myCursor.execute("""CREATE TABLE IF NOT EXISTS userList (
    username VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    userType INT,
    clientID INT AUTO_INCREMENT PRIMARY KEY)""")
myConnection.commit()
myConnection.close()


# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

if __name__ == "__main__":
    app.run(debug=True)