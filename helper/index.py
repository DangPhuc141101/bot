import json
from constant.index import*

def readData():
    with open("dataBase.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    users = jsonObject['users']
    return users

def findUserById(id):
    with open("dataBase.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    users = jsonObject['users']
    for i in range(len(users)):
        if users[i]['id_tele'] == id:
            return i
    return -1

def getUserById(id):
    with open("dataBase.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    users = jsonObject['users']
    index=-1
    for i in range(len(users)):
        if users[i]['id_tele'] == id:
            index=i
    return users[index]

def createUser(id):
    users = readData()
    users.append({
        "id_tele": id,
        "totalTrue": 0,
        "totalQuestion": 0,
        "type_question": 27,
        "difficulty": "multiple",
        "correct_answer":"A"
    })

    with open('dataBase.json', 'w') as jsonFile:
        json.dump({'users':users}, jsonFile)
        jsonFile.close()


def getCorrectAnswerById(id):
    users = readData()
    indexUser = -1
    
    for i in range(len(users)):
        if users[i]['id_tele'] == id:
            indexUser = i

     # chỉnh sửa user
    if(indexUser != -1):
        return users[indexUser]['correct_answer']

def editCorrectAnswerById(id,correctAnswer ):
    users = readData()
    indexUser = -1
    
    for i in range(len(users)):
        if users[i]['id_tele'] == id:
            indexUser = i

     # chỉnh sửa user
    if(indexUser != -1):
         users[indexUser]['correct_answer']=correctAnswer
         
    with open('dataBase.json', 'w') as jsonFile:
        json.dump({'users':users}, jsonFile)
        jsonFile.close()

def editTypeAddDifficulty(id, type='' , difficulty=''):
     users = readData()
     indexUser = -1
    
     for i in range(len(users)):
        if users[i]['id_tele'] == id:
            indexUser = i
     # chỉnh sửa user
     if(indexUser != -1):
         if(type!=''):
             users[indexUser]['type_question']=type
         if(difficulty!=''):
             users[indexUser]['difficulty']=difficulty


     with open('dataBase.json', 'w') as jsonFile:
        json.dump({'users': users}, jsonFile)
        jsonFile.close()

def editTotalQuestion(id , answer ):
    users = readData()
    # tìm user by index
    indexUser = -1
    
    for i in range(len(users)):
        if users[i]['id_tele'] == id:
            indexUser = i

     # chỉnh sửa user
    if(indexUser != -1):
        if(answer):
            users[indexUser]['totalTrue'] = users[indexUser]['totalTrue']+1
  
        users[indexUser]['totalQuestion'] = users[indexUser]['totalQuestion']+1

    # ghi file lại
    with open('dataBase.json', 'w') as jsonFile:
        json.dump({'users':users}, jsonFile)
        jsonFile.close()

def index_corect(answers, corect_answer):
    for i in range(0, len(answers)):
        if answers[i] == corect_answer:
            return i
    return 0

def makeAnewUrlQuestion(typeOfQuestion , difficulty):
    #original url
    baseUrl = 'https://opentdb.com/api.php?amount=1&type=multiple'
    newUrl = ''
    newUrl = baseUrl + '&category=' + str(typeOfQuestion) + '&difficulty=' + str(difficulty)
    return newUrl

def getInformationById(id):
    users = readData()
    indexUser = -1
    
    for i in range(len(users)):
        if users[i]['id_tele'] == id:
            return users[i]

def findTypeOfQuestion(type):
    for i in typeOfQuestion:
        if int(i['value'])==int(type):
            return i['text']
     
