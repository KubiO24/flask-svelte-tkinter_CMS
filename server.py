from flask import Flask, send_from_directory, request
import random
import sqlite3

app = Flask(__name__)
myConnection = sqlite3.connect('data.sqlite', check_same_thread=False)

myCursor = myConnection.cursor()

myCursor.execute("""CREATE TABLE IF NOT EXISTS userList (
    clientID INT AUTO_INCREMENT PRIMARY KEY,
    username TEXT,
    email TEXT,
    password TEXT,
    userType INT
)""")

myConnection.commit()


###################################################################################################


def userExist(username):
    myCursor = myConnection.cursor()
    myCursor.execute(f'SELECT EXISTS(SELECT 1 FROM userList WHERE username="{username}")')
    row = myCursor.fetchall()
    if(row[0][0] == 1):
        return True
    return False


###################################################################################################


@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/register", methods = ['POST'])
def register():
    data = request.json
    username = data["username"]
    password = data["password"]
    email = data["email"]

    if(userExist(username)):
        return '0'

    myCursor.execute(f"""INSERT INTO userList
        (username, email, password, userType)
        VALUES
        ('{username}','{email}','{password}',0)""")
    myConnection.commit()
    return '1'

if __name__ == "__main__":
    app.run(debug=True)


