from index import*
from button.choice_difficult.index import*
from  helper.Index_correct import*
from helper.getDataApi import*
from helper.index import*
from constant.index import*

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
)

## ------------- Answer ------------------------

def AnswerA(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    teleId=query['message']['chat']['id'] 
    #lấy cau tra lời đúng
    trueAnswer = getCorrectAnswerById(teleId)

    #update.effective_chat("TYPING")

    url = "https://opentdb.com/api.php?amount=1&category=9&type=multiple"
    question = GetQuestion(url)

    keyboard = [
        [
            InlineKeyboardButton("A) " + question['listAnswer'][0], callback_data=str(ONE)),
            InlineKeyboardButton("B) " + question['listAnswer'][1], callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("C) " + question['listAnswer'][2], callback_data=str(THREE)),
            InlineKeyboardButton("D) " + question['listAnswer'][3], callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
     
    text = ""
     
    if trueAnswer == 'A':
        text = "Correct Answer!\tNext question:\n" + question['question']
        editTotalQuestion(teleId, True)
    else:
        text =   "A is wrong anwser!     " + trueAnswer + " is correct!\n" + question['question']
        editTotalQuestion(teleId, False)

    # lưu câu trả lời đúng mới
    editCorrectAnswerById(teleId , answer[index_corect(question['listAnswer'], question['correct_answer'])] )

    query.edit_message_text(
        text=text, reply_markup=reply_markup
    )

    return THIRD


def AnswerB(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    teleId=query['message']['chat']['id'] 
    #lấy cau tra lời đúng
    trueAnswer = getCorrectAnswerById(teleId)

    url = "https://opentdb.com/api.php?amount=1&category=9&type=multiple"
    question = GetQuestion(url)

    keyboard = [
        [
            InlineKeyboardButton("A) " + question['listAnswer'][0], callback_data=str(ONE)),
            InlineKeyboardButton("B) " + question['listAnswer'][1], callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("C) " + question['listAnswer'][2], callback_data=str(THREE)),
            InlineKeyboardButton("D) " + question['listAnswer'][3], callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
     
    text = ""
    index_choice = int(query.data)
     
    if trueAnswer == 'B':
        text = "Correct Answer!\tNext question:\n" + question['question']
        editTotalQuestion(teleId, True)
    else:
        text =  "B is wrong anwser! " + trueAnswer + " is correct!\n" + question['question']
        editTotalQuestion(teleId, False)

    # lưu câu trả lời đúng mới
    editCorrectAnswerById(teleId , answer[index_corect(question['listAnswer'], question['correct_answer'])] )

    query.edit_message_text(
        text=text, reply_markup=reply_markup
    )

    return THIRD


def AnswerC(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    teleId=query['message']['chat']['id'] 
    #lấy cau tra lời đúng
    trueAnswer = getCorrectAnswerById(teleId)

    url = "https://opentdb.com/api.php?amount=1&category=9&type=multiple"
    question = GetQuestion(url)

    keyboard = [
        [
            InlineKeyboardButton("A) " + question['listAnswer'][0], callback_data=str(ONE)),
            InlineKeyboardButton("B) " + question['listAnswer'][1], callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("C) " + question['listAnswer'][2], callback_data=str(THREE)),
            InlineKeyboardButton("D) " + question['listAnswer'][3], callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
     
    text = ""
    index_choice = int(query.data)
     
    if trueAnswer == 'C':
        text = "Correct Answer!\tNext question:\n" + question['question']
        editTotalQuestion(teleId, True)
    else:
        text = "C is wrong anwser!     " + trueAnswer + " is correct!\n" + question['question']
        editTotalQuestion(teleId, False)

    # lưu câu trả lời đúng mới
    editCorrectAnswerById(teleId , answer[index_corect(question['listAnswer'], question['correct_answer'])] )

    query.edit_message_text(
        text=text, reply_markup=reply_markup
    )

    return THIRD

def AnswerD(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    teleId=query['message']['chat']['id'] 
    #lấy cau tra lời đúng
    trueAnswer = getCorrectAnswerById(teleId)

    url = "https://opentdb.com/api.php?amount=1&category=9&type=multiple"
    question = GetQuestion(url)

    keyboard = [
        [
            InlineKeyboardButton("A) " + question['listAnswer'][0], callback_data=str(ONE)),
            InlineKeyboardButton("B) " + question['listAnswer'][1], callback_data=str(TWO)),
        ],
        [
            InlineKeyboardButton("C) " + question['listAnswer'][2], callback_data=str(THREE)),
            InlineKeyboardButton("D) " + question['listAnswer'][3], callback_data=str(FOUR)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
     
    text = ""
    index_choice = int(query.data)
     
    if trueAnswer == 'D':
        text = "Correct Answer!\tNext question:\n" + question['question']
        editTotalQuestion(teleId, True)
    else:
        text = "D is wrong anwser! " + trueAnswer + " is correct!\n" + question['question']
        editTotalQuestion(teleId, False)

    # lưu câu trả lời đúng mới
    editCorrectAnswerById(teleId , answer[index_corect(question['listAnswer'], question['correct_answer'])] )

    query.edit_message_text(
        text=text, reply_markup=reply_markup
    )

    return THIRD
 