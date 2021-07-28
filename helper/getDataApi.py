import requests
import random
def getDatFormApiLink(url):
    response = requests.request("GET", url )
    listQuestion=response.json()
    print("list" ,listQuestion['results'][0])
    return listQuestion['results'][0]

def format_text(str):
    literal_double = ["&quot;", "&rdquo;"]          # Elements in list are  " in html
    for key in literal_double:
        str = str.replace(key, '"')
    literal_single = ["&#039;", "&rsquo;"]          # Elements in list are  ' in html
    for key in literal_single:
        str = str.replace(key, "'")
    return str

def GetQuestion( url ):
    listQuestion =getDatFormApiLink(url)
    question = listQuestion
    listAnswer = question['incorrect_answers']
    listAnswer.append(question['correct_answer'])
    random.shuffle(listAnswer)

    # format text answer
    for ans in listAnswer:
        ans= format_text(str(ans))

    return {
        'category':question['category'],
        'typeQuestion':question['difficulty'],
        'question' : format_text(str(question['question'])),
        'correct_answer': question['correct_answer'], 
        'listAnswer' : listAnswer,
    }

#GetQuestion('https://opentdb.com/api.php?amount=1&category=9&type=multiple')


