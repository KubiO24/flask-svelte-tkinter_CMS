import flask
from flask import Flask, send_from_directory, request
import sqlite3
import json
import os

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
    SELECT 'Admin', 'admin', 'admin', 2
    WHERE NOT EXISTS(SELECT 1 FROM userList WHERE LOWER(username) = 'admin');
""")


# themes table
myCursor.execute("""CREATE TABLE IF NOT EXISTS themes (
    preset TEXT,
    mainColor TEXT,
    secondColor TEXT,
    mainBackground TEXT,
    secondBackground TEXT,
    newsBorder TEXT,
    font TEXT,
    selected INT
)""")

# add presets if not exists
myCursor.execute("""
    INSERT INTO themes (preset, mainColor, secondColor, mainBackground, secondBackground, newsBorder, font, selected)
    SELECT 'light', '#000000', '#000000', '#ffffff', '#cccccc', '#444444', 'Arial', 1
    WHERE NOT EXISTS(SELECT 1 FROM themes WHERE preset = 'light');
""")
myCursor.execute("""
    INSERT INTO themes (preset, mainColor, secondColor, mainBackground, secondBackground, newsBorder, font, selected)
    SELECT 'dark', '#ffffff', '#ffffff', '#222222', '#333333', '#111111', 'Arial', 0
    WHERE NOT EXISTS(SELECT 1 FROM themes WHERE preset = 'dark');
""")
myCursor.execute("""
    INSERT INTO themes (preset, mainColor, secondColor, mainBackground, secondBackground, newsBorder, font, selected)
    SELECT 'custom', '#000000', '#000000', '#ffffff', '#ffffff', '#cccccc', 'Arial', 0
    WHERE NOT EXISTS(SELECT 1 FROM themes WHERE preset = 'custom');
""")


# blocks table
myCursor.execute("""CREATE TABLE IF NOT EXISTS blocks (
    name TEXT,
    active TEXT,
    orderIndex INT
)""")

# add themes if not exists
myCursor.execute("""
    INSERT INTO blocks (name, active, orderIndex)
    SELECT 'navbar', 'true', '0'
    WHERE NOT EXISTS(SELECT 1 FROM blocks WHERE name = 'navbar');
""")
myCursor.execute("""
    INSERT INTO blocks (name, active, orderIndex)
    SELECT 'slider', 'true', '1'
    WHERE NOT EXISTS(SELECT 1 FROM blocks WHERE name = 'slider');
""")
myCursor.execute("""
    INSERT INTO blocks (name, active, orderIndex)
    SELECT 'news', 'true', '2'
    WHERE NOT EXISTS(SELECT 1 FROM blocks WHERE name = 'news');
""")
myCursor.execute("""
    INSERT INTO blocks (name, active, orderIndex)
    SELECT 'content', 'true', '3'
    WHERE NOT EXISTS(SELECT 1 FROM blocks WHERE name = 'content');
""")
myCursor.execute("""
    INSERT INTO blocks (name, active, orderIndex)
    SELECT 'footer', 'true', '4'
    WHERE NOT EXISTS(SELECT 1 FROM blocks WHERE name = 'footer');
""")


# news table
myCursor.execute("""CREATE TABLE IF NOT EXISTS news (
    title TEXT,
    description TEXT,
    category TEXT,
    images TEXT
)""")


# menu table
myCursor.execute("""CREATE TABLE IF NOT EXISTS menu (
    text TEXT,
    link TEXT,
    id INTEGER PRIMARY KEY AUTOINCREMENT
)""")


# menu table
myCursor.execute("""CREATE TABLE IF NOT EXISTS menuType (
    type TEXT
)""")
myCursor.execute("""
    INSERT INTO menuType (type)
    SELECT 'horizontal'
    WHERE NOT EXISTS(SELECT 1 FROM menuType);
""")


# footer table
myCursor.execute("""CREATE TABLE IF NOT EXISTS footer (
    text TEXT,
    link TEXT,
    id INTEGER PRIMARY KEY AUTOINCREMENT
)""")

myConnection.commit()


###################################################################################################


def userExist(username):
    myCursor.execute(
        f'SELECT EXISTS(SELECT 1 FROM userList WHERE LOWER(username)=LOWER("{username}"))')
    row = myCursor.fetchall()
    if row[0][0] == 1:
        return True
    return False


def newsTitleExist(title):
    myCursor.execute(
        f'SELECT EXISTS(SELECT 1 FROM news WHERE LOWER(title)=LOWER("{title}"))')
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


@app.route("/register", methods=['POST'])
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


@app.route("/login", methods=['POST'])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]

    myCursor.execute(
        f'SELECT EXISTS(SELECT 1 FROM userList WHERE LOWER(username)=LOWER("{username}") AND password="{password}")')
    row = myCursor.fetchall()
    if (row[0][0] == 1):
        return '1'
    return '0'


@app.route("/getPermission", methods=['POST'])
def getPermission():
    username = request.data.decode("utf-8")
    myCursor = myConnection.cursor()
    myCursor.execute(
        f'SELECT userType FROM userList WHERE LOWER(userName) = LOWER("{username}");')
    permission = myCursor.fetchall()[0][0]
    return str(permission)


@app.route("/getProperUsername", methods=['POST'])
def getProperUsername():
    username = request.data.decode("utf-8")
    myCursor.execute(
        f'SELECT userName FROM userList WHERE LOWER(userName) = LOWER("{username}");')
    userName = myCursor.fetchall()[0][0]
    return str(userName)


@app.route("/getUserList", methods=['POST'])
def getUserList():
    permissionLevel = request.json['permissionLevel']
    username = request.json['username']
    print(username)
    if permissionLevel == '2':
        myCursor.execute(
            f'SELECT * FROM userList ORDER BY userType DESC, username ASC')
    else:
        myCursor.execute(
            f'SELECT * FROM userList WHERE LOWER(username)=LOWER("{username}")')
    userList = json.dumps(myCursor.fetchall())
    return userList


@app.route("/deleteUser", methods=['POST'])
def deleteUser():
    username = request.data.decode("utf-8")
    myCursor.execute(
        f'DELETE FROM userList WHERE LOWER(username)=LOWER("{username}");')
    myConnection.commit()
    return "success"


@app.route("/editUser", methods=['POST'])
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


@app.route("/getPresets", methods=['POST'])
def getPresets():
    myCursor.execute(f'SELECT * FROM themes')
    themes = json.dumps(myCursor.fetchall())
    return themes


@app.route("/savePreset", methods=['POST'])
def savePreset():
    myCursor.execute(f"""
                UPDATE themes 
                SET selected=0
                WHERE selected=1;
            """)
    myConnection.commit()
    selectedPreset = request.json['selectedPreset']
    preset = request.json['preset']
    myCursor.execute(f"""
            UPDATE themes 
            SET mainColor="{preset[0]}", secondColor="{preset[1]}", mainBackground="{preset[2]}" , secondBackground="{preset[3]}", newsBorder="{preset[4]}", font="{preset[5]}", selected=1
            WHERE LOWER(preset)=LOWER("{selectedPreset}");
        """)
    myConnection.commit()
    return 'success'


@app.route("/getBlocks", methods=['POST'])
def getBlocks():
    myCursor.execute(f'SELECT * FROM blocks')
    blocks = json.dumps(myCursor.fetchall())
    return blocks


@app.route("/saveBlocks", methods=['POST'])
def saveBlocks():
    blocks = request.json
    i = 0
    for block in blocks:
        myCursor.execute(f"""
                UPDATE blocks
                SET active="{block['active']}", orderIndex="{i}"
                WHERE LOWER(name)=LOWER("{block['name']}");
            """)
        i += 1
    myConnection.commit()
    return 'success'


@app.route("/getNews", methods=['POST'])
def getNews():
    myCursor.execute(f'SELECT * FROM news')
    news = json.dumps(myCursor.fetchall())
    return news


@app.route("/saveNews", methods=['POST'])
def saveNews():
    news = request.json
    if newsTitleExist(news['title']):
        return {"type": "error", "message": "News title already exists"}

    myCursor.execute(f"""
        INSERT INTO news (title, description, category, images)
        VALUES ('{news['title']}','{news['description']}','{news['category']}','{news['images']}')
    """)
    myConnection.commit()
    return {"type": "success"}


@app.route("/updateNews", methods=['POST'])
def updateNews():
    news = request.json
    if news['title'].lower() == 'title':
        return {"type": "error", "message": "c'mon can't you think about a better title?"}
    if newsTitleExist(news['title']) and news['originalTitle'].lower() != news['title'].lower():
        return {"type": "error", "message": "News title already exists"}
    myCursor.execute(f"""
        UPDATE news 
        SET title="{news['title']}", description="{news['description']}", category="{news['category']}", images="{news['images']}" 
        WHERE LOWER(title)=LOWER("{news['originalTitle']}");
    """)
    myConnection.commit()
    return {"type": "success"}


@app.route("/deleteNews", methods=['POST'])
def deleteNews():
    title = request.data.decode("utf-8")
    myCursor.execute(
        f'DELETE FROM news WHERE LOWER(title)=LOWER("{title}");')
    myConnection.commit()
    return {"type": "success"}


@app.route("/getMenu", methods=['POST'])
def getMenu():
    myCursor.execute(f'SELECT * FROM menu')
    menu = json.dumps(myCursor.fetchall())
    return menu


@app.route("/saveMenu", methods=['POST'])
def saveMenu():
    text = request.json['text']
    link = request.json['link']
    myCursor.execute(f"""
        INSERT INTO menu (text, link)
        VALUES ('{text}','{link}')
    """)
    myConnection.commit()
    myCursor.execute("select seq from sqlite_sequence WHERE name = 'menu'")
    lastId = myCursor.fetchall()
    return {"type": "success", 'message': lastId[0][0]}


@app.route("/updateMenu", methods=['POST'])
def updateMenu():
    menu = request.json
    myCursor.execute(f"""
        UPDATE menu 
        SET text="{menu['text']}", link="{menu['link']}"
        WHERE id={menu['id']};
    """)
    myConnection.commit()
    return {"type": "success"}


@app.route("/deleteMenu", methods=['POST'])
def deleteMenu():
    id = request.data.decode("utf-8")
    myCursor.execute(
        f'DELETE FROM menu WHERE id={id};')
    myConnection.commit()
    return {"type": "success"}


@app.route("/getMenuType", methods=['POST'])
def getMenuType():
    myCursor = myConnection.cursor()
    myCursor.execute(f'SELECT * FROM menuType')
    menu = myCursor.fetchall()
    return menu[0][0]


@app.route("/changeMenuType", methods=['POST'])
def changeMenuType():
    menuType = request.data.decode("utf-8")
    lastType = ''
    if menuType == 'horizontal':
        lastType = 'hamburger'
    else:
        lastType = 'horizontal'

    myCursor.execute(f"""
        UPDATE menuType
        SET type="{menuType}"
        WHERE type="{lastType}";
    """)
    myConnection.commit()
    return {"type": "success"}


@app.route("/getFooter", methods=['POST'])
def getFooter():
    myCursor.execute(f'SELECT * FROM footer')
    footer = json.dumps(myCursor.fetchall())
    return footer


@app.route("/saveFooter", methods=['POST'])
def saveFooter():
    text = request.json['text']
    link = request.json['link']
    myCursor.execute(f"""
        INSERT INTO footer (text, link)
        VALUES ('{text}','{link}')
    """)
    myConnection.commit()
    myCursor.execute("select seq from sqlite_sequence WHERE name = 'footer'")
    lastId = myCursor.fetchall()
    return {"type": "success", 'message': lastId[0][0]}


@app.route("/updateFooter", methods=['POST'])
def updateFooter():
    footer = request.json
    myCursor.execute(f"""
        UPDATE footer 
        SET text="{footer['text']}", link="{footer['link']}"
        WHERE id={footer['id']};
    """)
    myConnection.commit()
    return {"type": "success"}


@app.route("/deleteFooter", methods=['POST'])
def deleteFooter():
    id = request.data.decode("utf-8")
    myCursor.execute(
        f'DELETE FROM footer WHERE id={id};')
    myConnection.commit()
    return {"type": "success"}


@app.route("/getData", methods=['POST'])
def getData():
    nav = {
        "type": "navbar",
        "navbarType": "horizontal",
        "navbarItems": []
    }
    theme = []
    blocks = []
    news = []
    myCursor.execute(f'SELECT * FROM blocks')
    bblocks = myCursor.fetchall()
    for i in bblocks:
        if i[1] == 'true':
            blocks.append(i)
    hV = ()
    isSorted = False
    while isSorted == False:
        isSorted = True
        for i in range(1, len(blocks)-1):
            if blocks[i][2] > blocks[i+1][2]:
                hV = blocks[i]
                blocks[i] = blocks[i+1]
                blocks[i+1] = hV
                isSorted = False
    myCursor.execute(f'SELECT * FROM menuType')
    menuType = myCursor.fetchall()
    nav["navbarType"] = menuType[0][0]
    myCursor.execute(f'SELECT * FROM menu')
    links = myCursor.fetchall()
    for i in links:
        link = {
            "navbarText": i[0],
            "navbarLink": i[1]
        }
        nav["navbarItems"].append(link)

    myCursor.execute(f'SELECT * FROM themes')
    themes = myCursor.fetchall()
    for i in themes:
        if i[7] == 1:
            theme = i

    myCursor.execute(f'SELECT * FROM news')
    newsTab = myCursor.fetchall()

    for idx, i in enumerate(newsTab):
        news.append(
            {
                "newsCategory": i[2],
                "newsTitle": i[0],
                "newsText": i[1],
                "newsPhoto": i[3],
                "newsIndex": idx
            }
        )
    resBlocks = [nav]

    for i in blocks:
        if i[0] == 'slider':
            resBlocks.append(
                {
                    "type": "slider",
                    "sliderDuration": 5000,
                    "sliderColor": "white",
                    "sliderItems": [
                        {
                            "sliderPhoto": "../static/xyz1.jpg",
                            "sliderText": "Teskt1 na sliderze"
                        },
                        {
                            "sliderPhoto": "../static/xyz2.jpg",
                            "sliderText": "Teskt2 na sliderze"
                        },
                        {
                            "sliderPhoto": "../static/xyz2.jpg",
                            "sliderText": "Teskt3 na sliderze"
                        },
                        {
                            "sliderPhoto": "../static/xyz2.jpg",
                            "sliderText": "Teskt4 na sliderze"
                        },
                        {
                            "sliderPhoto": "../static/xyz2.jpg",
                            "sliderText": "Teskt5 na sliderze"
                        }
                    ]
                },
            )
        elif i[0] == 'news':
            resBlocks.append({
                "type": "news",
                "newsItems": news
            },)
        elif i[0] == 'content':
            resBlocks.append({
                "type": "content",
            })
    footerItems = []
    myCursor.execute(f'SELECT * FROM footer')
    footer = myCursor.fetchall()
    for i in footer:
        footerItems.append(
            {
                "text": i[0],
                "link": i[1]
            }
        )

    resBlocks.append(
        {
            "type": "footer",
            "footerItems": footerItems,
            "footerText": "Jakub Kowal - Igor Świerczyński CMS 2022"
        }
    )
    finalJSON = {
        "theme": {
            "mainColor": theme[1],
            "secondColor": theme[2],
            "mainBackground": theme[3],
            "newsBorder": theme[5],
            "secondBackground": theme[4],
            "font": theme[6]
        },
        "blocks": resBlocks
    }
    return finalJSON


@app.route("/saveData", methods=['POST'])
def saveData():
    theme = []
    blocks = []
    myCursor.execute(f'SELECT * FROM blocks')
    bblocks = myCursor.fetchall()
    for i in bblocks:
        if i[1] == 'true':
            blocks.append(i)
    hV = ()
    isSorted = False
    while isSorted == False:
        isSorted = True
        for i in range(1, len(blocks)-1):
            if blocks[i][2] > blocks[i+1][2]:
                hV = blocks[i]
                blocks[i] = blocks[i+1]
                blocks[i+1] = hV
                isSorted = False
    myCursor.execute(f'SELECT * FROM themes')
    themes = myCursor.fetchall()
    for i in themes:
        if i[7] == 1:
            theme = i

    print(blocks, theme, flush=True)

    for i in blocks:
        if i[0] == 'slider':
            print('slider', flush=True)
        elif i[0] == 'news':
            print('news', flush=True)
        elif i[0] == 'content':
            print('content', flush=True)
    finalJSON = {
        "theme": {
            "mainColor": theme[1],
            "secondColor": theme[2],
            "mainBackground": theme[3],
            "newsBorder": theme[4],
            "secondBackground": theme[5],
            "font": "Roboto"
        },
    }

    return 'success'


if __name__ == "__main__":
    app.run(debug=True)
