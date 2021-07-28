from index import*
import logging
import requests
from  helper.Index_correct import*
from helper.getDataApi import*
from helper.index import*
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND, THIRD = range(3)
# Callback data
ONE, TWO, THREE, FOUR = range(4)

answer = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

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
            InlineKeyboardButton("chọn độ khó", callback_data=str(ONE)),
            InlineKeyboardButton("chọn loại câu hỏi", callback_data=str(TWO)),
            InlineKeyboardButton("Start now", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("Start handler, Choose a route", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST

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

    query.edit_message_text(
        text=question['question'], reply_markup=reply_markup
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
            InlineKeyboardButton("chọn độ khó", callback_data=str(ONE)),
            InlineKeyboardButton("chọn loại câu hỏi", callback_data=str(TWO)),
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
