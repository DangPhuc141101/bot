from main import*
import logging
from  helper.Index_correct import*
from helper.getDataApi import*
from helper.index import*
from constant.index import*
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (

    ConversationHandler,
    CallbackContext,
    CallbackQueryHandler
)


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)



def start(update: Update, context: CallbackContext) -> int:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)

    teleId=user.id
    checkUser=findUserById(teleId)
    if(checkUser==-1):
        createUser(teleId)


    keyboard = [
        [
            InlineKeyboardButton("choose level", callback_data=str(ONE)),
            InlineKeyboardButton("choose type of question", callback_data=str(TWO)),
        ],
        [ 
            InlineKeyboardButton("Start now", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    Uname=update.message.chat.last_name
    update.message.reply_text("🌈🌈🌈Welcome "+Uname+" to english bot🌈🌈🌈"\
        +"\n✨ /help to show instruction"\
        +"\n🎫 /info to show test information",reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST

# def start1(update: Update, context: CallbackContext) -> int:
#     CallbackQueryHandler(startNow)
#     print("something")
    

def startNow(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    teleId=query['message']['chat']['id'] 
    
    dataUser= getUserById(teleId)

    url =makeAnewUrlQuestion(dataUser['type_question'] , dataUser['difficulty'])
    print("this is url", url)
    question = GetQuestion(url)
    global index_corect_answer_previous
    index_corect_answer_previous = index_corect(question['listAnswer'], question['correct_answer'])
    keyboard = [
        [
            InlineKeyboardButton("A) " + question['listAnswer'][0], callback_data=str(ONE)),
            InlineKeyboardButton("B)" + question['listAnswer'][1], callback_data=str(TWO)),

        ],
        [
            InlineKeyboardButton("C)" + question['listAnswer'][2], callback_data=str(THREE)),
            InlineKeyboardButton("D) " + question['listAnswer'][3], callback_data=str(FOUR)),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    editCorrectAnswerById(teleId,answer[index_corect(question['listAnswer'], question['correct_answer'])])
    question_bold="*"+question['question']+"*"
    query.edit_message_text(
        text=question_bold,parse_mode="Markdown", reply_markup=reply_markup
    )

    return THIRD

# FIRST -> ONE

def start_over(update: Update, context: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("chosse level", callback_data=str(ONE)),
            InlineKeyboardButton("chosse type of question", callback_data=str(TWO)),
            InlineKeyboardButton("Start now", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(text="Start handler, Choose a route", reply_markup=reply_markup)
    return FIRST





def end(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="See you next time!")
    return ConversationHandler.END

def help(update: Update, context: CallbackContext) -> int:
    Uname=update.message.chat.full_name
    update.message.reply_text("🌈🌈🌈Welcome "+Uname+" to english bot🌈🌈🌈\
    \n✨/start to set up and start the test\
    \n✨/info to show your test information"\
    +"\n✨/help to show instuction")

    
def information(update: Update, context: CallbackContext) -> int:
    
    user = update.message.from_user
    teleId=user.id
    checkUser=findUserById(teleId)
    if(checkUser==-1):
        createUser(teleId)
    users=getUserById(teleId)
    Uname=update.message.chat.full_name
    typeOfques=users['type_question']
    nameOfType=findTypeOfQuestion(typeOfques)
    update.message.reply_text("🤵Your telegram id is: "+str(users['id_tele'])+\
    "\n💖Your name is: "+Uname+\
    "\n🏆Your total question is: "+str(users['totalQuestion'])\
    +"\n🥇Your total correct answer is: "+str(users['totalTrue'])+\
    "\n💔Your total incorrect answer is: "+str(users['totalQuestion']-users['totalTrue'])\
    +"\n🚀Your current type of question: "+str(nameOfType)\
    +"\n✈Your level is: "+str(users['difficulty']))

#"totalTrue": 44, "totalQuestion": 195, "type_question": "27", "difficulty": "medium"