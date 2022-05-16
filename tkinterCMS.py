from tkinter import *
from tkinter import filedialog
import sqlite3
import base64

myConnection = sqlite3.connect('data.sqlite')

loginWindow = Tk()
loginWindow.title("Login")
loginWindow.geometry("280x160")
loginWindow.resizable(0, 0)

username = StringVar()
password = StringVar()

Label(loginWindow, text="Username:", fg='#FF4B2B').grid(column=0, row=0, sticky=W, padx=20, pady=10)
Entry(loginWindow, textvariable=username, fg='#FF4B2B').grid(column=1, row=0, sticky=E, padx=20, pady=10)
Label(loginWindow, text="Password:", fg='#FF4B2B').grid(column=0, row=1, sticky=W, padx=20, pady=10)
Entry(loginWindow, textvariable=password, show="*", fg='#FF4B2B').grid(column=1, row=1, sticky=E, padx=20, pady=10)
Button(loginWindow, text="Login", bg='#FF4B2B', fg='white', command=lambda: login(username.get(), password.get())).grid(column=1, row=2, sticky=W, padx=20, pady=5)

def login(username, password):
    global loginWindow, settingsWindow

    if username == "" or password == "":
        return

    userList = getUserList()
    adminLoginned = False
    for user in userList:
        if user[0].lower() == username.lower() and user[2] == password and user[3] == 2:
            adminLoginned = True
    if adminLoginned:
        loginWindow.destroy()
        settingsWindow = Tk()
        settingsWindow.title("Settings")
        settingsWindow.geometry("1150x100")

        Button(settingsWindow, text="Menu", bg='#FF4B2B', fg='white', command=lambda: showMenu(), width=20).grid(column=0, row=0, padx=20, pady=20)
        Button(settingsWindow, text="Slider", bg='#FF4B2B', fg='white', command=lambda: showSlider(), width=20).grid(column=1, row=0, padx=20, pady=20)
        Button(settingsWindow, text="News", bg='#FF4B2B', fg='white', command=lambda: showNews(), width=20).grid(column=2, row=0, padx=20, pady=20)
        Button(settingsWindow, text="Content", bg='#FF4B2B', fg='white', command=lambda: showContent(), width=20).grid(column=3, row=0, padx=20, pady=20)
        Button(settingsWindow, text="Footer", bg='#FF4B2B', fg='white', command=lambda: showFooter(), width=20).grid(column=4, row=0, padx=20, pady=20)
        Button(settingsWindow, text="Users", bg='#FF4B2B', fg='white', command=lambda: showUsers(), width=20).grid(column=5, row=0, padx=20, pady=20)

        settingsWindow.mainloop()
    else:
        Label(loginWindow, text="Wrong username or password for admin account", fg='red').grid(column=0, columnspan=2, row=3, padx=5)

#############################################################################################################################################################################

def clearGrid():
    global settingsWindow
    for element in settingsWindow.grid_slaves():
        if int(element.grid_info()["row"]) > 0:
            element.grid_forget()

def getMenu():
    myCursor = myConnection.cursor()
    myCursor.execute(f'SELECT * FROM menu')
    records = myCursor.fetchall()
    return records

def getSlider():
    myCursor = myConnection.cursor()
    myCursor.execute(f'SELECT * FROM slider')
    records = myCursor.fetchall()
    return records

def getSliderDuration():
    myCursor = myConnection.cursor()
    myCursor.execute(f'SELECT * FROM sliderDuration')
    records = myCursor.fetchall()
    return records

def getNews():
    myCursor = myConnection.cursor()
    myCursor.execute(f'SELECT * FROM news')
    records = myCursor.fetchall()
    return records

def getContent():
    myCursor = myConnection.cursor()
    myCursor.execute(f'SELECT * FROM content')
    records = myCursor.fetchall()
    return records

def getUserList():
    myCursor = myConnection.cursor()
    myCursor.execute(f'SELECT * FROM userList')
    records = myCursor.fetchall()
    return records

def getFooter():
    myCursor = myConnection.cursor()
    myCursor.execute(f'SELECT * FROM footer')
    records = myCursor.fetchall()
    return records

#############################################################################################################################################################################

def showMenu():
    global settingsWindow
    settingsWindow.geometry("1150x400")
    generateMenuList('', False)

def generateMenuList(editingId, editing):
    global textMenuEntry, linkMenuEntry

    clearGrid()

    Label(settingsWindow, text="Text", font='Arial 12 bold').grid(column=0, row=1, padx=10, pady=10)
    Label(settingsWindow, text="Link", font='Arial 12 bold').grid(column=1, row=1, padx=10, pady=10)
    menuList = getMenu()

    i = 0
    for index, menu in enumerate(menuList):
        if menu[2] == editingId and editing == True:
            textMenuEntry = Entry(settingsWindow, width=15)
            textMenuEntry.grid(column=0, row=index + 2, padx=10, pady=10)
            textMenuEntry.insert(0, str(menu[0]))

            linkMenuEntry = Entry(settingsWindow, width=15)
            linkMenuEntry.grid(column=1, row=index + 2, padx=10, pady=10)
            linkMenuEntry.insert(0, str(menu[1]))

            generateMenuSaveButton(menu[2], index)
            Button(settingsWindow, text="Discard", command=discardMenuChanges).grid(column=5, row=index + 2, padx=10, pady=10)
        else:
            Label(settingsWindow, text=str(menu[0])).grid(column=0, row=index + 2, padx=10, pady=10)
            Label(settingsWindow, text=str(menu[1])).grid(column=1, row=index + 2, padx=10, pady=10)

            generateMenuEditButton(menu[2], editing, index)
            generateMenuDeleteButton(menu[2], index)
        i = index
    Button(settingsWindow, text="Add Menu", command=addMenu).grid(column=2, columnspan=2, row=i + 3, padx=10, pady=10)

def generateMenuEditButton(id, editing, index):
    if editing:
        Button(settingsWindow, text="Edit", command=lambda: editMenu(id), state=DISABLED).grid(column=4, row=index + 2, padx=10, pady=10)
    else:
        Button(settingsWindow, text="Edit", command=lambda: editMenu(id)).grid(column=4, row=index + 2, padx=10, pady=10)

def generateMenuSaveButton(id, index):
    Button(settingsWindow, text="Save", command=lambda: saveMenu(id)).grid(column=4, row=index + 2, padx=10, pady=10)

def generateMenuDeleteButton(id, index):
    Button(settingsWindow, text="Delete", command=lambda: deleteMenu(id)).grid(column=5, row=index + 2, padx=10, pady=10)

def editMenu(id):
    generateMenuList(id, True)

def saveMenu(id):
    global textMenuEntry, linkMenuEntry
    if textMenuEntry.get() == '' or linkMenuEntry.get() == '':
        return

    myCursor = myConnection.cursor()
    myCursor.execute(f"""
            UPDATE menu 
            SET text="{str(textMenuEntry.get())}", link="{str(linkMenuEntry.get())}"
            WHERE id={id};
        """)
    myConnection.commit()
    generateMenuList('', False)

def discardMenuChanges():
    generateMenuList('', False)

def addMenu():
    myCursor = myConnection.cursor()
    myCursor.execute(f"""
            INSERT INTO menu (text, link)
            VALUES ('link','/#/')
        """)
    myConnection.commit()
    generateMenuList('', False)

def deleteMenu(id):
    myCursor = myConnection.cursor()
    myCursor.execute(f'DELETE FROM menu WHERE id={id}')
    myConnection.commit()
    generateMenuList('', False)

#############################################################################################################################################################################

def showSlider():
    global settingsWindow, sliderIndex
    settingsWindow.geometry("1150x350")
    sliderIndex = 0
    generateSlider()

def fixSlider(slider):
    for slide in slider:
        myCursor = myConnection.cursor()
        myCursor.execute(f"""
                UPDATE slider 
                SET orderIndex="{slide[2]}"
                WHERE id={slide[3]};
            """)
        myConnection.commit()

def generateSlider():
    global sliderDurationEntry, sliderTextEntry, sliderBase64Image, sliderIndex, sliderId, sliderMaxIndex

    clearGrid()

    sliderPrimal = getSlider()
    if len(sliderPrimal) == 0:
        Button(settingsWindow, text="Add Slide", command=addSlide).grid(column=2, columnspan=2, row=1, padx=10, pady=10)
        sliderMaxIndex = -1
        return
    sliderPrimal.sort(key=lambda x: int(x[2]))
    slider = []
    lastIndex = 0
    for slide in sliderPrimal:
        slide = list(slide)
        if int(slide[2]) > lastIndex:
            slider.append([slide[0], slide[1], lastIndex, slide[3]])
        else:
            slider.append([slide[0], slide[1], slide[2], slide[3]])
        lastIndex += 1

    fixSlider(slider)
    sliderMaxIndex = slider[-1][2]
    for slide in slider:
        if str(slide[2]) == str(sliderIndex):
            slider = slide
            break

    sliderBase64Image = slider[1]
    sliderId = slider[3]

    sliderDuration = getSliderDuration()[0][0]

    Label(settingsWindow, text="Slider duration:").grid(column=2, row=2, padx=10, pady=10)
    sliderDurationEntry = Entry(settingsWindow, width=15)
    sliderDurationEntry.grid(column=3, row=2, padx=10, pady=10)
    sliderDurationEntry.insert(0, str(sliderDuration))

    Label(settingsWindow, text='Text').grid(column=2, row=3, padx=10, pady=10)
    sliderTextEntry = Entry(settingsWindow, width=15)
    sliderTextEntry.grid(column=3, row=3, padx=10, pady=10)
    sliderTextEntry.insert(0, str(slider[0]))

    Button(settingsWindow, text="Change Slider Image", command=changeSliderImage).grid(column=2, columnspan=2, row=4, padx=10, pady=10)

    Button(settingsWindow, text="Index --", command=sliderIndexMinus).grid(column=1, row=5, padx=10, pady=10)
    Label(settingsWindow, text=f'Index: {sliderIndex}').grid(column=2, columnspan=2, row=5, padx=10, pady=10)
    Button(settingsWindow, text="Index ++", command=sliderIndexPlus).grid(column=4, row=5, padx=10, pady=10)

    Button(settingsWindow, text="Previous Slide", command=previousSlide).grid(column=1, row=6, padx=10, pady=10)
    Button(settingsWindow, text="Save", command=saveSlider).grid(column=2, columnspan=2, row=6, padx=10, pady=10)
    Button(settingsWindow, text="Next Slide", command=nextSlide).grid(column=4, row=6, padx=10, pady=10)

    Button(settingsWindow, text="Delete This Slide", command=deleteSlide).grid(column=2, row=7, padx=10, pady=10)
    Button(settingsWindow, text="Add Slide", command=addSlide).grid(column=3, row=7, padx=10, pady=10)

def changeSliderImage():
    global sliderBase64Image
    filename = filedialog.askopenfilename(filetypes=[('Pictures', '*.jpg *.png')])
    if filename == '':
        return
    img = open(filename, 'rb')
    base64image = base64.b64encode(img.read()).decode('ascii')
    sliderBase64Image = 'data:image/png;base64,{}'.format(base64image)

def sliderIndexMinus():
    global sliderIndex

    if sliderIndex == 0:
        return
    myCursor = myConnection.cursor()
    myCursor.execute(f"""
            UPDATE slider 
            SET orderIndex="{-1}"
            WHERE orderIndex="{sliderIndex}";
        """)
    myCursor = myConnection.cursor()
    myCursor.execute(f"""
            UPDATE slider 
            SET orderIndex="{sliderIndex}"
            WHERE orderIndex="{sliderIndex-1}";
        """)
    myCursor = myConnection.cursor()
    myCursor.execute(f"""
                UPDATE slider 
                SET orderIndex="{sliderIndex-1}"
                WHERE orderIndex="{-1}";
            """)
    myConnection.commit()
    sliderIndex -= 1
    generateSlider()

def sliderIndexPlus():
    global sliderIndex

    sliderLen = len(getSlider())
    if sliderIndex == sliderLen - 1:
        return
    myCursor = myConnection.cursor()
    myCursor.execute(f"""
                UPDATE slider 
                SET orderIndex="{-1}"
                WHERE orderIndex="{sliderIndex}";
            """)
    myCursor = myConnection.cursor()
    myCursor.execute(f"""
                UPDATE slider 
                SET orderIndex="{sliderIndex}"
                WHERE orderIndex="{sliderIndex + 1}";
            """)
    myCursor = myConnection.cursor()
    myCursor.execute(f"""
                    UPDATE slider 
                    SET orderIndex="{sliderIndex + 1}"
                    WHERE orderIndex="{-1}";
                """)
    myConnection.commit()
    sliderIndex += 1
    generateSlider()

def previousSlide():
    global sliderIndex
    if sliderIndex > 0:
        sliderIndex -= 1
    generateSlider()

def nextSlide():
    global sliderIndex
    sliderLen = len(getSlider())
    if sliderIndex < sliderLen-1:
        sliderIndex += 1
    generateSlider()

def saveSlider():
    global sliderDurationEntry, sliderTextEntry, sliderBase64Image, sliderId

    if sliderDurationEntry.get() == '':
        return
    if not sliderDurationEntry.get().isdigit():
        return
    myCursor = myConnection.cursor()
    myCursor.execute(f"""
            UPDATE sliderDuration
            SET duration="{sliderDurationEntry.get()}";
        """)
    myConnection.commit()

    if sliderTextEntry.get() == '' or sliderBase64Image == '':
        return
    myCursor = myConnection.cursor()
    myCursor.execute(f"""
            UPDATE slider 
            SET text="{sliderTextEntry.get()}", image="{sliderBase64Image}"
            WHERE id={sliderId};
        """)
    myConnection.commit()

def addSlide():
    global sliderMaxIndex, sliderIndex
    myCursor = myConnection.cursor()
    myCursor.execute(f"""
           INSERT INTO slider (text, image, orderIndex)
           VALUES ('','data:image/png;base64,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', '{str(int(sliderMaxIndex)+1)}')
       """)
    myConnection.commit()
    sliderIndex = int(sliderMaxIndex) + 1
    generateSlider()

def deleteSlide():
    global sliderId, sliderIndex
    myCursor = myConnection.cursor()
    myCursor.execute(
        f'DELETE FROM slider WHERE id={sliderId};')
    myConnection.commit()
    sliderIndex = 0
    generateSlider()

#############################################################################################################################################################################

def showNews():
    global settingsWindow, newsIndex
    settingsWindow.geometry("1150x350")
    newsIndex = 0
    generateNews()

def generateNews():
    global newsTitleEntry, newsDescriptionEntry, newsCategoryEntry, newsBase64Image, ogNewsBase64Image, newsId, newsIndex, maxNewsIndex

    clearGrid()

    news = getNews()

    if len(news) == 0:
        Button(settingsWindow, text="Add News", command=addNews).grid(column=2, columnspan=2, row=2, padx=10, pady=10)
        maxNewsIndex = -1
        return

    maxNewsIndex = len(news)-1
    news = news[newsIndex]

    newsBase64Image = news[3]
    ogNewsBase64Image = news[3]
    newsId = news[4]

    Label(settingsWindow, text='Title').grid(column=2, row=2, padx=10, pady=10)
    newsTitleEntry = Entry(settingsWindow, width=15)
    newsTitleEntry.grid(column=3, row=2, padx=10, pady=10)
    newsTitleEntry.insert(0, str(news[0]))

    Label(settingsWindow, text='Description').grid(column=2, row=3, padx=10, pady=10)
    newsDescriptionEntry = Entry(settingsWindow, width=15)
    newsDescriptionEntry.grid(column=3, row=3, padx=10, pady=10)
    newsDescriptionEntry.insert(0, str(news[1]))

    Label(settingsWindow, text='Category').grid(column=2, row=4, padx=10, pady=10)
    newsCategoryEntry = Entry(settingsWindow, width=15)
    newsCategoryEntry.grid(column=3, row=4, padx=10, pady=10)
    newsCategoryEntry.insert(0, str(news[2]))

    Button(settingsWindow, text="Add News Image", command=addNewsImage).grid(column=2, columnspan=2, row=5, padx=10, pady=10)

    Button(settingsWindow, text="Previous News", command=previousNews).grid(column=1, row=6, padx=10, pady=10)
    Button(settingsWindow, text="Save", command=saveNews).grid(column=2, columnspan=2, row=6, padx=10, pady=10)
    Button(settingsWindow, text="Next News", command=nextNews).grid(column=4, row=6, padx=10, pady=10)

    Button(settingsWindow, text="Delete This News", command=deleteNews).grid(column=2, row=7, padx=10, pady=10)
    Button(settingsWindow, text="Add News", command=addNews).grid(column=3, row=7, padx=10, pady=10)

def addNews():
    global newsIndex, maxNewsIndex
    myCursor = myConnection.cursor()
    myCursor.execute(f"""
            INSERT INTO news (title, description, category, images)
            VALUES ('','','','data:image/png;base64,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')
        """)
    myConnection.commit()
    newsIndex = maxNewsIndex + 1
    generateNews()

def previousNews():
    global newsIndex
    if newsIndex > 0:
        newsIndex -= 1
    generateNews()

def nextNews():
    global newsIndex
    newsLen = len(getNews())
    if newsIndex < newsLen-1:
        newsIndex += 1
    generateNews()

def addNewsImage():
    global newsBase64Image
    filename = filedialog.askopenfilename(filetypes=[('Pictures', '*.jpg *.png')])
    if filename == '':
        return
    img = open(filename, 'rb')
    base64image = base64.b64encode(img.read()).decode('ascii')
    newsBase64Image = 'data:image/png;base64,{}'.format(base64image)

def saveNews():
    global newsTitleEntry, newsDescriptionEntry, newsCategoryEntry, newsBase64Image, ogNewsBase64Image, newsId

    if newsTitleEntry.get() == '' or newsDescriptionEntry.get() == '' or newsCategoryEntry.get() == '':
        return

    if ogNewsBase64Image == 'data:image/png;base64,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' and newsBase64Image != '':
        ogNewsBase64Image = ''

    if ogNewsBase64Image == newsBase64Image:
        ogNewsBase64Image = ''

    if ogNewsBase64Image != '' and newsBase64Image != '':
        ogNewsBase64Image += '.'

    myCursor = myConnection.cursor()
    myCursor.execute(f"""
            UPDATE news 
            SET title="{newsTitleEntry.get()}", description="{newsDescriptionEntry.get()}", category="{newsCategoryEntry.get()}", images="{ogNewsBase64Image + newsBase64Image}" 
            WHERE id={int(newsId)};
        """)

    ogNewsBase64Image = ogNewsBase64Image + newsBase64Image
    newsBase64Image = ''
    myConnection.commit()

def deleteNews():
    global newsIndex
    myCursor = myConnection.cursor()
    myCursor.execute(
        f'DELETE FROM news WHERE id={int(newsId)};')
    myConnection.commit()
    newsIndex = 0
    generateNews()

#############################################################################################################################################################################

def showContent():
    global settingsWindow
    settingsWindow.geometry("1150x250")
    generateContent()

def generateContent():
    global contentTitleEntry, contentDescriptionEntry, contentBase64Image
    clearGrid()

    content = getContent()[0]
    contentBase64Image = content[2]

    Label(settingsWindow, text='Title').grid(column=2, row=2, padx=10, pady=10)
    contentTitleEntry = Entry(settingsWindow, width=15)
    contentTitleEntry.grid(column=3, row=2, padx=10, pady=10)
    contentTitleEntry.insert(0, str(content[0]))

    Label(settingsWindow, text='Description').grid(column=2, row=3, padx=10, pady=10)
    contentDescriptionEntry = Entry(settingsWindow, width=15)
    contentDescriptionEntry.grid(column=3, row=3, padx=10, pady=10)
    contentDescriptionEntry.insert(0, str(content[1]))

    Button(settingsWindow, text="Change Content Image", command=changeContentImage).grid(column=2, columnspan=2, row=5, padx=10, pady=10)

    Button(settingsWindow, text="Save", command=saveContent).grid(column=2, columnspan=2, row=6, padx=10, pady=10)


def changeContentImage():
    global contentBase64Image
    filename = filedialog.askopenfilename(filetypes=[('Pictures', '*.jpg *.png')])
    if filename == '':
        return
    img = open(filename, 'rb')
    base64image = base64.b64encode(img.read()).decode('ascii')
    contentBase64Image = 'data:image/png;base64,{}'.format(base64image)

def saveContent():
    global contentTitleEntry, contentDescriptionEntry, contentBase64Image

    if contentTitleEntry.get() == '' or contentDescriptionEntry.get() == '' or contentBase64Image == '':
        return

    myCursor = myConnection.cursor()
    myCursor.execute(f"""
            UPDATE content 
            SET title="{contentTitleEntry.get()}", description="{contentDescriptionEntry.get()}", image="{contentBase64Image}"
        """)
    myConnection.commit()

#############################################################################################################################################################################

def showFooter():
    global settingsWindow
    settingsWindow.geometry("1150x400")
    generateFooterList('', False)

def generateFooterList(editingId, editing):
    global textFooterEntry, linkFooterEntry

    clearGrid()

    Label(settingsWindow, text="Text", font='Arial 12 bold').grid(column=0, row=1, padx=10, pady=10)
    Label(settingsWindow, text="Link", font='Arial 12 bold').grid(column=1, row=1, padx=10, pady=10)
    footerList = getFooter()

    i = 0
    for index, footer in enumerate(footerList):
        if footer[2] == editingId and editing == True:
            textFooterEntry = Entry(settingsWindow, width=15)
            textFooterEntry.grid(column=0, row=index + 2, padx=10, pady=10)
            textFooterEntry.insert(0, str(footer[0]))

            linkFooterEntry = Entry(settingsWindow, width=15)
            linkFooterEntry.grid(column=1, row=index + 2, padx=10, pady=10)
            linkFooterEntry.insert(0, str(footer[1]))

            generateFooterSaveButton(footer[2], index)
            Button(settingsWindow, text="Discard", command=discardFooterChanges).grid(column=5, row=index + 2, padx=10, pady=10)
        else:
            Label(settingsWindow, text=str(footer[0])).grid(column=0, row=index + 2, padx=10, pady=10)
            Label(settingsWindow, text=str(footer[1])).grid(column=1, row=index + 2, padx=10, pady=10)

            generateFooterEditButton(footer[2], editing, index)
            generateFooterDeleteButton(footer[2], index)
        i = index
    Button(settingsWindow, text="Add Footer", command=addFooter).grid(column=2, columnspan=2, row=i + 3, padx=10, pady=10)

def generateFooterEditButton(id, editing, index):
    if editing:
        Button(settingsWindow, text="Edit", command=lambda: editFooter(id), state=DISABLED).grid(column=4, row=index + 2, padx=10, pady=10)
    else:
        Button(settingsWindow, text="Edit", command=lambda: editFooter(id)).grid(column=4, row=index + 2, padx=10, pady=10)

def generateFooterSaveButton(id, index):
    Button(settingsWindow, text="Save", command=lambda: saveFooter(id)).grid(column=4, row=index + 2, padx=10, pady=10)

def generateFooterDeleteButton(id, index):
    Button(settingsWindow, text="Delete", command=lambda: deleteFooter(id)).grid(column=5, row=index + 2, padx=10, pady=10)

def editFooter(id):
    generateFooterList(id, True)

def saveFooter(id):
    global textFooterEntry, linkFooterEntry
    if textFooterEntry.get() == '' or linkFooterEntry.get() == '':
        return

    myCursor = myConnection.cursor()
    myCursor.execute(f"""
            UPDATE footer 
            SET text="{str(textFooterEntry.get())}", link="{str(linkFooterEntry.get())}"
            WHERE id={id};
        """)
    myConnection.commit()
    generateFooterList('', False)

def discardFooterChanges():
    generateFooterList('', False)

def addFooter():
    myCursor = myConnection.cursor()
    myCursor.execute(f"""
            INSERT INTO footer (text, link)
            VALUES ('link','/#/')
        """)
    myConnection.commit()
    generateFooterList('', False)

def deleteFooter(id):
    myCursor = myConnection.cursor()
    myCursor.execute(f'DELETE FROM footer WHERE id={id}')
    myConnection.commit()
    generateFooterList('', False)

#############################################################################################################################################################################

def showUsers():
    global settingsWindow
    settingsWindow.geometry("1150x600")
    generateUserList('', False)

def generateUserList(editingUsername, editing):
    global usernameEntry, emailEntry, passwordEntry, permissionEntry

    clearGrid()

    Label(settingsWindow, text="Username", font='Arial 12 bold').grid(column=0, row=1, padx=10, pady=10)
    Label(settingsWindow, text="Email", font='Arial 12 bold').grid(column=1, row=1, padx=10, pady=10)
    Label(settingsWindow, text="Password", font='Arial 12 bold').grid(column=2, row=1, padx=10, pady=10)
    Label(settingsWindow, text="Permission", font='Arial 12 bold').grid(column=3, row=1, padx=10, pady=10)
    userList = getUserList()

    for index, user in enumerate(userList):
        if user[0].lower() == editingUsername.lower() and editing == True:
            usernameEntry = Entry(settingsWindow, width=15)
            usernameEntry.grid(column=0, row=index + 2, padx=10, pady=10)
            usernameEntry.insert(0, str(user[0]))

            emailEntry = Entry(settingsWindow, width=15)
            emailEntry.grid(column=1, row=index + 2, padx=10, pady=10)
            emailEntry.insert(0, str(user[1]))

            passwordEntry = Entry(settingsWindow, width=15)
            passwordEntry.grid(column=2, row=index + 2, padx=10, pady=10)
            passwordEntry.insert(0, str(user[2]))

            permissionEntry = Entry(settingsWindow, width=15)
            permissionEntry.grid(column=3, row=index + 2, padx=10, pady=10)
            permissionEntry.insert(0, str(user[3]))

            generateSaveButton(user[0], index)
            Button(settingsWindow, text="Discard", command=discardChanges).grid(column=5, row=index + 2, padx=10, pady=10)
        else:
            Label(settingsWindow, text=str(user[0])).grid(column=0, row=index + 2, padx=10, pady=10)
            Label(settingsWindow, text=str(user[1])).grid(column=1, row=index + 2, padx=10, pady=10)
            Label(settingsWindow, text=str(user[2])).grid(column=2, row=index + 2, padx=10, pady=10)
            Label(settingsWindow, text=str(user[3])).grid(column=3, row=index + 2, padx=10, pady=10)

            generateEditButton(user[0], editing, index)
            generateDeleteButton(user[0], index)

def generateEditButton(username, editing, index):
    if editing:
        Button(settingsWindow, text="Edit", command=lambda: editUser(username), state=DISABLED).grid(column=4, row=index + 2, padx=10, pady=10)
    else:
        Button(settingsWindow, text="Edit", command=lambda: editUser(username)).grid(column=4, row=index + 2, padx=10, pady=10)

def generateSaveButton(username, index):
    Button(settingsWindow, text="Save", command=lambda: saveUserChanges(username)).grid(column=4, row=index + 2, padx=10, pady=10)

def generateDeleteButton(username, index):
    Button(settingsWindow, text="Delete", command=lambda: deleteUser(username)).grid(column=5, row=index + 2, padx=10, pady=10)

def editUser(username):
    generateUserList(username, True)

def saveUserChanges(username):
    global usernameEntry, emailEntry, passwordEntry, permissionEntry
    if usernameEntry.get() == '' or emailEntry.get() == '' or passwordEntry.get() == '' or permissionEntry.get() == '':
        return
    if permissionEntry.get() != '0' and permissionEntry.get() != '1' and permissionEntry.get() != '2':
        return

    myCursor = myConnection.cursor()
    myCursor.execute(f"""
            UPDATE userList 
            SET username="{usernameEntry.get()}", email="{emailEntry.get()}", password="{passwordEntry.get()}", userType="{permissionEntry.get()}" 
            WHERE LOWER(username)=LOWER("{username}");
        """)
    myConnection.commit()
    generateUserList('', False)

def discardChanges():
    generateUserList('', False)

def deleteUser(username):
    myCursor = myConnection.cursor()
    myCursor.execute('DELETE FROM userList WHERE LOWER(username)=LOWER("' + str(username) + '")')
    myConnection.commit()
    generateUserList('', False)


loginWindow.mainloop()