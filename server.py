import flask
from flask import Flask, send_from_directory, request
import sqlite3
import json

app = Flask(__name__)
myConnection = sqlite3.connect('data.sqlite', check_same_thread=False)

myCursor = myConnection.cursor()

# userList table
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

# themePresets table
myCursor.execute("""CREATE TABLE IF NOT EXISTS themes (
    preset TEXT,
    mainColor TEXT,
    secondColor TEXT,
    mainBackground TEXT,
    secondBackground TEXT,
    newsBorder TEXT,
    font TEXT
)""")

# add light preset if not exists
myCursor.execute("""
    INSERT INTO themes (preset, mainColor, secondColor, mainBackground, secondBackground, newsBorder, font)
    SELECT 'light', '#000000', '#000000', '#ffffff', '#cccccc', '#444444', 'Arial'
    WHERE NOT EXISTS(SELECT 1 FROM themes WHERE preset = 'light');
""")

# add dark preset if not exists
myCursor.execute("""
    INSERT INTO themes (preset, mainColor, secondColor, mainBackground, secondBackground, newsBorder, font)
    SELECT 'dark', '#ffffff', '#ffffff', '#222222', '#333333', '#111111', 'Arial'
    WHERE NOT EXISTS(SELECT 1 FROM themes WHERE preset = 'dark');
""")

# add custom preset if not exists
myCursor.execute("""
    INSERT INTO themes (preset, mainColor, secondColor, mainBackground, secondBackground, newsBorder, font)
    SELECT 'custom', '#000000', '#000000', '#ffffff', '#ffffff', '#cccccc', 'Arial'
    WHERE NOT EXISTS(SELECT 1 FROM themes WHERE preset = 'custom');
""")

myConnection.commit()


###################################################################################################


def userExist(username):
    print(username)
    myCursor.execute(f'SELECT EXISTS(SELECT 1 FROM userList WHERE LOWER(username)=LOWER("{username}"))')
    row = myCursor.fetchall()
    if row[0][0] == 1:
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

    myCursor.execute(f'SELECT EXISTS(SELECT 1 FROM userList WHERE LOWER(username)=LOWER("{username}") AND password="{password}")')
    row = myCursor.fetchall()
    if (row[0][0] == 1):
        return '1'
    return '0'

@app.route("/getPermission", methods = ['POST'])
def getPermission():
    username = request.data.decode("utf-8")
    myCursor.execute(f'SELECT userType FROM userList WHERE LOWER(userName) = LOWER("{username}");')
    permission = myCursor.fetchall()[0][0]
    return str(permission)

@app.route("/getProperUsername", methods = ['POST'])
def getProperUsername():
    username = request.data.decode("utf-8")
    myCursor.execute(f'SELECT userName FROM userList WHERE LOWER(userName) = LOWER("{username}");')
    userName = myCursor.fetchall()[0][0]
    return str(userName)

@app.route("/getUserList", methods = ['POST'])
def getUserList():
    permissionLevel = request.json['permissionLevel']
    username = request.json['username']
    print(username)
    if permissionLevel == '2':
        myCursor.execute(f'SELECT * FROM userList ORDER BY userType DESC, username ASC')
    else:
        myCursor.execute(f'SELECT * FROM userList WHERE LOWER(username)=LOWER("{username}")')
    userList = json.dumps(myCursor.fetchall())
    return userList

@app.route("/deleteUser", methods = ['POST'])
def deleteUser():
    username = request.data.decode("utf-8")
    myCursor.execute(f'DELETE FROM userList WHERE LOWER(username)=LOWER("{username}");')
    myConnection.commit()
    print(username)
    return "success"

@app.route("/editUser", methods = ['POST'])
def editUser():
    print('editUser')
    originalUsername = request.json['originalUsername']
    username = str(request.json['username'])
    email = request.json['email']
    password = request.json['password']
    permissionLevel = str(request.json['permissionLevel'])

    if originalUsername.lower() != username.lower():
        if userExist(username):
            return {'type': "error", 'message': "This username is already taken"}

    print(permissionLevel)
    if permissionLevel != '0' and permissionLevel != '1' and permissionLevel != '2':
        return {'type': "error", 'message': "Wrong permission level"}

    myCursor.execute(f"""
        UPDATE userList 
        SET username="{username}", email="{email}", password="{password}", userType="{permissionLevel}" 
        WHERE LOWER(username)=LOWER("{originalUsername}");
    """)
    myConnection.commit()
    return {'type': "success", 'message': "msg"}

@app.route("/getPresets", methods = ['POST'])
def getPresets():
    print('getPresets')
    myCursor.execute(f'SELECT * FROM themes')
    themes = json.dumps(myCursor.fetchall())
    return themes

@app.route("/savePreset", methods = ['POST'])
def savePreset():
    selectedPreset = request.json['selectedPreset']
    preset = request.json['preset']
    print(preset[0])
    myCursor.execute(f"""
            UPDATE themes 
            SET mainColor="{preset[0]}", secondColor="{preset[1]}", mainBackground="{preset[2]}" , secondBackground="{preset[3]}", newsBorder="{preset[4]}", font="{preset[5]}"
            WHERE LOWER(preset)=LOWER("{selectedPreset}");
        """)
    myConnection.commit()
    return 'success'

if __name__ == "__main__":
    app.run(debug=True)


