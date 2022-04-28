import flask
from flask import Flask, send_from_directory, request
import sqlite3
import json

app = Flask(__name__)
myConnection = sqlite3.connect('data.sqlite', check_same_thread=False)

myCursor = myConnection.cursor()

myCursor.execute("""CREATE TABLE IF NOT EXISTS userList (
    username TEXT,
    email TEXT,
    password TEXT,
    userType INT
)""")

# add admin if not exists
myCursor.execute("""
    INSERT INTO userList (username, email, password, userType)
    SELECT 'admin', 'admin', 'admin', 2
    WHERE NOT EXISTS(SELECT 1 FROM userList WHERE username = 'admin');
""")

myConnection.commit()


###################################################################################################


def userExist(username):
    myCursor = myConnection.cursor()
    myCursor.execute(f'SELECT EXISTS(SELECT 1 FROM userList WHERE LOWER(username)=LOWER("{username}"))')
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

    if userExist(username):
        return '0'

    myCursor.execute(f"""INSERT INTO userList
        (username, email, password, userType)
        VALUES
        ('{username}','{email}','{password}',0)""")
    myConnection.commit()
    return '1'

@app.route("/login", methods = ['POST'])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]

    myCursor = myConnection.cursor()
    myCursor.execute(f'SELECT EXISTS(SELECT 1 FROM userList WHERE LOWER(username)=LOWER("{username}") AND password="{password}")')
    row = myCursor.fetchall()
    if (row[0][0] == 1):
        return '1'
    return '0'

@app.route("/getPermission", methods = ['POST'])
def getPermission():
    username = request.data.decode("utf-8")
    myCursor = myConnection.cursor()
    myCursor.execute(f'SELECT userType FROM userList WHERE LOWER(userName) = LOWER("{username}");')
    permission = myCursor.fetchall()[0][0]
    return str(permission)

@app.route("/getProperUsername", methods = ['POST'])
def getProperUsername():
    username = request.data.decode("utf-8")
    myCursor = myConnection.cursor()
    myCursor.execute(f'SELECT userName FROM userList WHERE LOWER(userName) = LOWER("{username}");')
    userName = myCursor.fetchall()[0][0]
    return str(userName)

@app.route("/getUserList", methods = ['POST'])
def getUserList():
    permissionLevel = request.json['permissionLevel']
    username = request.json['username']
    myCursor = myConnection.cursor()
    if permissionLevel == '2':
        myCursor.execute(f'SELECT * FROM userList ORDER BY userType DESC, username ASC')
    else:
        myCursor.execute(f'SELECT * FROM userList WHERE LOWER(username)=LOWER("{username}")')
    userList = json.dumps(myCursor.fetchall())
    return userList

if __name__ == "__main__":
    app.run(debug=True)


